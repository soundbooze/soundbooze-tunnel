from django.shortcuts import render
from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer
 
# Create your views here.

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
