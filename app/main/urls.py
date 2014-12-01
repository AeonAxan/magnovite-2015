from django.conf.urls import patterns, url

urlpatterns = patterns('app.main.views',
    url('^$', 'index', name='home'),
    url('^logout/', 'logout', name='logout'),
    url('^profile/', 'profile', name='profile'),
)
