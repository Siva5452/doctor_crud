from django.shortcuts import render
from rest_framework.views import APIView 
from drm.models import Doctor
from drm.serializers import DoctorSerializer
from rest_framework.response import Response
from rest_framework import authentication,permissions

# Create your views here.
class DoctorListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]
    def get(self,request):
        qs=Doctor.objects.all()
        serializer_instance=DoctorSerializer(qs,many=True)
        return Response(serializer_instance.data)

    def post(self,request):
        form_data=request.data 
        serializer_instance=DoctorSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors) 

class DoctorRetrieveUpdateDeleteView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]
    def get(self,request,pk=None):
        qs=Doctor.objects.get(id=pk)
        serializer_instance=DoctorSerializer(qs,many=True)
        return Response(serializer_instance.data) 

    def put(self,request,pk=None):
        form_data=request.data
        serializer_instance=DoctorSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors) 

    def delete(self,request,pk=None):
        Doctor.objects.get(id=pk).delete()
        return Response({"message":"deleted"})

