from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class AppUser(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    patronymic = models.CharField(max_length=50, verbose_name='отчество')
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=12, verbose_name='телефон')

    def __str__(self):
        return self.username