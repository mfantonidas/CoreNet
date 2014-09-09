# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from rest_framework import routers
from rest_framework import viewsets
from testapp.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User,Group

def hello1(request):
    return HttpResponse('oh shit~~')   

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
	
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
