from django.conf.urls import patterns, url

urlpatterns = patterns('app.event.views',
    url('^$', 'index', name='events'),
    url('^api/register/(?P<id>\d+)/', 'register', name='register'),
    url('^api/unregister/(?P<id>\d+)/', 'unregister', name='unregister'),

    url('^(?P<slug>\w+)/', 'details', name='event_details')
)
