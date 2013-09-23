# Create your views here.
#-*- coding: utf-8 -*-

# from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})


def view_article(request, ID, slug):
    """Affiche un article selon son identifiant (id)"""
    article = get_object_or_404(Article, ID=ID, slug=slug)
    return render(request, 'blog/read.html', {'article': article})
