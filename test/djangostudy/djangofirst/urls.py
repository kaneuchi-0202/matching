from django.urls import path
from . import views

app_name = 'djangofirst'

urlpatterns =[
    path('', views.index, name='index'),
]