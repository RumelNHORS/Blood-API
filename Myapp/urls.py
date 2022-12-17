from django.urls import path, include
from Myapp import views
from rest_framework.routers import DefaultRouter



routers=DefaultRouter()
routers.register('profileapi',views.ProfileModelViewSet,basename='profile')
routers.register('donorlist', views.DonorModelViewSet,basename='donor_list')


urlpatterns = [
    path('',include(routers.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    
]
