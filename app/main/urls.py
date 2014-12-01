from django.conf.urls import patterns, url

urlpatterns = patterns('app.main.views',
    url('^$', 'index', name='home'),
    url('^logout/', 'logout_view', name='logout'),
    url('^profile/', 'profile', name='profile'),
)
