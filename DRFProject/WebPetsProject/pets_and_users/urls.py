from pets_and_users import views
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# Урлы с разделом о сортах винограда.
urlpatterns = [
    # Главная страница о сортах.
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/pet/', views.PetAPIList.as_view()),
    path('api/v1/women/<int:pk>/',  views.PetAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/',  views.PetAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]