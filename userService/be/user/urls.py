from django.contrib import admin
from django.urls import path
from user.api.v1.views import register_client_user_view, login_user_view

urlpatterns = [
    path("auth/client/register/", register_client_user_view, name="register-client"),
    path("auth/login/", login_user_view, name="login-user"),
]
