from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse


from django.contrib import messages
from django.contrib.auth.decorators import login_required

from wcag20.models         import WCAG20_Guideline
from ruleCategories.models import RuleCategory
from rules.models          import Rule
from rulesets.models       import Ruleset, RuleMapping
from breadCrumbs           import breadCrumbs

class RulesetMapping:

  mapped   = False
  required = False

  def __init__(self, m, r):
    if m:
      self.mapped = m
      
    if r:  
      self.required = r
  
class RulesetMappingsByRule:

  def __init__(self, r):
    self.rule = r
    self.ruleset_info = [] 

class RulesetMappingsByRuleCategory:

  def __init__(self, rc):
    self.rule_category = rc
    self.rule_info = []
    self.has_rules = False
    
class RulesetMappingsByRuleCategories:

  def __init__(self, rs):
    self.rulesets = rs
    self.rule_category_info = []

class RulesetMappingsBySuccessCriterion:

  def __init__(self, sc):
    self.success_criterion = sc
    self.rule_info = []
    self.has_rules = False
    
class RulesetMappingsByGuideline:

  def __init__(self, g):
    self.guideline = g
    self.success_criterion_info = []

class RulesetMappingsByGuidelines:

  def __init__(self, rs):
    self.rulesets = rs
    self.guideline_info = []


def rule_category(request):
   rulesets          = Ruleset.objects.all()
   
   ruleset_by_rule_category = RulesetMappingsByRuleCategories(Ruleset.objects.all())
   
   for rc in RuleCategory.objects.all():
     rm_for_rc = RulesetMappingsByRuleCategory(rc)
     for r in rc.rules.all().order_by('wcag_primary__level', 'wcag_primary__guideline__principle__num', 'wcag_primary__guideline__num', 'wcag_primary__num'):
       rm_for_r = RulesetMappingsByRule(r)
       rm_for_rc.has_rules = True
       for rs in ruleset_by_rule_category.rulesets.all():
         try:
           rm = rs.rule_mappings.get(rule=r)
           mapping = RulesetMapping(True, rm.required)  
         except ObjectDoesNotExist:
           mapping = RulesetMapping(False, False)  
         rm_for_r.ruleset_info.append(mapping)       
       rm_for_rc.rule_info.append(rm_for_r)
     ruleset_by_rule_category.rule_category_info.append(rm_for_rc)
     
   request.session['oaa_bread_crumb_1_title'] = 'Rule categories'
   request.session['oaa_bread_crumb_1_url']   = reverse('show_rulesets_rule_category')
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''
     
   request.session['oaa_main_rulesets_url'] = reverse('show_rulesets_rule_category')
   request.session['oaa_main_rulesets_opt'] = 'compare'
      
   return render_to_response('rulesets/rule_categories.html',{
      'title'                    : 'Compare Rulesets by Rule Categories',
      'main'                     : 'rulesets',
      'rulesets'                 : rulesets,
      'option'                   : request.session['oaa_main_rulesets_opt'],
      'ruleset_by_rule_category' : ruleset_by_rule_category,
      'bread_crumbs'             : breadCrumbs(request),
   },context_instance=RequestContext(request))
      
def wcag20(request):
   rulesets          = Ruleset.objects.all()

   ruleset_by_guidelines = RulesetMappingsByGuidelines(Ruleset.objects.all())
   
   for g in WCAG20_Guideline.objects.all():
     rm_for_g = RulesetMappingsByGuideline(g)
     for sc in g.success_criteria.all():
       rm_for_sc = RulesetMappingsBySuccessCriterion(sc)
       for r in sc.rules.all():
         rm_for_r = RulesetMappingsByRule(r)
         rm_for_sc.has_rules = True
         for rs in ruleset_by_guidelines.rulesets.all():
           try:
             rm = rs.rule_mappings.get(rule=r)
             mapping = RulesetMapping(True, rm.required)  
           except ObjectDoesNotExist:
             mapping = RulesetMapping(False, False) 
           rm_for_r.ruleset_info.append(mapping)       
         rm_for_sc.rule_info.append(rm_for_r)
       rm_for_g.success_criterion_info.append(rm_for_sc)
     ruleset_by_guidelines.guideline_info.append(rm_for_g)

   request.session['oaa_bread_crumb_1_title'] = 'WCAG 2.0'
   request.session['oaa_bread_crumb_1_url']   = reverse('show_rulesets_wcag20')
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''
   
   request.session['oaa_main_rulesets_url']   = reverse('show_rulesets_wcag20')
   request.session['oaa_main_rulesets_opt']   = 'wcag20'
   
   return render_to_response('rulesets/wcag20.html',{
      'title'                 : 'Compare Rulesets by WCAG 2.0 Guidelines',
      'main'                  : 'rulesets',
      'rulesets'              : rulesets,
      'option'                : request.session['oaa_main_rulesets_opt'],
      'ruleset_by_guidelines' : ruleset_by_guidelines,
      'bread_crumbs'          : breadCrumbs(request)
   },context_instance=RequestContext(request))


def scope(request):
   rulesets = Ruleset.objects.all()

   element_rules = Rule.objects.filter(scope='1').order_by('wcag_primary__guideline__principle__num', 'wcag_primary__guideline__num', 'wcag_primary__num')
   
   element_rule_mappings = []
   for r in element_rules.all():
     rm_for_r = RulesetMappingsByRule(r)
     for rs in rulesets.all():
       try:
         rm = rs.rule_mappings.get(rule=r)
         mapping = RulesetMapping(True, rm.required)  
       except ObjectDoesNotExist:
         mapping = RulesetMapping(False, False)  
       rm_for_r.ruleset_info.append(mapping)       
     element_rule_mappings.append(rm_for_r)

   page_rules    = Rule.objects.filter(scope='2').order_by('wcag_primary__guideline__principle__num', 'wcag_primary__guideline__num', 'wcag_primary__num')

   page_rule_mappings = []
   for r in page_rules.all():
     rm_for_r = RulesetMappingsByRule(r)
     for rs in rulesets.all():
       try:
         rm = rs.rule_mappings.get(rule=r)
         mapping = RulesetMapping(True, rm.required)  
       except ObjectDoesNotExist:
         mapping = RulesetMapping(False, False)  
       rm_for_r.ruleset_info.append(mapping)       
     page_rule_mappings.append(rm_for_r)
   
   website_rules = Rule.objects.filter(scope='3').order_by('wcag_primary__guideline__principle__num', 'wcag_primary__guideline__num', 'wcag_primary__num')

   website_rule_mappings = []
   for r in website_rules.all():
     rm_for_r = RulesetMappingsByRule(r)
     for rs in rulesets.all():
       try:
         rm = rs.rule_mappings.get(rule=r)
         mapping = RulesetMapping(True, rm.required)  
       except ObjectDoesNotExist:
         mapping = RulesetMapping(False, False)  
       rm_for_r.ruleset_info.append(mapping)       
     website_rule_mappings.append(rm_for_r)

   request.session['oaa_bread_crumb_1_title'] = 'Rule scope'
   request.session['oaa_bread_crumb_1_url']   = reverse('show_rulesets_scope')
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''
    
   request.session['oaa_main_rulesets_url'] = reverse('show_rulesets_scope')
   request.session['oaa_main_rulesets_opt'] = 'scope'
   
   return render_to_response('rulesets/scope.html',{
      'title'                 : 'Rules by Rule Scope',
      'main'                  : 'rulesets',
      'rulesets'              : rulesets,
      'option'                : request.session['oaa_main_rulesets_opt'],
      'element_rule_mappings' : element_rule_mappings,
      'page_rule_mappings'    : page_rule_mappings,
      'website_rule_mappings' : website_rule_mappings,
      'website_rules'         : website_rules,
      'bread_crumbs'          : breadCrumbs(request),
   },context_instance=RequestContext(request))



def rule(request, rule_id):
   rulesets        = Ruleset.objects.all()
   rule            = Rule.objects.get(rule_id=rule_id)

   request.session['oaa_bread_crumb_2_title'] = rule.nls_rule_id
   request.session['oaa_bread_crumb_2_url']   = reverse('show_rule', args=(rule.rule_id,))
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''
   
   return render_to_response('rulesets/rule.html',{
      'website'         : "OAA Rule: " + rule.summary_text,
      'title'           : "Rule: " + rule.summary_html,
      'main'            : 'ruleset',
      'rulesets'        : rulesets,
      'option'          : request.session['oaa_main_rulesets_opt'],
      'rule'            : rule,
      'bread_crumbs'    : breadCrumbs(request),
   },context_instance=RequestContext(request))# Create your views here.
   


class RuleMappingsForRuleCategory:

   def __init__(self, rc):
    self.rule_category = rc
    self.rule_mappings = []  
    
def ruleset(request, ruleset_slug):
   ruleset           = Ruleset.objects.get(slug=ruleset_slug)
   rulesets          = Ruleset.objects.all()
   
   required_rules    = RuleMapping.objects.filter(ruleset=ruleset, required=True)
   recommended_rules = RuleMapping.objects.filter(ruleset=ruleset, required=False)
      
   rule_mappings_by_categories = []
   
   for rc in RuleCategory.objects.all():
     rm_for_rc = RuleMappingsForRuleCategory(rc)
     for rm in RuleMapping.objects.filter(ruleset=ruleset, rule__rule_category=rc).order_by('rule__wcag_primary__level', 'rule__wcag_primary__guideline__principle__num', 'rule__wcag_primary__guideline__num', 'rule__wcag_primary__num', '-required'):     
       rm_for_rc.rule_mappings.append(rm)
          
     rule_mappings_by_categories.append(rm_for_rc)     

   request.session['oaa_bread_crumb_1_title'] = ruleset.title_text
   request.session['oaa_bread_crumb_1_url']   = reverse('show_ruleset', args=(ruleset.slug,))
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''
     
   
   request.session['oaa_main_rulesets_url'] = reverse('show_ruleset', args=(ruleset.slug,))   
   request.session['oaa_main_rulesets_opt'] = ruleset.slug   


   return render_to_response('rulesets/ruleset.html',{
      'website'           : 'OAA Ruleset: ' + ruleset.title,
      'title'             : 'Ruleset: ' + ruleset.title,
      'main'              : 'rulesets',
      'option'            : request.session['oaa_main_rulesets_opt'],
      'rulesets'          : rulesets,
      'required_rules'    : required_rules,
      'recommended_rules' : recommended_rules,
      'rule_mappings_by_categories' : rule_mappings_by_categories,
      'bread_crumbs'      : breadCrumbs(request),
   },context_instance=RequestContext(request))

   
def show(request):
  slug = Ruleset.objects.get(ruleset_id='ARIA_TRANS').slug
  return ruleset(request, slug)


   
       