from rest_framework import serializers
from .models import *

class SalesmanSerializer(serializers.ModelSerializer):
    user = serializer.SerializerMethodField()
    class Meta:
        model = Salesman
        fields = ['id', 'user', 'date_of_birth', 'photo', 'address', 'town_hall_number']
    def get_user(self, obj):
        return obj.user
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['phone'], 
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        try:
            user.set_password(validated_data['password'])
            salesman = Salesman.objects.create(**validated_data, user=user)
            return salesman
        except Exception as e:
            print(e)
            user.delete()
            return None

class ClientSerializer(serializers.ModelSerializer):
    user = serializer.SerializerMethodField()
    class Meta:
        model = Client
        fields = ['id', 'user', 'date_of_birth', 'photo', 'address']
    def get_user(self, obj):
        return obj.user
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['phone'], 
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        try:
            user.set_password(validated_data['password'])
            client = Client.objects.create(**validated_data, user=user)
            return client
        except Exception as e:
            print(e)
            user.delete()
            return None

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'amout', 'name', 'description', 'salesman', 'photo', 'price']
    def create(self, validated_data):
        salesman = Salesman.objects.get(user=self.context['user'])
        product = Product.objects.create(**validated_data, salesman=salesman)
        return product