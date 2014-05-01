from django.contrib import admin
from loaderio.models import Validation


class ValidationAdmin(admin.ModelAdmin):
    fields = ['token', 'enabled']
    list_display = ['token', 'enabled']
    list_editable = ['enabled']

admin.site.register(Validation, ValidationAdmin)
