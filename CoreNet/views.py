from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

def hello(request):    
    return HttpResponse('shit~~')                                                                                                       

def corenet(request):
    return render_to_response('corenet_admin/corenet.html', {},context_instance=RequestContext(request))

def login_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
	    login(request, user)
		return corenet(request)
    else
	    return 
def logout_view(request):
    logout(request)
	return 