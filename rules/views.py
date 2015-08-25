from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.core import urlresolvers

from django.contrib.auth.models import User, Group

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from wcag20.models         import WCAG20_Guideline
from ruleCategories.models import RuleCategory
from rules.models          import Rule 
from techniques.models import Technique
from manualChecks.models import ManualCheck
from examples.models import Example, ExampleRuleReference
from forms import RuleReferenceCreationForm
import json

def ruleCategories(request):
   categories = RuleCategory.objects.all()
   
   try:
     request.session['oaa_main_rules_url']  = reverse('show_rules_by_rule_categories') + "#RULE_" + request.session['oaa_last_rule_id'] 
     request.session['oaa_main_rules_base'] = reverse('show_rules_by_rule_categories') 
   except:
     request.session['oaa_main_rules_url']  = reverse('show_rules_by_rule_categories')   
     request.session['oaa_main_rules_base'] = reverse('show_rules_by_rule_categories') 
   
   return render_to_response('rules/rule_categories.html',{
      'title'         : 'Rules Organized by Rule Categories',
      'main'          : 'rules',
      'rules'         : 'by_rule_category',
      'categories'    : categories,
   },context_instance=RequestContext(request))# Create your views here.

def wcag20(request):
   guidelines = WCAG20_Guideline.objects.all()
   admin_url = urlresolvers.reverse('admin:rules_rule_add')
   try:
     request.session['oaa_main_rules_url']  = reverse('show_rules_by_wcag20') +  "#RULE_" + request.session['oaa_last_rule_id'] 
     request.session['oaa_main_rules_base'] = reverse('show_rules_by_wcag20')  
   except:
     request.session['oaa_main_rules_url']  = reverse('show_rules_by_wcag20')
     request.session['oaa_main_rules_base'] = reverse('show_rules_by_wcag20')  
           
   return render_to_response('rules/wcag20.html',{
      'title'         : 'Rules Organized by WCAG 2.0 Guidelines and Success Criteria',
      'main'          : 'rules',
      'rules'         : 'by_wcag20',
      'guidelines'    : guidelines,
      'admin_url'     : admin_url,
   },context_instance=RequestContext(request))# Create your views here.

def rule(request, rule_id):
   rule            = Rule.objects.get(rule_id=rule_id)
   rule_categories = RuleCategory.objects.all()
   
   admin_url_rule = urlresolvers.reverse('admin:rules_rule_change', args=(rule.id,))
   admin_rule_reference = urlresolvers.reverse('admin:examples_examplerulereference_add', args=() )
   
   user = request.user
   rule_editor = False
   example_editor = False
   groups = user.groups.all()
   for group in groups:
     if group.name == 'rule_editors':
       rule_editor = True
     if group.name == 'example_editors':
       example_editor = True
      
   techniques = list( Technique.objects.filter(rule=rule)  )
   technique_admin_urls = []
   for t in techniques:
     technique_admin_urls.append( t.get_admin_url() )
   techniques_list = zip(techniques, technique_admin_urls)
   
   manualchecks = list( ManualCheck.objects.filter(rule=rule)  )
   manualchecks_admin_urls = []
   for m in manualchecks:
     manualchecks_admin_urls.append( m.get_admin_url() )
   manualchecks_list = zip(manualchecks, manualchecks_admin_urls)
   
   ruleReferences = list( ExampleRuleReference.objects.filter(rule=rule)  )
   examples_admin_urls = []
   for r in ruleReferences:
     examples_admin_urls.append( r.get_admin_url() )
   examples_list = zip(ruleReferences, examples_admin_urls)
   
   technique_add = urlresolvers.reverse('admin:techniques_technique_add', args=())
   manualcheck_add = urlresolvers.reverse('admin:manualChecks_manualcheck_add', args=())
   request.session['oaa_last_rule_id'] = rule.rule_id   
   request.session['oaa_main_rules_url'] = request.session['oaa_main_rules_base'] + "#RULE_" + rule.rule_id
   
   return render_to_response('rules/rule.html',{
      'website'         : "OAA " + rule.rule_category.title + " Rule: " + rule.summary_text,
      'title'           : rule.rule_category.title + " Rule</br>" + rule.summary_html,
      'main'            : 'rules',
      'rules'           : 'rule',
      'rule'            : rule,
      'admin_url_rule'       : admin_url_rule,
      'techniques_list' : techniques_list,
      'manualchecks_list' : manualchecks_list,
      'examples_list': examples_list,
      'rule_editor': rule_editor,
      'example_editor': example_editor,
      'technique_add': technique_add,
      'manualcheck_add': manualcheck_add,
      'admin_rule_reference':  admin_rule_reference,
      'rule_id' : rule_id
   },context_instance=RequestContext(request))# Create your views here.
   
   
def createRuleReference(request, rule_id):

  rule  = Rule.objects.get(rule_id=rule_id)
  
  rules_to_techniques = {}
  techniques = Technique.objects.filter(rule=rule)
  technique_names = []
  for t in techniques:
    title = t.title
    technique_names.append(rule.nls_rule_id + ": " + title)
  rules_to_techniques[rule.summary_text] = technique_names
     
  json_rules_to_techniques = json.dumps(rules_to_techniques)
  

  if request.POST:
    form = RuleReferenceCreationForm(request.POST)
    if form.is_valid():
      new_rule = form.save(commit = False)
      new_rule.rule = rule
      new_rule.note = " "
      new_rule.save()
      new_rule.techniques = form.cleaned_data['techniques']
      return HttpResponseRedirect("/")
  else:
    form = RuleReferenceCreationForm()
  return render_to_response("rules/add_rule_reference.html", {
    'title' : rule.summary_html,
    'form': form,
    'rule': rule,
    'rule_to_techniques': json_rules_to_techniques,
    'key': rule.summary_text,
  },context_instance=RequestContext(request))   
