from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

def hello(request):    
    return HttpResponse('shit~~')                                                                                                       

