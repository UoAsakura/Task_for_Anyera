from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверяем запрос не для изменения данных.
        if request.method in permissions.SAFE_METHODS:
            # Даём доступ для всех пользователей.
            return True
        # Иначе только для администратора.
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Даём доступ для всех пользователей, если запрос не на изменение.
            return True
        # Если пользователь который пришёл с запросом,
        # является пользователем-создателем из БД, тогда даём доступ.
        return obj.user == request.user