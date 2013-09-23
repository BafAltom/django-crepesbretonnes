# Create your views here.
#-*- coding: utf-8 -*-

# from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})


def view_article(request, id):
    """Affiche un article selon son identifiant (id)"""
    article = Article.objects.filter(id=id)
    return render(request, 'blog/read.html', {'article': article})
