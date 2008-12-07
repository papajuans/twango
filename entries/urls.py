from django.conf.urls.defaults import *

urlpatterns = patterns('twango.entries.views',
    (r'^$', 'public'),
)
