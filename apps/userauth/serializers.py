from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import Address, User, ManagerUser, CustomerUser, SupplierUser

class AddressSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('__all__')

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerUser
        fields = ('__all__')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierUser
        fields = ('__all__')