from django.contrib import admin
from CoreNE.models import *

class OltsAdmin(admin.ModelAdmin):
    list_display = ('name', 'ipaddr', 'netype')
    search_fields = ('name', 'ipaddr', 'netype')
    ordering = ('netype',)

class fttoAdmin(admin.ModelAdmin):
    list_display = ('locate', 'area')
    search_fields = ('locate', 'area')
    ordering = ('locate',)

class fttxAdmin(admin.ModelAdmin):
    list_display = ('area',)
    search_fields = ('area',)
    ordering = ('area',)

class dataprojectAdmin(admin.ModelAdmin):
    list_display = ('area',)
    search_fields = ('area',)
    ordering = ('area',)

class numbersrcAdmin(admin.ModelAdmin):
    list_display = ('area',)
    search_fields = ('area',)
    ordering = ('area',)
	
admin.site.register(Olts, OltsAdmin)
admin.site.register(Ftto, fttoAdmin)
admin.site.register(Fttx, fttxAdmin)
admin.site.register(Dataproject, dataprojectAdmin)
admin.site.register(Numbersrc, numbersrcAdmin)
