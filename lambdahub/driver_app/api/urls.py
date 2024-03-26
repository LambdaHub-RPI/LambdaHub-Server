from rest_framework import routers
from .views import RideViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'rides', RideViewSet)

urlpatterns = [
    path('', include(router.urls))
]