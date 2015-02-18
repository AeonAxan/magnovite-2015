from django.conf.urls import patterns, url

urlpatterns = patterns('app.internal.views',
    url(r'^register/$', 'register_view', name='register'),

    url(r'^accounts/$', 'accounts_view'),

    url(r'^all.csv/$', 'all_csv'),

    url(r'^private/(?P<type>[a-z]+)/$', 'private_view'),
    url(r'^private/(?P<type>[a-z]+)/(?P<slug>[a-z0-9]*)/$', 'private_view'),

    url(r'^api/register/$', 'register_create', name='register:create'),
    url(r'^api/items/$', 'api_items'),
    url(r'^api/bulk/$', 'test'),

    url(r'^(?P<type>[a-z]+)/$', 'table_view'),
    url(r'^(?P<type>[a-z]+)/(?P<slug>[a-z\-]*)/$', 'table_view'),
)
