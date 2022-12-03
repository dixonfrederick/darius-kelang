from django.urls import path

from .views import *

app_name = 'export'

urlpatterns = [
    path('select', export, name='select'),
]

