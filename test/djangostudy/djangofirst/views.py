from django.shortcuts import render
from .quiz import *

# Create your views here.
def index(request):
    context = {
        'title': 'はじめての Django Web アプリケーション',
    }
    return render(request, 'djangofirst/index.html', context)

def pref_quiz(request):
    prefecture, city, url = prefecture_quiz()
    context = {
        'title': '県庁所在地クイズ',
        'prefecture': prefecture,
        'city': city,
        'url': url,
    }
    return render(request, 'djangofirst/prefecture_tpl.html', context)

def pref_result(request):
    if request.method == 'POST':
        userinput_city = request.POST['userinput_city']
        prefecture = request.POST['prefecture']
        city = request.POST['city']
        url = request.POST['url']
        
        if city == userinput_city:
            result = '正解'
        else :
            result = '不正解'
        
        context = {
            'title': '県庁所在地クイズ - 結果',
            'result': result,
            'prefecture': prefecture,
            'city': city,
            'url': url,
        }
        return render(request, 'djangofirst/prefecture_result.html', context)