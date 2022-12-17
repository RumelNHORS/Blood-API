from rest_framework import serializers
from . models import UserProfile, DonorList, User
#from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, min_length=6, write_only=True )
    class Meta:
        model = User
        fields = ('user_name', 'email', 'phone', 'blood_group', 'password')
        
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
class LoginSerilizer(serializers.ModelSerializer):
     password = serializers.CharField(max_length=20, min_length=6, write_only=True)
     class Meta:
         model = User
         fields = ('email', 'password', 'token')
         
         read_only_fields = ['token']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorList
        fields = '__all__'
