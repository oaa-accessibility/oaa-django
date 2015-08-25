from django.contrib import admin

from techniques.models import  Technique, TechniqueNLS

class TechniqueAdmin(admin.ModelAdmin):
    list_display = ('technique_id', 'rule', 'type', 'title')
    list_filter  = ('rule', 'type')
    exclude = ('url', 'notes', 'notes_html', 'abbrev_html', 'title_html')

admin.site.register(Technique, TechniqueAdmin)

class TechniqueNLSAdmin(admin.ModelAdmin):
    list_display = ('technique', 'title', 'rule', 'language')
    list_filter = ('language',)

admin.site.register(TechniqueNLS, TechniqueNLSAdmin)

