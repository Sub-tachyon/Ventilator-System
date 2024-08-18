from rest_framework import serializers
from ventilator.models import Ventilator

class devicedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventilator
        fields = '__all__'

"""Note: Serializer defines how complex data from Django models should be serialized (converted) into a JSON
 format and vice versa."""