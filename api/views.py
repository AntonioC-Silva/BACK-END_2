from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor
from .serializers import  AutorSerializers

class AutoresView(ListCreateAPIView): #creat post  list get
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers

class Crud(RetrieveUpdateDestroyAPIView): #creat post  list get
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers



# Create your views here.
