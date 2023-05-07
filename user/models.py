from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.username = self.email
        print(args,kwargs)
        return super().save(*args, **kwargs)
    

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    
    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
    