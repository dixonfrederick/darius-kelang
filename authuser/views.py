from rest_framework import viewsets, status
from .models import User, Transaksi
from .serializers import UserSerializer, TransaksiSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from wallet.views import namedtuplefetchall
from django.db import connection
from django.shortcuts import render


def getBalance(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute(
        """SELECT balance FROM wallet WHERE userid=(SELECT username FROM authuser_user WHERE username='donoKasino');""")
    result = namedtuplefetchall(cursor)
    return render(request, 'authuser/test.html', {'result': result})


class UserViewSet(viewsets.ModelViewSet):
    # /api/v1/user [GET,POST]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()


class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer
    permission_classes = [IsAuthenticated]

    # /api/v1/transaksi [GET] (GET transaksi sesuai user yang login)
    def get_queryset(self):
        user = self.request.user
        return Transaksi.objects.filter(users=user)

    # /api/v1/transaksi [POST] (POST transaksi sesuai user yang login)
    def create(self, request, *args, **kwargs):
        user = self.request.user
        data_transaksi = request.data

        # asumsi 5jt adalah balance wallet nanti
        if (data_transaksi['nominal'] < 5000000):
            new_transaksi = Transaksi.objects.create(
                jenisTransaksi=data_transaksi['jenisTransaksi'],
                nominal=data_transaksi['nominal'],
                users=user
            )

            new_transaksi.save()

            serializer = TransaksiSerializer(new_transaksi)

            return Response(serializer.data)
        else:
            return Response({'message': 'data melebehi balance yang ditentukan'}, status=status.HTTP_400_BAD_REQUEST)
