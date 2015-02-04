from django.conf.urls import patterns, url

urlpatterns = patterns('app.workshop.views',
    url(r'^$', 'index', name='workshop_index'),
)
