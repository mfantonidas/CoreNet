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
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST

def hello(request):    
    return HttpResponse('shit~~')                                                                                                       

def corenet(request):
    if request.user.is_authenticated():
	    user = request.user
	else:
	    user = request.user
    return render_to_response('corenet_admin/corenet.html', {'user':user},context_instance=RequestContext(request))

def validate_login(request, username, password):
    return_value = False
    user = authenticate(username=username,password=password)
    if user:
        if user.is_active:
            auth_login(request,user)
            return_value = True
        else:
            messages.add_message(request, messages.INFO, _(u'此账户尚未激活，请联系管理员'))
    else:
        messages.add_message(request, messages.INFO, _(u'此账户不存在，请联管理员'))
 
    return return_value
	
def login_view(request):
    template_var = {}
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST.copy())
        if form.is_valid():
            validate_login(request, form.cleaned_data["username"], form.cleaned_data["password"])
            return HttpResponseRedirect(reverse('main_page'))
    template_var["form"] = form
    return render_to_response('corenet_admin/login.html', template_var, context_instance=RequestContext(request));
    
def logout_view(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('main_page'))
	
class LoginForm(forms.Form):
    username=forms.CharField(label=_(u"登录账号"), widget=forms.TextInput(attrs={'placeholder':'登录账号','class':'input-block-level'}))
    password=forms.CharField(label=_(u"登录密码"), widget=forms.PasswordInput(attrs={'placeholder':'登录密码','class':'input-block-level'}))