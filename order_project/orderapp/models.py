from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from django.utils import timezone

from userapp.models import AppUser


class NameModelMixin(models.Model):
    name = models.CharField(max_length=70,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Order(NameModelMixin):
    status_vars = (
        ('0', 'Cозданный'),
        ('1', 'Подтверждённый'),
        ('2', 'Отклонённый'),
    )

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    user = models.ForeignKey(AppUser, on_delete=models.PROTECT, related_name='users')
    inspector = models.ForeignKey(AppUser, on_delete=models.PROTECT, blank=True, null=True,
                                  related_name='inspectors', default=None)
    status = models.CharField(max_length=1,
                              choices=status_vars,
                              default=status_vars[0][0],
                              verbose_name='статус заказа')
    comment = models.TextField(default='не указан',
                               verbose_name='комментарий')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    @admin.display(description='статус заказа',
                   ordering='status')
    def get_status_view(self):
        if self.status == '-1':   # изменённый
            fmt = '<div style="color: green"><b>Изменённый</b>' \
                  '<br>Время: {datetime_now}<div>'
            return format_html(fmt.format(datetime_now=timezone.now().strftime("%m/%d/%Y, %H:%M:%S")))

        if self.status == '0':   # Cозданный
            return format_html('<b>{}</b>'.
                               format(self.status_vars[int(self.status)][1]))

        if self.status == '1':   # Подтверждённый
            fmt = '<div style="color: blue"><b>{status}</b>,' \
                  '<br>{inspector},' \
                  '<br>Время: {datetime_now}<div>'
            return format_html(fmt.format(status=self.status_vars[int(self.status)][1],
                                          inspector=self.inspector,
                               datetime_now=timezone.now().strftime("%m/%d/%Y, %H:%M:%S")))

        if self.status == '2':  # Отклонённый
            fmt = '<div style="color: red"><b>{status}</b>,' \
                  '<br>Время: {datetime_now},' \
                  '<br>{inspector},' \
                  '<br>Комментарий: {comment}<div>'
            return format_html(fmt.format(status=self.status_vars[int(self.status)][1],
                                          datetime_now=timezone.now().strftime("%m/%d/%Y, %H:%M:%S"),
                                          inspector=self.inspector,
                                          comment=self.comment))


class Product(NameModelMixin):
    link = models.CharField(max_length=250, verbose_name='ссылка на товар')
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              verbose_name='категория',
                              related_name='order')
    comment = models.CharField(default='не указан',
                               verbose_name='комментарий к товару',
                               max_length=300)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
