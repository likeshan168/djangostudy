from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from mysite.views import hello, current_datetime, my_homepage_view, hours_ahead,mypage

urlpatterns = patterns('',
	url(r'^$', my_homepage_view),
	url(r'^hello/$', hello),	
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^mypage/$', mypage),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
