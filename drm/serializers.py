from rest_framework import serializers
from drm.models import Doctor

class DoctorSerializer(serializers.Serializer):
    
    id=serializers.IntegerField(read_only=True)

    name=serializers.CharField() 

    specilaization=serializers.CharField()

    experience=serializers.IntegerField()

    fee=serializers.IntegerField()

    def create(request,validated_data):
        return Doctor.objects.create(**validated_data)

    def update(request,instance,validated_data):
        for attribute,value in validated_data.items():
            setattr(instance,attribute,value)
            return instance    