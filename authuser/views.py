import requests
import json
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Transaksi
from .serializers import UserSerializer, TransaksiSerializer
from wallet.views import namedtuplefetchall


# get Wallet balance
ACCESS_TOKEN_GLOBAL = None


def transaksi_add(request: Request):
    if request.method == 'GET':
        return render(request, "authuser/tambahTransaksi.html")
    elif request.method == 'POST':
        headers = {
            "Authorization": "Bearer " + ACCESS_TOKEN_GLOBAL
        }
        jenisTransaksi = request.POST.get('transaksi')
        nominal = request.POST.get('nominal')
        nominal = int(nominal)
        payload = {
            'jenisTransaksi': jenisTransaksi,
            'nominal': nominal
        }
        url = "https://darius-kelang-production.up.railway.app/api/v1/transaksi"
        response = requests.post(url=url, data=payload, headers=headers)
        print(response.content)
        return redirect("/transaksi/")


def transaksi_list(request):
    url = "https://darius-kelang-production.up.railway.app/api/v1/transaksi/"
    headers = {
        "Authorization": "Bearer " + ACCESS_TOKEN_GLOBAL
    }
    response = requests.get(url=url, headers=headers)
    json_response = json.loads(response.content)
    print(json_response)
    return render(request, "authuser/listTransaksi.html", {'Transaksi': json_response})


class LogoutView(APIView):
    permission_classes = []

    def get(self, request: Request):
        logout(request)
        return redirect("/")


class LoginView(APIView):
    permission_classes = []

    def get(self, request: Request):
        return render(request, 'authuser/login.html')

    def post(self, request: Request):
        global ACCESS_TOKEN_GLOBAL
        username = request.POST.get('username')
        password = request.POST.get('password')

        payload = {
            'username': username,
            'password': password
        }
        url = "https://darius-kelang-production.up.railway.app/auth/login/"

        response = requests.post(url=url, data=payload)
        json_response = json.loads(response.content)
        ACCESS_TOKEN_GLOBAL = json_response['access']
        print(ACCESS_TOKEN_GLOBAL)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            message = {
                'message': 'Login Sukses',
                'username': request.user.username,
                'access': json_response['access']
            }
            return redirect('/')
        else:
            message = {
                'message': "Username atau password invalid"
            }
            return render(request, "authuser/login.html", context=message)


def getBalance(username: str):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute(
        """SELECT balance FROM wallet WHERE userid=(SELECT username FROM authuser_user WHERE username='{0}');""".format(username))
    result = namedtuplefetchall(cursor)
    return result[0].balance

# update balance untuk transaksi


def updateBalance(username: str, amount: int):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute(
        """UPDATE wallet SET balance={0} WHERE userid='{1}';""".format(amount, username))

# init balance saat buat user baru


def getLastId():
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute("""SELECT MAX(id) FROM wallet;""")
    id = namedtuplefetchall(cursor)
    print(id)
    return id[0].max


def initWallet(username):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute(
        """INSERT INTO wallet VALUES ({0},'{1}',0,'{1}');""".format(
            getLastId()+1, username)
    )


class UserViewSet(viewsets.ModelViewSet):
    # /api/v1/user [GET,POST]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        if ('password' in self.request.data):
            initWallet(self.request.data['username'])
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
        print(self.request.user)
        return Transaksi.objects.filter(users=user.id)

    # /api/v1/transaksi [POST] (POST transaksi sesuai user yang login)
    def create(self, request, *args, **kwargs):
        user = self.request.user
        data_transaksi = request.data
        nominal = int(data_transaksi['nominal'])
        jenisTransaksi = data_transaksi['jenisTransaksi']
        username = user.get_username()
        user_balance = getBalance(username)

        # asumsi 5jt adalah balance wallet nanti
        if (nominal <= user_balance):
            new_balance = user_balance - nominal
            updateBalance(username, new_balance)
            new_transaksi = Transaksi.objects.create(
                jenisTransaksi=jenisTransaksi,
                nominal=nominal,
                users=user
            )

            new_transaksi.save()

            serializer = TransaksiSerializer(new_transaksi)

            return Response(serializer.data)
        else:
            return Response({'message': 'data melebehi balance yang ditentukan', 'username': "{0}".format(user.get_username())}, status=status.HTTP_400_BAD_REQUEST)
