from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    # check passwords
    # avoid duplicate emails
    # remove confirm_password
    def save(self):
        username = self.validated_data['username']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        email_given = self.validated_data['email']

        if password != confirm_password:
            raise serializers.ValidationError({'error':"Passwords didn't match"})
        
        if User.objects.filter(email=email_given).exists():
            raise serializers.ValidationError({'error':"Email already Exists"})
        
        account = User(email=email_given, username=username)
        account.set_password(password)
        account.save()

        return account
