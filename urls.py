from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
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
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/(.*)', admin.site.root),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
