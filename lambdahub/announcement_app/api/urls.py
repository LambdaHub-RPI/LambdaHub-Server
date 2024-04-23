from rest_framework import routers
from .views import AnnouncementViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'announcements', AnnouncementViewSet)

urlpatterns = {
    path('', include(router.urls))
}