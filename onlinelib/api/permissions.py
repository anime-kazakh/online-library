from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Читать могут все. Удалять, обновлять, записывать могут только админы.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешает доступ к endpoint пользователям из группы.
    Разрешает доступ к объекту автору или админу.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._group_name = 'author'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        return request.user.groups.filter(name=self._group_name).exists()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        return obj.user == request.user


class IsOwnerStuffOrReadOnly(permissions.BasePermission):
    """
    Проверка на автора или админа.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        return obj.user == request.user