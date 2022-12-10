from django.urls import path

from .views import *

urlpatterns = [
    path("home/", homePageView, name="home"),
    path('dashboard', viewDashboard, name="dashboard"),  # Needs UID
    path('entries/<int:type_ID>/', viewEntries, name="list"),  # Needs UID + TypeID
    path('entries/<int:type_ID>/<int:entryID>/detail/', viewEntryDetail, name="detail"),
    path('entries/<int:type_ID>/create/', createEntry, name="create"),
    path('entries/<int:type_ID>/<int:entryID>/edit/', editEntry, name="edit")
]
