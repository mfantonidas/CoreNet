from django.conf.urls import *
from CoreNet.views import hello, corenet
from CoreNet.views import login_view, logout_view
import testapp
from testapp import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CoreNet.views.home', name='home'),
    # url(r'^CoreNet/', include('CoreNet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^hello1/', include(testapp.urls)),
    url(r'^corenet/$', "views.corenet",name='main_page'),
	url(r'^accounts/login$', "views.login_view", name='accounts_login'),
	url(r'^accounts/logout$', "views.logout_view", name='accounts_logout'),
)

