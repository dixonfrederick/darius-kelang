from django.shortcuts import render
from django.http import QueryDict
from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listwallet(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute("""SELECT * FROM WALLET;""") #TODO
    result = namedtuplefetchall(cursor)
    return render (request, 'wallet/listwallet.html', {'result': result})

def createwallet(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    if (request.method == 'POST'):
        res = request.POST
        id = res.get('id')
        name = res.get('name') 
        balance = res.get('balance')
        userid = res.get('userid')
        cursor.execute("""INSERT INTO WALLET
        VALUES (%s, %s, %s, %s)""", [id, name, balance,  userid])
    return render (request, 'wallet/createwallet.html')