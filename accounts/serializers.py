from rest_framework.serializers import ModelSerializer, EmailField, CharField
from django.contrib.auth.models import User

class JustSerializer(ModelSerializer):
    confirm_password = CharField()
    email = EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

class PeopleSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser', 'is_staff']
