from django.contrib import admin
from tips.models import contact_info

class contactAdmin(admin.ModelAdmin):
    list_display = ('department', 'tel')
    search_fields = ('department', 'tel')

admin.site.register(contact_info, contactAdmin)
