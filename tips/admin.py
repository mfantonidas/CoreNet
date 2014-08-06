from django.contrib import admin
from tips.models import contact_info

class contactAdmin(admin.ModelAdmin):
    list_display = ('department', 'tel', 'duty')
    search_fields = ('department', 'tel', 'duty')
    ordering = ('id',)

admin.site.register(contact_info, contactAdmin)
