from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

    url(r'^$', 'app.main.views.index', name='home'),
    url(r'^profile/', 'app.main.views.profile', name='profile'),

    url(r'^events/', 'app.main.views.events', name='events'),

    url(r'^subscribe/', include('app.subscribe.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # 3rd party
    url(r'^accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

