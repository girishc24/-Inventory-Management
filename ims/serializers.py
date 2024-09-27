from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *



class UserCreateSerializer(serializers.ModelSerializer):
    class  Meta:
        model  =  User
        fields = ['id','first_name','last_name','email','password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, attrs):
        attrs['username'] = attrs['email']  
        return attrs

    def save(self, **kwargs):
        password = self.validated_data.get('password')
        if password:  
            self.validated_data['password'] = make_password(password)  
        return super().save(**kwargs)


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= ['phone','designation','company','department','emp_id']
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description'] 
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
           
        }