from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article

def index(request):
    return redirect('home')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def home_page(request):
    # last_added_article = Article.objects.latest('date_added')
    latest_articles = Article.objects.order_by('-date_added')[:3]
    return render(request, 'page.html', {'latest_articles': latest_articles})
