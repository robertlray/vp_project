from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('vp_project.views',
    (r'^$', 'index'),
    (r'^(?P<category_id>\d+)/$', 'category'),
    (r'^video/(?P<video_id>\d+)/$', 'video'),
 url(r'^about', 'about'),
    # Example:
    # (r'^videoportrait/', include('videoportrait.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
