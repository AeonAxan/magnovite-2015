from django.conf.urls import patterns, url

urlpatterns = patterns('app.subscribe.views',
    url('^$', 'subscribe', name='subscribe')
)
