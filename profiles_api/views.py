# from django.shortcuts import render, render_to_response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from profile_project.profiles_api.serializers import HelloSerializer

# Create your views here.
class HelloApiView(viewsets.ViewSet):
    serializer_class = HelloSerializer
    def create(self , request) :
        serialzier = self . serializer_class(data = request.data)
        if serialzier.is_valid():
            name = serialzier.validated_data.get('name')
            message = f"hello{name}!"
            return Response({'message': message})
        else :
            return Response(
                serialzier.error_messages,
                status= status.HTTP_400_BAD_REQUEST  
            )
         
    def retrieve(self , request , pk=None):
        return Response
    
    def update(self , request , pk=None):
        pass
            
    def partial_update(self , request , pk = None):
        pass
    
    def destroy(self , request ,,, pk = None):
        
            
        
        