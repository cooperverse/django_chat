from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterApiView
urlpatterns = [
    path("registration/", RegisterApiView.as_view(), name="registration"),
    path("login/", TokenObtainPairView.as_view(), name="login")
]
