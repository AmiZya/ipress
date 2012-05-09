from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('news.views',
    url(r'^$', 'articles', name='article'),
    url(r'^$/(\d+)/$', 'articles', name='articles'),
)