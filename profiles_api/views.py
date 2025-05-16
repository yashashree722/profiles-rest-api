# from django.shortcuts import render, render_to_response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from profiles_api import models
from profiles_api import serializers
# from profiles_api.serializers import  UserProfileSerializer
from profiles_api import permissions
from profiles_api.permissions import UpdateOwnProfile,UpdateOwnstatus
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views  import ObtainAuthToken
from rest_framework.settings import api_settings
class UserProfileViewset(viewsets.ModelViewSet):
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
    permissions.UpdateOwnProfile,
    )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name' , 'email' ,)
    
class UserLoginApiView(ObtainAuthToken):
    """handle creating user auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    
    

class UserProfileFeedViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset  = models.ProfileFeedItem.objects.all()
    permission_classes = (UpdateOwnstatus,IsAuthenticated)
    
    
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user) 
    