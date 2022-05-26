from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    extra_context = {'title': 'Новости моего сайта'}

    # вместо экстра конетент, для динамических
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Новости моего сайта'
    #     return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class CategoryNews(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'add_news.html'
    # success_url = reverse_lazy('home')



# def index(request):
#     title = 'Новости моего сайта'
#     news = News.objects.all()[:11]
#     # categories = Category.objects.all()
#     context = {
#         'news': news,
#         'title': title,
#         # 'categories': categories,
#     }
#     response = render(request, 'news/index.html', context)
#     return response


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     # categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         # 'categories': categories,
#         'category': category,
#     }
#     response = render(request, 'news/category.html', context)
#     return response


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'news_item': news_item,
#     }
#     response = render(request, 'news/view_news.html', context)
#     return response


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            #  для не связанной формы
            # users_news = News.objects.create(**form.cleaned_data)
            users_news = form.save()
            return redirect(users_news)
    else:
        #  экземпляр класса
        form = NewsForm()
    context = {
        'form': form,
    }
    response = render(request, 'news/add_news.html', context)
    return response
