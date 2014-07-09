from django.conf.urls import *
from testapp.views import hello1

urlpatterns = patterns('',
    url(r'', hello1),
)
