from rest_framework.response import Response
from rest_framework.decorators import api_view
from ventilator.models import Ventilator
from .serializers import devicedataSerializer
  
@api_view(['POST'])
def addDevices(request):
    serializer = devicedataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)