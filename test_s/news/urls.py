from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    path('news/<int:news_id>/', views.view_news, name='read_more_button'),
    path('news/add_news/', views.add_news, name='add_news'),
]
