from rest_framework import serializers,status
from .models import User, Transaksi
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password','role', 'name')
    
        def create(self,validated_data):
            password = validated_data['password']
            user = User(**validated_data)
            user.set_password(password)
            
            return user


class TransaksiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaksi
        fields = ('id', 'jenisTransaksi', 'nominal',
                  'tanggalTransaksi', 'users_id')
