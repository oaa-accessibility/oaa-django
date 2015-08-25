from django.contrib import admin
from rules.models import Rule
from rules.models import RuleNLS 
from rules.models import InformationalLink 
from rules.models import NodeResultMessage

class RuleAdmin(admin.ModelAdmin):
    list_display = ('rule_id', 'summary', 'wcag_primary', 'rule_category', 'scope')
    list_filter = ('wcag_primary', 'rule_category', 'scope')
    exclude = ('purpose_1_html', 'purpose_2_html', 'purpose_3_html', 'purpose_4_html', 'definition_html', 'summary_html', 'target_resource_desc_html')
    
admin.site.register(Rule, RuleAdmin)

class NodeResultMessageAdmin(admin.ModelAdmin):
    list_display = ('rule', 'label', 'message')
    list_filter = ('rule', )
    
admin.site.register(NodeResultMessage, NodeResultMessageAdmin)

class RuleNLSAdmin(admin.ModelAdmin):
    list_display = ('nls_rule_id', 'summary', 'language')
    list_filter = ('nls_rule_id', 'language')

admin.site.register(RuleNLS, RuleNLSAdmin)

class InformationalLinkAdmin(admin.ModelAdmin):
    list_display = ('rule', 'title', 'type', 'url')
    list_filter = ('rule', 'type')

admin.site.register(InformationalLink, InformationalLinkAdmin)


