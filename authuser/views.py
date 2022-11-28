from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Transaksi
from .serializers import UserSerializer, TransaksiSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer

# Create your views here
