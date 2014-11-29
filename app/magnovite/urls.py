from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

    url(r'^$', 'app.main.views.index', name='home'),
    url(r'^events/', 'app.main.views.events', name='events'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^subscribe/', include('app.subscribe.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

