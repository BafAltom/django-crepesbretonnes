# Create your views here.
#-*- coding: utf-8 -*-

# from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.forms import ContactForm
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})


def view_article(request, ID):
    article = get_object_or_404(Article, id=ID)
    return render(request, 'blog/read.html', {'article': article})


def contact(request):
    messageSent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            sendCopy = form.cleaned_data['sendCopy']

            # Envoi du mail...
            messageSent = True
            form = ContactForm()

    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form, 'messageSent': messageSent})
