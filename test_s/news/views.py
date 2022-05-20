from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    title = 'Новости моего сайта'
    news = News.objects.all()[:11]
    context = {
        'news': news,
        'title': title,
    }
    response = render(request, 'news/index.html', context)
    return response

def test(request):
    return HttpResponse('<h1>OMG</h1>')