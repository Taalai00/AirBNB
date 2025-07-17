from rest_framework import permissions

class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'host'


class CheckUserReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'quest':
            return True
        return False

class CheckStoreOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.role == request.user:
            return True
        return False
