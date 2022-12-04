from django.urls import path

from .views import *

urlpatterns = [
    path("home/", homePageView, name="home"),
    path('', viewDashboard, name="dashboard"),  # Needs UID
    path('entries/', viewEntries, name="list"),  # Needs UID + TypeID
    path('entries/entry?id=1', viewEntryDetail, name="detail"),  # Needs UID + TypeID + EntryID
    path('entries/entry?id=1/edit', editEntry, name="edit"),  # Needs UID + TypeID + EntryID
    path('entries/entry?id=1/delete', deleteEntry, name="delete"),  # Needs UID + TypeID + EntryID
    path('entries/create/', createEntry, name="create"),
    path('entries/edit/', editEntry, name="edit")
]
