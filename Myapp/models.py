from django.db import models
from django.conf import settings
import jwt
from datetime import datetime, timedelta


class User(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    address = models.TextField(max_length=300)
    
    @property
    def token(self):
        token = jwt.encode({'username':self.user_name, 'email':self.email, 'exp':datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY, algorithm='HS256')
        return token
        
    

class UserProfile(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=300)
    blod_group = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    social = models.CharField(max_length=300)
    last_dination = models.DateField()
    bio = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.full_name
    
class DonorList(models.Model):
    donor_name = models.CharField(max_length=20)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    
    def __str__(self):
        return self.donor_name
    
