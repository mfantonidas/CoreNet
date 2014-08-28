#from django.contrib import admin
import xadmin
from xadmin import views
from tips.models import contact_info

class GlobalSetting(object):
    site_title = 'CoreNet'
	site_footer = 'CoreNet'
#class contactAdmin(admin.ModelAdmin):
class contactAdmin(object):
    list_display = ('department', 'tel', 'duty')
    search_fields = ('department', 'tel', 'duty')
    ordering = ('id',)

xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(contact_info, contactAdmin)
