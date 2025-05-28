from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .serializers import PlanetSerializer, PlanetListSerializer
from .models import Planet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view()
def planet_list_view(request, slug=None):
    if not slug:serializer = PlanetListSerializer(Planet.objects.all(),many=True);return Response(serializer.data)
    elif request.user.is_authenticated:return Response(PlanetSerializer(get_object_or_404(Planet, slug=slug)).data)
    return Response({'message':'authentication required for further exploration'})

@swagger_auto_schema(method='POST', request_body=PlanetSerializer)
@api_view(['POST'])
def planet_create_view(request):
    if request.user.is_authenticated:return Response({'message':'authentication required for further exploration'})
    serializer = PlanetSerializer(data=request.data)
    if serializer.is_valid():serializer.save();return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors)

@swagger_auto_schema(methods=['PATCH', 'PUT'], request_body=PlanetSerializer)
@api_view(['PUT', 'PATCH'])
def planet_update_view(request, slug):
    if request.user.is_authenticated:return Response({'message':'authentication required for further exploration'})
    serializer = PlanetSerializer(get_object_or_404(Planet, slug=slug), data=request.data, partial=True if request.method=='PATCH' else False)
    if serializer.is_valid():serializer.save();return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['Delete'])
def planet_delete_view(request, slug):
    if request.user.is_authenticated:return Response({'message':'authentication required for further exploration'})
    try:get_object_or_404(Planet, slug=slug).delete();return Response({'message':'Successfully deleted!'})
    except:return Response({'message':'An error occured by trying to delete that'})

