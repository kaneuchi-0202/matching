from django.urls import path
from . import views

app_name = 'matching_web'

urlpatterns = [
    path('', views.index, name='index'),
]