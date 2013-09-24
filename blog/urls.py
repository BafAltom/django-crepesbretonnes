#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'home'),
    url(r'^read/(?P<ID>\d+)/?$', 'view_article'),
)
