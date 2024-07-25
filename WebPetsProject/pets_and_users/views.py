from django.shortcuts import render

from rest_framework import generics, viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .models import Pet, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PetSerializer
# Create your views here.

class PetAPIListPagination(PageNumberPagination):
    # Количество записей на страницу.
    page_size = 3
    # Строка, через которую обратившись, клиент может
    # регулировать кол-во отображаемых записей.
    page_size_query_param = 'page_size'
    # Ограничение по регулируемому кол-ву записей.
    max_page_size = 10_000


class PetAPIList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    # Объект в котором с помощью контейнера можно указать,
    # какие действия может делать пользователь (любой пользователь).
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # Активация кастомного класса пагинации.
    pagination_class = PetAPIListPagination


class PetAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    # Изменять может только создатьль объекта.
    permission_classes = [IsAuthenticated]
    # Авторизация только по токену.
    # authentication_classes = [TokenAuthentication]


class PetAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    # Действия связанные с удалением, может производить только администратор.
    permission_classes = [IsAdminOrReadOnly]