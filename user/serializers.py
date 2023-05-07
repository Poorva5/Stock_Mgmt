from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from user.models import CustomUser, Address


class CustomRegistrationSerializer(RegisterSerializer):
    username = serializers.CharField(required=False)
    phone = serializers.CharField(required=True)    

class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'id', 'username', 'phone']
        extra_kwargs = {
            'username': {'read_only': True},
        }
        

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'user', 'street', 'city', 'state', 'zip_code']
        
        