from django.contrib import admin
from .models import AppUser


@admin.register(AppUser)
class StoreAppUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_staff', 'email', 'first_name', 'last_name', 'patronymic', 'phone')
    list_display_links = ('id', 'username', 'email')
    # list_editable = ('is_staff', )

