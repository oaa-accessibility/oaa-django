class RuleMappingsForRuleCategory:

   def __init__(self, rs):
    self.rule_category = rs
    self.rule_mappings = []  


def ruleset(request, ruleset_slug):
   ruleset           = Ruleset.objects.get(slug=ruleset_slug)
   rulesets          = Ruleset.objects.all()
   
   rule_mappings = RuleMapping.objects.filter(ruleset=ruleset).order_by('rule__wcag_primary__level', 'rule__wcag_primary__guideline__principle__num', 'rule__wcag_primary__guideline__num', 'rule__wcag_primary__num')
   
   rule_mappings_by_rule_categories = []
   
   for rc in RuleCategory.objects.all():
     rm_for_rc = RuleMappingsForRuleCategory(rc)
     for rm in rule_mappings:     
       if rm.rule.rule_category == rc:
          rm_for_rc.rule_mappings.append(rm)
          
     rule_mappings_by_rule_categories.append(rm_for_rc)     
      
   request.session['oaa_main_rulesets_url'] = reverse('show_ruleset', args=(ruleset.slug,))   


   return render_to_response('rulesets/ruleset.html',{
      'website'           : 'OAA Ruleset: ' + ruleset.title,
      'title'             : 'Ruleset: ' + ruleset.title,
      'main'              : 'rulesets',
      'ruleset'           : ruleset,
      'rulesets'          : rulesets,
      'rule_mappings_by_rule_categories' : rule_mappings_by_rule_categories,
      ''
      'bread_crumbs'      : breadCrumbs(request, []),
   },context_instance=RequestContext(request))
