from django.contrib import admin
from CoreNE.models import corenet_ne, softxinfo, IMSinfo

class coreneAdmin(admin.ModelAdmin):
    list_display = ('name', 'ipaddr', 'netype')
    search_fields = ('name', 'ipaddr', 'netype')
    ordering = ('netype',)

class softxAdmin(admin.ModelAdmin):
    list_display = ('locate', 'area')
    search_fields = ('locate', 'area')
    ordering = ('locate',)

class IMSAdmin(admin.ModelAdmin):
    list_display = ('area',)
    search_fields = ('area',)
    ordering = ('area',)

admin.site.register(corenet_ne, coreneAdmin)
admin.site.register(softxinfo, softxAdmin)
admin.site.register(IMSinfo, IMSAdmin)
