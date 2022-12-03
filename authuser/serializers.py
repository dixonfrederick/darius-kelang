from rest_framework import serializers
from .models import User, Transaksi


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'role', 'name')


class TransaksiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaksi
        fields = ('id', 'jenisTransaksi', 'nominal',
                  'tanggalTransaksi', 'users_id')
