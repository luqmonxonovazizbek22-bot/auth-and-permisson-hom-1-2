from django.contrib.auth import get_user_model

from .models import Product
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



User = get_user_model()



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "password"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class VerifyEmailSerializer(serializers.Serializer):
    pre_token = serializers.CharField()
    code = serializers.CharField(min_length=6, max_length=6)


class ResendCodeSerializer(serializers.Serializer):
    pre_token = serializers.CharField()