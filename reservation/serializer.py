from rest_framework import serializers
from reservation.models import Appointment
from drm.models import Doctor
from datetime import datetime


class AppointmentSerializer(serializers.Serializer):
    
    name=serializers.CharField()

    phone=serializers.CharField()

    email=serializers.EmailField()

    doctor=serializers.IntegerField()

    appointment_date=serializers.DateField()

    appointment_time=serializers.TimeField()

    appointment_end_time=serializers.TimeField(read_only=True)

    duration=serializers.IntegerField()

    token=serializers.IntegerField(null=True)

    def create(self,validated_data):
        return Appointment.objects.create(**validated_data)

    def validate(self,validated_data):
        duration=validated_data.get("duration")
        if duration not in range(1,5):
            raise serializers.ValidationError("invalid duration time")    
        
        doctor_id=validated_data.get("doctor")
        if not doctor.objects.filter(id=doctor).exists():
            raise serializers.ValidationError("doctor not exists")

        appointment_date=validated_data.get("appointment_date")
        if appointment_date < datetime.today().date():
            raise serializers.ValidationError("invalid appointment_date")
        return validated_data    