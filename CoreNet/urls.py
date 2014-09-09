from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from django.contrib.auth.views import login,logout
from CoreNet.views import *
from testapp import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
import xadmin
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
xadmin.autodiscover()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


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
    url(r'^', include(routers.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += patterns('olts.views',
    (r'fttx/$', 'fttxorder'),
	(r'upload/$', 'register'),
)