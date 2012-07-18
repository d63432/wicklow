from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': 'http://resources.dublinsix.net/favicon.ico'}),
                       url(r'^$', 'wicklow.views.home'),
                       url(r'^library-services/$', 'wicklow.views.library_services'),
                       url(r'^publisher-services/$', 'wicklow.views.publisher_services'),
                       url(r'^products/$', 'wicklow.views.products'),
                       url(r'^about/$', 'wicklow.views.about'),
                       url(r'^terms-of-service/$', 'wicklow.views.terms_of_service'),
                       url(r'^privacy-policy/$', 'wicklow.views.privacy_policy'),
                       url(r'time/$', 'wicklow.views.current_datetime'),
                       url(r'^time/plus/(\d{1,2})/$', 'wicklow.views.hours_ahead'),
    # Examples:
    # url(r'^$', 'wicklow.views.home', name='home'),
    # url(r'^wicklow/', include('wicklow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
