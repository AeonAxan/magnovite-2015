from django.conf.urls import patterns, url

urlpatterns = patterns('app.dashboard.views',
    url(r'^$', 'index', name='dashboard'),
    url(r'^capture/', 'capture', name='dashboard:capture'),
    url(r'^data/', 'data', name='dashboard:data'),
)
