from django.urls import path
from . import views

app_name = 'djangofirst'

urlpatterns =[
    path('', views.index, name='index'),
    path('pref_quiz', views.pref_quiz, name='pref_quiz'),
    path('pref_reult', views.pref_result, name='pref_result'),
]