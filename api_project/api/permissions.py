from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    """
    def has_permission(self, request, view):
        # Read-only permissions are allowed for any request
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # Write permissions are only allowed to the admin user
        return request.user and request.user.is_staff
