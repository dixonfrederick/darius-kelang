from rest_framework import viewsets, status
from .models import User, Transaksi
from .serializers import UserSerializer, TransaksiSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    # /api/v1/user [GET,POST]
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
