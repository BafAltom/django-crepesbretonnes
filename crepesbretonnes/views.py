# Create your views here.
#-*- coding: utf-8 -*-
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'base.html', {})


def view_article(request, id):
    """Affiche un article selon son identifiant (id)"""
    text = "Vous avez demandé l'article n°{0} !".format(id)
    return HttpResponse(text)


def tpl(request):
    return render(request, 'blog/tpl.html', {'current_date': datetime.now()})
