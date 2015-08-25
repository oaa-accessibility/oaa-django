from django.contrib import admin

from manualChecks.models import  ManualCheck, ManualCheckNLS

class ManualCheckAdmin(admin.ModelAdmin):
    list_display = ('rule', 'title')
    list_filter  = ('rule',)

admin.site.register(ManualCheck, ManualCheckAdmin)

class ManualCheckNLSAdmin(admin.ModelAdmin):
    list_display = ('title', 'rule', 'language')
    list_filter = ('language',)

admin.site.register(ManualCheckNLS, ManualCheckNLSAdmin)

