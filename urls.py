from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^example1/', 'testapp.views.example1'),
    (r'^example2/', 'testapp.views.example2'),
    (r'^example3/', 'testapp.views.example3'),
    (r'^example4/', 'testapp.views.example4'),
    (r'^example5/', 'testapp.views.example5'),
    (r'^example6/', 'testapp.views.example6'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
