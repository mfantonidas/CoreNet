from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from django.contrib.auth.views import login,logout
from CoreNet.views import *
from rest_framework import routers
from testapp import views
import xadmin
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
xadmin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^account/login$',login,{'template_name': 'corenet_admin/login.html'}),
    url(r'^account/logout$', "CoreNet.views.corenet_logout"),
    #url(r'^account/login$', "CoreNet.views.login", name='accounts_login'),
    #url(r'^corenet_logout$', "CoreNet.views.logout", name='accounts_logout'),
    url(r'accounts/profile/$', "CoreNet.views.corenet", name='main_page'),
    url(r'corenet/$', "CoreNet.views.corenet", name='main_page'), 
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += patterns('olts.views',
    (r'fttx/$', 'fttxorder'),
	(r'upload/$', 'register'),
)