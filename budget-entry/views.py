from django.shortcuts import render, redirect
from django.http import HttpResponse


def homePageView(request):
    return render(request, "/home")


def viewDashboard(request):
    return render(request, "")


def viewEntries(request):
    return render(request, "")


def viewEntryDetail(request):
    return render(request, "")


def editEntry(request):
    return render(request, "")


# def editEntry(request): # Post
#     return render(request, "")


def deleteEntry(request):
    return render(request, "")


# def deleteEntry(request): # Post
#     return render(request, "")
