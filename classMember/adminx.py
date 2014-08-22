from django.template import loader

from xadmin.sites import site
from xadmin.views import BaseAdminPlugin, ListAdminView
import xadmin
from tips.models import contact_info

class TestAdminPlugin(BaseAdminPlugin):
    def get_context(self,context):
	    context['test'] = True
		return context
		
#class upload_duty(BaseAdminPlugin):
#    say_hello = False

# Register your models here.
#xadmin.site.register(, )
site.register_plugin(TestAdminPlugin, ListAdminView)