from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    # path('', views.index, name='home'),
    # path('', cache_page(60)(views.HomeNews.as_view()), name='home'),
    path('', views.HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', views.get_category, name='category'),
    path('category/<int:category_id>/', views.CategoryNews.as_view(), name='category'),
    # path('news/<int:news_id>/', views.view_news, name='read_more_button'),
    path('news/<int:pk>/', cache_page(60*15)(views.ViewNews.as_view()), name='read_more_button'),
    # path('news/add_news/', views.add_news, name='add_news'),
    path('news/add_news/', views.CreateNews.as_view(), name='add_news'),

    # path('foo/<int:code>/', cache_page(60 * 15)(my_view)),
]
