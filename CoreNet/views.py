from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

def hello(request):    
    return HttpResponse('shit~~')                                                                                                       

def corenet(request):
    return render_to_response('corenet_admin/corenet.html', )