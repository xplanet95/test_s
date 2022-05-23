from django.shortcuts import render
from .models import News, Category


def index(request):
    title = 'Новости моего сайта'
    news = News.objects.all()[:11]
    # categories = Category.objects.all()
    context = {
        'news': news,
        'title': title,
        # 'categories': categories,
    }
    response = render(request, 'news/index.html', context)
    return response


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    # categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        # 'categories': categories,
        'category': category,
    }
    response = render(request, 'news/category.html', context)
    return response
