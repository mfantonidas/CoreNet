from django.contrib import admin
from CoreNE.models import corenet_ne, softxinfo, IMSinfo

class contactAdmin(admin.ModelAdmin):
    list_display = ('department', 'tel')
    search_fields = ('department', 'tel')
    ordering = ('id',)

admin.site.register(contact_info, contactAdmin)
