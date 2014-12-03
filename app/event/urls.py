from django.conf.urls import patterns, url

urlpatterns = patterns('app.event.views',
    url('^$', 'index', name='events'),
    url('^(?P<slug>\w+)/', 'details', name='event_details')
)
