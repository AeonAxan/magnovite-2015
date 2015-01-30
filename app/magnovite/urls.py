from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

    # apps
    url(r'', include('app.main.urls')),
    url(r'^subscribe/', include('app.subscribe.urls')),
    url(r'^events/', include('app.event.urls')),
    url(r'^quest/', include('app.quest.urls')),
    url(r'^dashboard/', include('app.dashboard.urls')),
    url(r'^payment/', include('app.payment.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # 3rd party
    url(r'^accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

