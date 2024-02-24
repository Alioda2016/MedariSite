from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path('home/all', views.article_list, name='article_list'),
    path('home', views.home_page, name='home'),
]
