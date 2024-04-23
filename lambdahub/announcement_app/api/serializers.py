from rest_framework import serializers
from ..models import Announcement

class AnnouncementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id', 'title','author', 'date', 'announcement')