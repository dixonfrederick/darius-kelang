from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hello, World!")

def budgetCategory_MainView(request):
    return HttpResponse("Your Budget Categories")