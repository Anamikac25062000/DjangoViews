from django.db.models import fields
from rest_framework import serializers

# from authentication.views import passwordrule as passwordrules
from .models import *
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"inut_type": "password"})
    
    first_name = serializers.CharField(required=True, allow_null=False)
    last_name = serializers.CharField(required=True, allow_null=False)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "mobile_phone",
            "status",
            "role_id"
        ]
        # exclude = ["groups","user_permissions","last_login"]

    # def validate_password(self, data):
    #         validators.validate_password(password=data, user=User)
    #         return data
    def validate_password(self, attrs):
        password = attrs
        alphabets = digits = special = 0
        password_rule = PasswordRule.objects.filter(status=0).first()
        for i in range(len(password)):
            if password[i].isalpha():
                alphabets = alphabets + 1
            elif password[i].isdigit():
                digits = digits + 1
            else:
                special = special + 1
        if password_rule.minimumcharaters > len(
            password
        ) or password_rule.maximumcharaters < len(password):
            raise serializers.ValidationError({
                "Status": "1",
                "Message": "Password length must be greater than eight characters or less than fifteen character",
            })
        if special > password_rule.specialcharaters or special == 0:
            raise serializers.ValidationError ({
                "Status": "1",
                "Message": "The password must contain at least one special character and  at most three special characters",
            })
        if digits < password_rule.uppercase:
            raise serializers.ValidationError( {
                "Status": "1",
                "Message": "The password must contain at least one digit",
            })
        return attrs
    
    def save(self):
        reg = User(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
            password=make_password(self.validated_data["password"]),
            mobile_phone=self.validated_data["mobile_phone"],
            role_id=self.validated_data["role_id"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
        )
        reg.save()


class UserSerializer(serializers.ModelSerializer):

    role = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()


    def get_role(self, instance):
        if instance.role_id:
            data = {
                "id":instance.role_id.role_id,
                "name":instance.role_id.name
            }
            return data
    
    def get_full_name(self, instance):
       if instance.first_name and instance.last_name:
        data = f"{instance.first_name} {instance.last_name}"
        return data

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "mobile_phone",
            "date_joined",
            "status",
            "role",
            "full_name"
            "user_id"
        ]
        


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(style={"input_type": "password"})


class PasswordChangeSerializer(serializers.Serializer):

    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)
    confirmpassword = serializers.CharField(max_length=128)



class LoginResponseSerializer(serializers.ModelSerializer):

    role = serializers.SerializerMethodField()
    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()

    def get_role(self, instance):
        data = {
            "id":instance.role_id.role_id,
            "name":instance.role_id.name
        }
    
        return data
    def get_refresh_token(self, instance):
        return str(RefreshToken.for_user(instance))
    
    def get_access_token(self, instance):
        return str(RefreshToken.for_user(instance).access_token)
    
    class Meta:
        model = User
        fields = [
            "user_id",
            "username",
            "email",
            "first_name",
            "last_name",
            "mobile_phone",
            "date_joined",
            "status",
            "role",
            "access_token",
            "refresh_token"
        ]
        
class UserCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "mobile_phone",
            "date_joined",
            "status",
            "role_id",
        ]