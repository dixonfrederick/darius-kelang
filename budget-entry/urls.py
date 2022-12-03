from django.urls import path

from .views import *

urlpatterns = [
    path("home/", homePageView, name="home"),
    path('/', viewDashboard, name="dashboard"),
    path('/entries/', viewEntries, name="list"),
    path('/entries/entry?id=1', viewEntryDetail, name="detail"),
    path('/entries/entry?id=1/edit', editEntry, name="edit"),
    path('/entries/entry?id=1/delete', deleteEntry, name="delete")
]
