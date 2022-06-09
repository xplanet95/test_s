from django.urls import path
from . import views

urlpatterns = [
    path('news/test/', views.test_mail, name='test'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    # path('', views.index, name='home'),
    path('', views.HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', views.get_category, name='category'),
    path('category/<int:category_id>/', views.CategoryNews.as_view(), name='category'),
    # path('news/<int:news_id>/', views.view_news, name='read_more_button'),
    path('news/<int:pk>/', views.ViewNews.as_view(), name='read_more_button'),
    # path('news/add_news/', views.add_news, name='add_news'),
    path('news/add_news/', views.CreateNews.as_view(), name='add_news'),
]
