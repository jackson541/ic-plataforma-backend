from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class SalesmanView(generics.ListCreateAPIView):
    queryset = Salesman.objects.all()
    serializer_class = SalesmanSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
