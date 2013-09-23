# Create your views here.
#-*- coding: utf-8 -*-
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    text = """<h1>Bienvenue sur mon blog !</h1>
          <p>Ton papa a fait l'amour avec ta maman au moins une fois</p>
        """
    return HttpResponse(text)


def view_article(request, id):
    """Affiche un article selon son identifiant (id)"""
    text = "Vous avez demandé l'article n°{0} !".format(id)
    return HttpResponse(text)


def tpl(request):
    return render(request, 'blog/tp1.html', {'current_date': datetime.now()})
