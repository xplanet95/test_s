from django import template
from news.models import Category, News
from django.db.models import Count, F

register = template.Library()


#  возвращает данные
@register.simple_tag(name='get_all_cat')
def get_categories():
    # можно вернуть просто все категории
    # Category.objects.all()
    # а можно вернуть только опубликованные + количество записей которых не равно 0.
    # что лучше, ибо если переходить на категории где нет записей будет 404 или типа того
    # мой вариант фильтра
    # Category.objects.filter(news__is_published=True).annotate(cnt=Count('news')).filter(cnt__gt=0)
    # ниже вариант с классом F
    return Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)


#  рендерит и показывает данные, помимо возвращения
@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    context = {
        'categories': categories,
        # 'arg1': arg1,
        # 'arg2': arg2,
    }
    return context
