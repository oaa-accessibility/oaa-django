from django.contrib import admin
from users.models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'title')

admin.site.register(Organization, OrganizationAdmin)

