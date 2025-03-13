from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already taken.")
        return value

    def validate_password(self,value):
        print(value)
        if len(value)<8:
            raise serializers.ValidationError("Password should be minimum 8 characters long")
        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])  # Hashing the password
        user.save()
        return user