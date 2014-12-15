from django.conf.urls import patterns, url

urlpatterns = patterns('app.quest.views',
    url('^$', 'index', name='quest:index'),
)
