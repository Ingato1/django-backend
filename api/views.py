from django.shortcuts import render

# Create your views here.

from .models import Teachers,students
from .serializers import TeachersSerializer,studentsSerializer
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response

class TeachersView(viewsets.ModelViewSet):
    queryset=Teachers.objects.all()
    serializer_class=TeachersSerializer
    
class studentsView(viewsets.ModelViewSet):
    queryset=students.objects.all()
    serializer_class=studentsSerializer
