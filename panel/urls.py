from django.urls import path
from .views import PanelTemplateView, logout_view

urlpatterns = [
    path("", PanelTemplateView.as_view(), name='panel'),
    path("logout", logout_view, name='logout')
]
