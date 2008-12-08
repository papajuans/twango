from django.conf.urls.defaults import *

urlpatterns = patterns('twango.twentries.views',
    url(r'^$', 'public', name='public_timeline'),
    url(r'^create/$', 'create', name='create_twentry'),
)
