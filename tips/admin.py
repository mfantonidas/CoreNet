#from django.contrib import admin
import xadmin
from tips.models import contact_info

#class contactAdmin(admin.ModelAdmin):
class contactAdmin(object):
    list_display = ('department', 'tel', 'duty')
    search_fields = ('department', 'tel', 'duty')
    ordering = ('id',)

xadmin.site.register(contact_info, contactAdmin)
