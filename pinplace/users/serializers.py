# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username' ,'email', 'password', 'is_staff']

# class RegistrationSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password1', 'password2']
#         extra_kwargs = {
#             'password': { 'write_only': True }
#         }
    
#     def save(self):
#         user = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username'],
#         )
#         password1 = self.validated_data['password1'],
#         password2 = self.validated_data['password2']

#         if password1 != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match'})
#         user.set_password(password1)
#         user.save()
#         return user