from django.urls import path

from .views import *

app_name = 'wallet'

urlpatterns = [
    path('listwallet', listwallet, name='listwallet'),
    path('createwallet', createwallet, name='createwallet')
]

