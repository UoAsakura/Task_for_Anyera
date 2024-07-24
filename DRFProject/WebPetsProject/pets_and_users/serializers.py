from rest_framework import serializers
from .models import Pet


# Создаём класс сериализатора, который работает с моделями,
# представлять их в JSON формате и отправлять в ответ на запрос пользователя.
class PetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Pet
        fields = ("name", "breed", "content", "cat", "image", "user")