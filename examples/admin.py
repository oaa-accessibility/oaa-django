from django.contrib import admin

from examples.models import  ExampleStyleReference, ExampleScriptReference
from examples.models import  ExampleStyle, ExampleImage, ExampleObject, ExampleScript
from examples.models import  Example
from examples.models import  ExampleUserAgent, ExampleCompatibility
from examples.models import  ExampleRuleReference
from examples.models import  ExampleGroup

class ExampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter  = ('status',)
    exclude = ('title_html', 'title_text', 'description_html', 'keyboard_html', 'style_code', 'style_source', 'html_code', 'html_source', 'script_code', 'script_source')

admin.site.register(Example, ExampleAdmin)

class ExampleCompatibilityAdmin(admin.ModelAdmin):
    list_display = ('user_agent', 'example', 'result')
    list_filter = ('user_agent', 'example', 'result')

admin.site.register(ExampleCompatibility, ExampleCompatibilityAdmin)

class ExampleUserAgentAdmin(admin.ModelAdmin):
    list_display = ('at', 'browser', 'os', 'show')
    list_filter = ('at', 'browser', 'os', 'show')

admin.site.register(ExampleUserAgent,ExampleUserAgentAdmin)

class ExampleStyleAdmin(admin.ModelAdmin):
    list_display = ('style_id', 'style')

admin.site.register(ExampleStyle,ExampleStyleAdmin)

class ExampleScriptAdmin(admin.ModelAdmin):
    list_display = ('script_id', 'script')

admin.site.register(ExampleScript, ExampleScriptAdmin)

class ExampleObjectAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'object')

admin.site.register(ExampleObject, ExampleObjectAdmin)

class ExampleImageAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'image')

admin.site.register(ExampleImage, ExampleImageAdmin)


class ExampleStyleReferenceAdmin(admin.ModelAdmin):
    list_display = ('example', 'style')

admin.site.register(ExampleStyleReference,ExampleStyleReferenceAdmin)

class ExampleScriptReferenceAdmin(admin.ModelAdmin):
    list_display = ('example', 'script')

admin.site.register(ExampleScriptReference, ExampleScriptReferenceAdmin)

class ExampleRuleReferenceAdmin(admin.ModelAdmin):
    list_display = ('example', 'rule', 'validation', 'manual_check')

admin.site.register(ExampleRuleReference, ExampleRuleReferenceAdmin)

class ExampleGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', )

admin.site.register(ExampleGroup, ExampleGroupAdmin)


