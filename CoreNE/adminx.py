#from django.contrib import admin
import xadmin
from CoreNE.models import corenet_ne, softxinfo, IMSinfo

#class coreneAdmin(admin.ModelAdmin):
class coreneAdmin(object):
    list_display = ('name', 'ipaddr', 'netype')
    search_fields = ('name', 'ipaddr', 'netype')
    ordering = ('netype',)

#class softxAdmin(admin.ModelAdmin):
class softxAdmin(object):
    list_display = ('locate', 'area')
    search_fields = ('locate', 'area')
    ordering = ('locate',)

#class IMSAdmin(admin.ModelAdmin):
class IMSAdmin(object):
    list_display = ('area',)
    search_fields = ('area',)
    ordering = ('area',)

xadmin.site.register(corenet_ne, coreneAdmin)
xadmin.site.register(softxinfo, softxAdmin)
xadmin.site.register(IMSinfo, IMSAdmin)
