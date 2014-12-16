from django.conf.urls import patterns, url

urlpatterns = patterns('app.quest.views',
    url(r'^$', 'index', name='quest:index'),
    url(r'guess/$', 'guess', name='quest:guess'),
)
