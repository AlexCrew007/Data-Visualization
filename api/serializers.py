from rest_framework import serializers
from app.models import dataBase

class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = dataBase
        fields = '__all__'