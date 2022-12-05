from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


def login(request):
    return render(request, "main/login.html")


@api_view(['GET'])
#@permission_classes((IsAuthenticated, ))
def homePageView(request):
    return render (request, 'main/main.html')