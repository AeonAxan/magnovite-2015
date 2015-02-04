from django.conf.urls import patterns, url

urlpatterns = patterns('app.main.views',
    url('^$', 'index', name='home'),
    url('^login/$', 'login', name='login'),
    url('^logout/$', 'logout_view', name='logout'),
    url('^profile/$', 'profile', name='profile'),
    url('^profile/update/(?P<pk>\d+)/$', 'profile_update_view', name='profile_update'),
    url(r'^profile/message/$', 'add_message', name='add_message'),
)
