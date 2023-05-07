from django.contrib import admin
from .models import CustomUser, Address


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["phone", "email", "username", "is_superuser"]
    

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'street', 'city', 'state', 'zip_code']
