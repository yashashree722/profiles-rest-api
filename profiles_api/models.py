from django.db import models
from django.conf import  settings

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
# Create your models here.
class UserProfileManager(BaseUserManager):
    """Mnager for user Profiles"""
    def create_user(self,email,name,password=None):
        """Create a new suer profile"""
        if not email:
            raise ValueError ('Must have email address')
        
        email = self.normalize_email(email)
        user = self.model(email= email ,name = name)
        
        
        
        user.set_password(password)
        user.save(using =self._db)
        return user
    
    def create_superuser(self,email, name,password):
        user = self.create_user(email,name,password)
        user.is_superuser =True
        user.is_staff = True
        
        user.save(using = self._db)
        return user


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
    
    
    
class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status_text