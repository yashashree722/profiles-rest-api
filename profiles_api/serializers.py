from rest_framework import serializers
from profiles_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """serialisers use rprofile """
    class Meta:
        model = models.UserProfile
        fields = ('id' , 'email' , 'name' , 'password')
        
        extra_kwargs ={
            'password' :{
                'write_only' : True,
                'style' :{'input_type' : 'password'}
                
            }
        }
        
        def create(slf , validated_data):
            user = models.UserProfile.objects.create_user(
                email = validated_data['email'],
                name =validated_data['name'],
                password = validated_data['password']
                
            )
            return user

    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id' , 'user_profile' , 'status_text' , 'created_on')
        extra_kwagrs ={
            'user_profile': {
                'read_only' :True
            }
            
        }