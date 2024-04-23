from rest_framework import viewsets
from ..models import Announcement
from .serializers import AnnouncementModelSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementModelSerializer
    