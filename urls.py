from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'twango.twentries.views.public'),
    url(r'^twentries/', include('twango.twentries.urls')),
    
    #url(r'^accounts/register/$', 'twango.registration.views.register', name='acct_register'),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='auth_login'),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
    #    {'next_page':'/' },
    #    name='auth_logout'),
    url(r'^accounts/', include('registration.urls')),
    url(r'^friends/', include('socialgraph.urls')),
    url(r'^profile/', include('profile.urls')),
    
    
    url(r'^admin/(.*)', admin.site.root),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        
    url(r'^(?P<username>[a-zA-Z0-9_-]+)/$', 'twango.twentries.views.user', 
        name='tw_user'),
)
