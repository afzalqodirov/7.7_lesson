from rest_framework.serializers import ModelSerializer
from .models import Star

class StarSerializer(ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'
        read_only_fields = ['slug']
