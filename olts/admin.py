from django.contrib import admin
from olts.models import *

class OltsAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'upswitch', 'type', 'odf', 'area', 'upbandwidth')
    search_fields = ('name', 'ipaddr')
    ordering = ('ip',)

class fttoAdmin(admin.ModelAdmin):
    list_display = ('name', 'oltip', 'sn', 'obd', 'pvlan', 'cvlan', 'ording', 'description')
    search_fields = ('name', 'sn')
    ordering = ('name',)

class fttxAdmin(admin.ModelAdmin):
    list_display = ('name', 'manage_ip', 'voice_ip', 'oltip')
    search_fields = ('name', 'manage_ip', 'voice_ip', 'oltip',)
    ordering = ('name',)

class dataprojectAdmin(admin.ModelAdmin):
    list_display = ('area', 'olt', 'vlantype', 'voicetype')
    search_fields = ('area',)
    ordering = ('area',)

#class numbersrcAdmin(admin.ModelAdmin):
#    list_display = ('',)
#    search_fields = ('area',)
#    ordering = ('area',)
	
admin.site.register(Olts, OltsAdmin)
admin.site.register(ftto, fttoAdmin)
admin.site.register(fttx, fttxAdmin)
admin.site.register(dataproject, dataprojectAdmin)
#admin.site.register(Numbersrc, numbersrcAdmin)
