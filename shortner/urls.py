from django.contrib import admin
from django.urls import path
from .views import UrlResolver, redirect_to_login

urlpatterns = [
    path("<str:url>", UrlResolver.as_view(), name="url_resolver"),
    path("", redirect_to_login, name="login"),
]
