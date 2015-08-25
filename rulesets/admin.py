from django.contrib import admin

from rulesets.models import Ruleset, RulesetNLS, RuleMapping

class RulesetAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'version')
    list_filter  = ('author', 'version')

admin.site.register(Ruleset, RulesetAdmin)

class RulesetNLSAdmin(admin.ModelAdmin):
    list_display = ('language', 'ruleset')
    list_filter  = ('language', 'ruleset')

admin.site.register(RulesetNLS, RulesetNLSAdmin)

class RuleMappingAdmin(admin.ModelAdmin):
    list_display = ('ruleset', 'rule', 'required', 'enabled')
    list_filter  = ('ruleset', 'rule', 'required', 'enabled')

admin.site.register(RuleMapping, RuleMappingAdmin)
