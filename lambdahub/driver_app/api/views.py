from rest_framework import viewsets
from ..models import Ride
from .serializers import RideModelSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideModelSerializer