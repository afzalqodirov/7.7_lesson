from rest_framework.response import Response
from .serializers import JustSerializer, PeopleSerializer 
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='POST', request_body=JustSerializer)
@api_view(['POST'])
def register_view(request):
    password = request.data.get('password')
    if password and len(password) >= 8 and password == request.data.get('confirm_password'):
        try:
            user = User.objects.create(username=request.data['username'], email=request.data['email'])
            user.set_password(password)
            user.save()
            return Response({'message':f'Congratulations! the user {request.data['username']} is created!'})
        except:return Response({'message':'Unexpected error occured!'})
    return Response({'message':'The password should contain atleast 8 characters and it must be the same as confirm password field'})

@api_view()
def users_view(request):
    if not request.user.is_authenticated:return Response({'message':'You\'re not authenticated!'})
    if request.user.is_superuser:return Response(PeopleSerializer(User.objects.all(), many=True).data)
    return Response({'message':'You are not superuser!'})
