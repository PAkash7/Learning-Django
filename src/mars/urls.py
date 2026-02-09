from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='MARS HOME'),
    path('news/', views.news, name='MARS NEWS'),
    path('news/latest', views.new_release, name='new-release'),
    path('news/monthly', views.monthly_news, name='monthly-news'),
    path('news/yearly', views.yearly_news, name='yearly-news'),
    path('about/', views.about, name='ABOUT MARS')
]