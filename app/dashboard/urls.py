from django.conf.urls import patterns, url

urlpatterns = patterns('app.dashboard.views',
    url('^$', 'index', name='dashboard'),
)
