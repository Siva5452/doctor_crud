from rest_framework.views import APIView
from reservation.serializer import AppointmentSerializer
from rest_framework.response import Response
from datetime import datetime,timedelta,time
from drm.models import Doctor
from rest_framework import authentication,permissions
from reservation.models import Appointment

class AppoinmentView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request):

        form_data=request.data

        serializer_instance=AppointmentSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data=serializer_instance._validated_data

            appointment_date=cleaned_data.get("appointment_date")

            appointment_time=cleaned_data.get("appointment_time")

            duration=cleaned_data.get("duration")

            end_date_time=datetime.combine(appointment_date,appointment_time) + timedelta(minutes=duration)

            appointment_end_time=end_date_time.time()

            doctor_id=cleaned_data.get("doctor")

            doctor_object=Doctor.objects.get(id=doctor_id)

            appointment_objects=Appointment.objects.filter(

                doctor=cleaned_data.get("doctor"),

                appointment_date=cleaned_data.get("appointment_date"),

            )
            
            serializer_instance.save(appointment_end_time=appointment_end_time)

            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)





class BookingSummaryView(APIView):

    def post(self,request):
    

        form_data=request.data

        doctor=form_data.get("doctor")

        appointment_date=datetime.strptime(form_data.get("appointment_date"),"%Y-%m-%d")

        appointments=Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date)

        serializer_instance=AppointmentSerializer(appointments,many=True)

        return Response(serializer_instance.data)               