from rest_framework import serializers
from django.contrib.auth import get_user_model  # This imports the custom user model
from rest_framework.authtoken.models import Token

# Get the user model (this works with both the default and custom user model)
User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile_picture', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # This method handles the creation of a user and ensures the password is hashed
    def create(self, validated_data):
        # Use the create_user method to create the user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],  # Ensure the password is hashed
            bio=validated_data.get('bio', ''),  # Optional fields can have default values
            profile_picture=validated_data.get('profile_picture', None)
        )
        
        # Generate and associate a token with the new user
        Token.objects.create(user=user)
        
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
