from django.contrib import admin

from .models import Order, Product, Sale


@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "quantity", "price"]
    
    
@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity"]
    

@admin.register(Sale)
class UserAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "total_price"]

