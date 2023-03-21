from django.contrib import admin

from .models import Product, Order


# можно не показывать эту таблицу в админке, пока оставил
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order', 'link')
    list_display_links = ('id', 'name')


class ProductInlineAdmin(admin.TabularInline):
    model = Product
    extra = 0
    show_change_link = True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    user_fieldsets = (
        ('Форма заполнения', {
            'fields': ('name', )
        }),
    )

    fieldsets = [
        ('Форма заполнения', {
            'fields': ('name', )
        }),
        ('Форма подтверждения администратора', {
            'fields': ('status', 'comment'), 'classes': ['collapse']
        }),
    ]

    list_display = ('id', 'name', 'created_at', 'user', 'get_status_view',)
    list_display_links = ('id', 'name',)
    ordering = ['-created_at']
    inlines = [ProductInlineAdmin]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # при создании заказа пользователь проставляется автоматически
            obj.user = request.user
        else:
            # если заказ уже имеется в базе, т.е редактируется
            # проверяю если открывает админ
            if request.user.is_superuser:
                # и меняет статус, то указываю его в качестве инспектора
                if obj.status != 0:
                    obj.inspector = request.user
            # если редактуриет заказ пользователь
            else:
                # (самодеятельность), то меняю статус на измененный чтобы выделить этот момент
                obj.status = '-1'
                # и убираю "флаг" проверки администратором
                obj.inspector = None
        super(OrderAdmin, self).save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super(OrderAdmin, self).get_fieldsets(request, obj)
        return self.user_fieldsets

    # если заказ редактируется пользователем, то запрещаю менять название заказа
    # показалась эта идея хорошей
    def get_readonly_fields(self, request, obj=None):
        if obj and not request.user.is_superuser:
            return ['name', ]
        else:
            return []