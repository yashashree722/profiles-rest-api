from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allowe user to edit own profile """
    def has_object_permission(self, request, view, obj):
        """ check use is trying to edit or update profile 
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id 
    
    
        