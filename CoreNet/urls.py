from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from django.contrib.auth.views import login,logout
from CoreNet.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/login$',login),
    url(r'^account/logout$', logout),
    #url(r'^account/login$', "CoreNet.views.login", name='accounts_login'),
    #url(r'^account/logout$', "CoreNet.views.logout", name='accounts_logout'),
    url(r'accounts/profile/$', "CoreNet.views.corenet", name='main_page'),
    url(r'corenet$', "CoreNet.views.corenet", name='main_page'), 
)
