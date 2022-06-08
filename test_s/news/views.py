from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .utils import MyMixin
# миксин, что бы закрыть доступ к ссылке для не авторизованных
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


def test_mail()


# форма регистрации
def register(request):
    if request.method == 'POST':
        # без отдельного приложения user
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сообщения об успехе
            messages.success(request, 'Вы успешно зарегестрировались')
            # сразу авторизуем если все хоршо
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Что-то пошло не так')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'news/register.html', context)


def user_login(request):
    if request.method == 'POST':
        # надо присвоить данные переменной data
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # метод получения пользователя
            user = form.get_user()
            # авторизация
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm
    context = {
        'form': form,
    }
    return render(request, 'news/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


class HomeNews(ListView):
    paginate_by = 2
    model = News
    extra_context = {'title': 'Новости моего сайта'}
    # можно задать queryset, вместо того, что бы дописавать .select_related('category') в return
    # queryset = News.objects.select_related('category')

    # вместо экстра конетент, для динамических
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Новости моего сайта'
    #     return context

    def get_queryset(self):
        #  оптимизация, подгрузка джоином сарзу всех категорий, что бы не дублировать запросы
        #  .select_related('category')
        return News.objects.filter(is_published=True).select_related('category')


class CategoryNews(ListView):
    paginate_by = 2
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
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

@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST) #  Получем данные из формы из объекта request
        if form.is_valid(): # проверка, прошла ли форма валидацию
            # если форма прошла валидацию то данные попадают в словарь form.cleaned_data

            # эти "чистые данные" надо сохранить, можно отдельно прописывать каждое поле:
            # title = form.cleaned_data['name']
            # ...

            # или можно сделать автоматическую распаковку словаря
            # News.objects.create(**form.cleaned_data)
            # метод create возвращает объект созданной записи => его можно сохранить в переменную
            # для метода create не надо form.save, делается автоматом
            # users_news = News.objects.create(**form.cleaned_data), что бы редирект на саму запись
            # либо надо очистить форму, либо редирект пользователя на другую страницу

            # для форм связанных с моделью нужно только form.save() сделать
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
