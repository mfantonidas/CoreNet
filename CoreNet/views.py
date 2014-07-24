from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def hello(request):    
    return HttpResponse('shit~~')                                                                                                       

def corenet(request):
    return render_to_response('corenet_admin/corenet.html', {},context_instance=RequestContext(request))

def main(request):