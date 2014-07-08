# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

def hello1(request):
    return HttpResponse('oh shit~~')   
