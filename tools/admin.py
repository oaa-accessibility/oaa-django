from django.contrib import admin
from tools.models import Tool

class ToolAdmin(admin.ModelAdmin):
    list_display = ('tool_slug', 'title')

admin.site.register(Tool, ToolAdmin)

