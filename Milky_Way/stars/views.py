from .serializers import StarSerializer
from .models import Star
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


@api_view()
def star_list_view(request):
    return Response(StarSerializer(Star.objects.all(), many=True).data)

@swagger_auto_schema(method='POST', request_body=StarSerializer)
@api_view(['POST'])
def star_create_view(request):
    serializer = StarSerializer(data=request.data)
    if serializer.is_valid():serializer.save();return Response(serializer.data)
    return Response(serializer.errors)
