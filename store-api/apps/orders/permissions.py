from rest_framework.permissions import BasePermission ,IsAdminUser


class IsCustomer(BasePermission):

    def has_object_permission(self, request, view, obj):

        return bool (
            IsAdminUser or
            request.user and
            request.user == obj.customer

        )
        
