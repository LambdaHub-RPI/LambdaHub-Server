from rest_framework import serializers
from ..models import Ride

class RideModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'

        
