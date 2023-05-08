from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import dataBase
from .serializers import DatabaseSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'/api/data'},
        {'GET':'/api/data/id'},
        {'GET':'/api/data/topic/topic_name'}
    ]
    return Response(routes)

@api_view(['GET'])
def getData(request):
    data=dataBase.objects.all()
    serializer=DatabaseSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDatabyID(request,pk):
    data=dataBase.objects.get(id=pk)
    serializer=DatabaseSerializer(data)
    return Response(serializer.data)


@api_view(['GET'])
def getDatabyTopic(request, pk):
    data = dataBase.objects.filter(topic__icontains=pk)
    serializer = DatabaseSerializer(data, many=True)
    return Response(serializer.data)
