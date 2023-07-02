from django.contrib import admin
from . import models


class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain_url', 'ping_ret', 'created_time', 'modified_time')


admin.site.register(models.Domain, DomainAdmin)
