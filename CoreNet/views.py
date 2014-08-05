#coding=utf-8

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

@csrf_protect
@login_required(login_url='/account/login')

def corenet(request):
    if request.user.is_authenticated():
        user = request.user
	contact = contact_info()
	return render_to_response('corenet_admin/corenet.html', {'user':user, 'contact':contact_info},context_instance=RequestContext(request))
    else:
	return login(request)

#def validate_login(request, username, password):
#    return_value = False
#    user = authenticate(username=username,password=password)
#    if user:
#        if user.is_active:
#            auth_login(request,user)
#            return_value = True
#        else:
#            messages.add_message(request, messages.INFO, '账号未激活')
#    else:
#        messages.add_message(request, messages.INFO, '账号或密码错误')#
#
#    return return_value
	
#def login(request):
#    template_var = {}
#    form = LoginForm()
#    if request.method == "POST":
#        form = LoginForm(request.POST.copy())
#        if form.is_valid():
#            if validate_login(request, form.cleaned_data["username"], form.cleaned_data["password"]):
#                return HttpResponseRedirect(reverse('main_page'))
#    template_var["form"] = form
#    return render_to_response('corenet_admin/login.html', template_var, context_instance=RequestContext(request));
    
def corenet_logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('main_page'))

#class LoginForm(forms.Form):
#    username = forms.CharField(label=_(u"Login Account"), widget=forms.TextInput(attrs={'placehoder':'Username', 'id':'username', 'name':'username', 'value':'Your Account'}))
#    password = forms.CharField(label=_(u"Password"), widget=forms.PasswordInput(attrs={'placeholder':'Password','id':'password', 'name':'password', 'value':'password'}))
