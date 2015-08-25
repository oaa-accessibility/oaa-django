from django.contrib import admin

from ruleCategories.models import  RuleCategory, RuleCategoryNLS

class RuleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

admin.site.register(RuleCategory, RuleCategoryAdmin)

class RuleCategoryNLSAdmin(admin.ModelAdmin):
    list_display = ('title', 'rule_category', 'language')
    list_filter = ('language',)

admin.site.register(RuleCategoryNLS, RuleCategoryNLSAdmin)

