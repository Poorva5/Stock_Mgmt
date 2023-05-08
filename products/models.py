from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(help_text='total quantity of the product in stock')
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text='unit price of the product')
    created_at = models.DateTimeField(auto_now_add=True)

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(help_text='number of units sold')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, help_text='total price of the sale')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def profit_or_loss(self):
        cost = self.product.price * self.quantity
        revenue = self.total_price
        profit_or_loss = revenue - cost
        return profit_or_loss

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
        