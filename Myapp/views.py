from .models import UserProfile, DonorList
from .serializers import ProfileSerializer, DonorSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import response, status
from Myapp.serializers import RegisterSerializer
from django.contrib.auth import authenticate
#from knox.models import AuthToken
#Login rest framework
#from django.contrib.auth import login
#from rest_framework.authtoken.serializers import AuthTokenSerializer
#from knox.views import LoginView as KnoxLoginView
from rest_framework.filters import SearchFilter

#User Profile View
class ProfileModelViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

#Donor List View
class DonorModelViewSet(viewsets.ModelViewSet):
    queryset = DonorList.objects.all()
    serializer_class = DonorSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['blood_group', 'address']


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class LoginAPIView(GenericAPIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        user = authenticate(username=email, password=password)
        
        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'msg': 'Invalid Credentials, Try Again'}, status=status.HTTP_401_UNAUTHORIZED)
