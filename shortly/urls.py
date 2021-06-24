from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shortner import views

router = routers.DefaultRouter()
router.register(r'', views.UrlViewSet)

urlpatterns = [
    path('', include("shortner.urls")),
    path('api/', include(router.urls)),
    path('panel/', include("panel.urls")),
    path('admin/', admin.site.urls),
    path('api-urls/', include('rest_framework.urls', namespace='rest_framework')),
]
