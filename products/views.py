import datetime

from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import Response

from .models import Order, Product, Sale
from .serializers import OrderSerializer, ProductSerializer, SaleSerializer
from rest_framework import serializers


class DashboardView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        today = datetime.date.today()
        products = Product.objects.filter(created_at__date=today)
        sales = Sale.objects.filter(created_at__date=today)
        total_stock = sum(product.quantity for product in products)
        total_sales = sum(sale.total_price for sale in sales)
        cost_of_goods_sold = Sale.objects.filter(created_at__date=today).aggregate(
            Sum("product__price")
        )["product__price__sum"]
        profit_and_loss = (
            total_sales - cost_of_goods_sold
            if total_sales and cost_of_goods_sold
            else 0
        )
        new_orders = Order.objects.filter(created_at__date=today)

        product_serializer = ProductSerializer(products, many=True)
        sale_serializer = SaleSerializer(sales, many=True)
        order_serializer = OrderSerializer(new_orders, many=True)
        response_data = {
            "total_stock": total_stock,
            "total_sales": total_sales,
            "total_profit_loss": profit_and_loss,
            "new_orders": order_serializer.data,
            "products": product_serializer.data,
            "sales": sale_serializer.data,
        }

        return Response(response_data)


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [AllowAny]

    def create(self, request):
        # get product instance
        try:
            product_instance = Product.objects.get(id=request.data.get("product"))
        except Product.DoesNotExist:
            return Response("Invalid product id", status=status.HTTP_400_BAD_REQUEST)

        # check if qty exits for the product
        qty = request.data.get("quantity")
        if qty > product_instance.quantity:
            return Response(
                "Not enough stock available for this product",
                status=status.HTTP_400_BAD_REQUEST,
            )

        # save order
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product_instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
