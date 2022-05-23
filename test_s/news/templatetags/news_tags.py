from django import template
from news.models import Category

register = template.Library()


#  возвращает данные
@register.simple_tag(name='get_all_cat')
def get_categories():
    return Category.objects.all()


#  рендерит и показывает данные, помимо возвращения
@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
