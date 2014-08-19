#from django.contrib import admin
import xadmin
from olts.models import *

#class OltsAdmin(admin.ModelAdmin):
class OltsAdmin(object):
    list_display = ('name', 'ip', 'upswitch', 'type', 'odf', 'area', 'upbandwidth')
    search_fields = ('name', 'ipaddr')
    ordering = ('ip',)

#class fttoAdmin(admin.ModelAdmin):
class fttoAdmin(object):
    list_display = ('name', 'oltip', 'sn', 'obd', 'pvlan', 'cvlan', 'ording', 'description')
    search_fields = ('name', 'sn')
    ordering = ('name',)

#class fttxAdmin(admin.ModelAdmin):
class fttxAdmin(object):
    list_display = ('name', 'manage_ip', 'voice_ip', 'oltip')
    search_fields = ('name', 'manage_ip', 'voice_ip', 'oltip',)
    ordering = ('name',)

#class dataprojectAdmin(admin.ModelAdmin):
class dataprojectAdmin(object):
    list_display = ('area', 'olt', 'vlantype', 'voicetype')
    search_fields = ('area',)
    ordering = ('area',)

#class numbersrcAdmin(admin.ModelAdmin):
#    list_display = ('',)
#    search_fields = ('area',)
#    ordering = ('area',)
	
xadmin.site.register(Olts, OltsAdmin)
xadmin.site.register(ftto, fttoAdmin)
xadmin.site.register(fttx, fttxAdmin)
xadmin.site.register(dataproject, dataprojectAdmin)
#admin.site.register(Numbersrc, numbersrcAdmin)
