# Create your views here.

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.conf import settings
from django.contrib import auth
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django import forms
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST
from tips.models import contact_info
from olts.models import *
from CoreNE.models import *

class DateForm(forms.Form):
    date = forms.CharField()
    xlsfile = forms.FileField()

def register(request):
    if request.method == "POST":
        uf = DateForm(request.POST,request.FILES)
        if uf.is_valid():
            date = uf.cleaned_data['date']
            xlsfile = uf.cleaned_data['xlsfile']
            duty = duty()
            duty.date = date
            duty.xlsfile = xlsfile
            duty.save()
            return HttpResponse('upload ok!')
    else:
        uf = DateForm()
    return render_to_response('corenet_admin/fttx.html',{'uf':uf},context_instance=RequestContext(request))
	
@csrf_protect
@login_required(login_url='/account/login')

def fttxorder(request):
    if request.user.is_authenticated():
        user = request.user
        uf = DateForm()
	return render_to_response('corenet_admin/fttx.html', {'user':user, 'uf':uf},context_instance=RequestContext(request))
    else:
	return login(request)
 
def corenet_logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('main_page'))

