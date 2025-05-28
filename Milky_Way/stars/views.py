from .serializers import StarSerializer, StarListSerializer
from .models import Star
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404


@api_view()
def star_list_view(request, slug=None):
    if slug:return Response(StarSerializer(get_object_or_404(Star,slug=slug)).data)
    return Response(StarListSerializer(Star.objects.all(), many=True).data)

@swagger_auto_schema(method='POST', request_body=StarSerializer)
@api_view(['POST'])
def star_create_view(request):
    if not request.user.is_authenticated:return Response({'message':'Login required!'})
    serializer = StarSerializer(data=request.data)
    if serializer.is_valid():serializer.save();return Response(serializer.data)
    return Response(serializer.errors)

@swagger_auto_schema(methods=['PUT', 'PATCH'], request_body=StarSerializer)
@api_view(['PATCH', 'PUT'])
def star_update_view(request, slug):
    if not request.user.is_authenticated:return Response({'message':'Login required!'})
    serializer = StarSerializer(get_object_or_404(Star, slug=slug), data=request.data, partial=(request.method=='PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def star_delete_view(request, slug):
    if not request.user.is_authenticated:return Response({'message':'Login required!'})
    try:get_object_or_404(Star, slug=slug).delete();return Response({'message':'Successfully deleted!'})
    except:return Response({'message':'An error occured!'})
