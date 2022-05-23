from django.shortcuts import render, get_object_or_404
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


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item,
    }
    response = render(request, 'news/view_news.html', context)
    return response
