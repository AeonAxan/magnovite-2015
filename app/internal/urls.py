from django.conf.urls import patterns, url

urlpatterns = patterns('app.internal.views',
    url(r'^register/$', 'register_view', name='register'),

    url(r'^private/(?P<type>[a-z]+)/(?P<slug>[a-z0-9]+)/$', 'private_view'),

    url(r'^api/register/$', 'register_create', name='register:create'),
    url(r'^api/items/$', 'api_items'),
)
