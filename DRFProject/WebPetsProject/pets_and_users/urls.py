from pets_and_users import views
from django.urls import path

# Урлы с разделом о сортах винограда.
urlpatterns = [
    # Главная страница о сортах.
    path('api/v1/pet/', views.PetAPIList.as_view()),
]