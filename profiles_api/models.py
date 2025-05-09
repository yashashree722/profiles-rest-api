from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class  UserProfile(AbstractBaseUser,PermissionsMixin):
    """ DB model for user cutom model"""
    email = models.EmailField(max_length= 255, unique=True)
    name = models.CharField(max_length= 100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name' ]
    
    def get_full_name(self):
        """ get the full name of user"""
        return self.name 

    def get_short_name(self):
        return self.name

         
    def __str__(self):
        return self.email 
    