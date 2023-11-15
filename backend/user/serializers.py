from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    role = serializers.CharField(source="user.role", read_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data["role"] = user.role
        data["id"] = user.id
        return data


class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
