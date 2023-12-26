from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'password', 'avatar')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class ResetPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ("email", "password")

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']

        if UserProfile.objects.filter(email=email).exists():
            user = UserProfile.objects.get(email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'error': 'Please enter valid credentials'})

