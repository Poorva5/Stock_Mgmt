# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Order, Dashoard


# @receiver(post_save, sender=Order)
# def update_dashboard(sender, instance, created, **kwargs):
#     if created:
#         dashboard = Dashboard.objects.get(id=1)
#         dashboard.total_sales += instance.total_price
#         dashboard.save()
