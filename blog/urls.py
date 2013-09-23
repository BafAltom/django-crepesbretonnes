from django.conf.urls import patterns, url

urlpatterns = patterns(
    'blog.views',
    url(r'^$', 'home'),
    url(r'^article/(?P<id>\d+)/?$', 'view_article'),
    url(r'^date$', 'tpl'),
)
