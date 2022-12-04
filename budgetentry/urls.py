from django.urls import path

from .views import *

urlpatterns = [
    path("home/", homePageView, name="home"),
    path('dashboard', viewDashboard, name="dashboard"),  # Needs UID
    path('entries/', viewEntries, name="list"),  # Needs UID + TypeID
    path('entries/detail/', viewEntryDetail, name="detail"),
    path('entries/create/', createEntry, name="create"),
    path('entries/edit/', editEntry, name="edit")
]
