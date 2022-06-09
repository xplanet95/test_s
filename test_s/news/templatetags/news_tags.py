from django import template
from news.models import Category, News
from django.db.models import Count, F
from django.core.cache import cache

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
    categories = Category.objects.annotate(
        cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    # или еще можно проверкк на наличие в кэшэ, если нету, то только тогда делать запрос и кэшировать
    # categories = cache.get('categories')
    # if not categories:
    #     categories = Category.objects.annotate(
    #         cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    #     # кэширование, присвоенное имя в кавычка, данные для кэшировани второй параметр, время 3й
    #     cache.set('categories', categories, 100)
    # или можно get or set
    #   cache.get_or_set('categories', Category.objects.annotate(
    #             cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0), 100)
    return categories


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
