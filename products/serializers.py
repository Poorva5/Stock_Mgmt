from rest_framework import serializers

from .models import Order, Product, Sale


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "quantity", "price"]


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ["product", "quantity", "total_price"]
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = Order
        fields = ["product", "quantity"]

    # def create(self, validated_data):
    #     print(validated_data)
    #     product = validated_data['product']
    #     quantity = validated_data['quantity']

    #     if quantity < product.quantity:
    #         raise serializers.ValidationError("Not enough stock available for this product.")

    #     product.quantity -= quantity
    #     product.save()

    #     order = Order.objects.create(product=product, quantity=quantity)
    #     return order
