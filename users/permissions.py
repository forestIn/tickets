from rest_framework import permissions

class IsDispatcher(permissions.BasePermission):
    """
    Object-level permission to only allow admin of an object to edit it.    
    """   
    def has_permission(self, request, view):
        return request.user.type_user=='DP'

