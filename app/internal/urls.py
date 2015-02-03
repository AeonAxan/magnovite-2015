from django.conf.urls import patterns, url

urlpatterns = patterns('app.internal.views',
    url(r'^register/$', 'register_view', name='register'),
    url(r'^register/create/$', 'register_create', name='register:create'),
)
