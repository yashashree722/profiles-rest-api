# from django.shortcuts import render, render_to_response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from profiles_api import models
from profiles_api import serializers
# from profiles_api.serializers import  UserProfileSerializer
from profiles_api import permissions
from profiles_api.permissions import UpdateOwnProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

class UserProfileViewset(viewsets.ModelViewSet):
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
    permissions.UpdateOwnProfile,
    )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name' , 'email' ,)
    
    

# 