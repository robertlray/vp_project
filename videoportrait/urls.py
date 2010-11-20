from django.conf.urls.defaults import *
from django.contrib import admin
from settings import CONFIG_SETTINGS, MEDIA_URL, MEDIA_ROOT
admin.autodiscover()


urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'', include('vp_project.urls')),
    (r'vp_project/', include('vp_project.urls')),
)

#Allow Django to Serve static "media" files during development
if CONFIG_SETTINGS == "local":
    urlpatterns += patterns('django.views.static',
                            (r'^%s(?P<path>.*)$'%MEDIA_URL[1:],'serve',
                             {'document_root': MEDIA_ROOT}))

