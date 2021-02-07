from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', "username", "email", "password"]

class SalesmanSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Salesman
        fields = ['id', 'user', 'first_name', 'last_name', "phone", "email", "password", 'date_of_birth', 'photo', 'address', 'town_hall_number']
    def get_user(self, obj):
        return UserSerializer(obj.user).data
    def create(self, validated_data):
        if User.objects.filter(username=validated_data['phone']).exists():
            raise serializers.ValidationError({"error": "Já existe um usuário cadastrado com esse telefone."})
        user = User.objects.create(
            first_name=validated_data['first_name'],
            username=validated_data['phone'], 
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        try:
            salesman = Salesman.objects.create(
                date_of_birth=validated_data['date_of_birth'],
                photo=validated_data['photo'],
                address=validated_data['address'],
                town_hall_number=validated_data['town_hall_number'], 
                user=user
            )
            return salesman
        except Exception as e:
            print(e)
            user.delete()
            return {"detail": "erro na criação do vendedor."}

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Client
        fields = ['id', 'user', 'first_name', 'last_name', "phone", "email", "password", 'date_of_birth', 'photo', 'address']
    def get_user(self, obj):
        return UserSerializer(obj.user).data
    def create(self, validated_data):
        if User.objects.filter(username=validated_data['phone']).exists():
            raise serializers.ValidationError({"error": "Já existe um usuário cadastrado com esse telefone."})
        user = User.objects.create(
            first_name=validated_data['first_name'],
            username=validated_data['phone'], 
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        try:
            client = Client.objects.create(
                date_of_birth=validated_data['date_of_birth'],
                photo=validated_data['photo'],
                address=validated_data['address'],
                user=user
            )
            return client
        except Exception as e:
            print(e)
            user.delete()
            raise serializers.ValidationError({"error": "erro na criação do cliente."})

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'amount', 'name', 'description', 'salesman', 'photo', 'price']
    def create(self, validated_data):
        salesman = Salesman.objects.get(user=self.context['user'])
        product = Product.objects.create(**validated_data, salesman=salesman)
        return product