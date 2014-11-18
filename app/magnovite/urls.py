from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'app.main.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^subscribe/', include('app.subscribe.urls')),
)

