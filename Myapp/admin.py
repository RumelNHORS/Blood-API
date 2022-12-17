from django.contrib import admin
from . models import UserProfile, DonorList, User

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'blod_group', 'email', 'phone']

@admin.register(DonorList)   
class DonorListAdmin(admin.ModelAdmin):
    list_display = ['id', 'donor_name','blood_group', 'age', 'phone', 'email']

@admin.register(User)
class Login(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'email']