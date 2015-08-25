import sys,os
sys.path.append(os.path.abspath('..'))
from django.core.exceptions import ObjectDoesNotExist

from django.core.management import setup_environ 
import coding.settings as settings
setup_environ(settings)

import json
import textile

from rules.models           import Rule, RuleNLS
from rules.models           import NodeResultMessage, NodeResultMessageNLS
from rules.models           import InformationalLink
from ruleCategories.models  import RuleCategory
from techniques.models      import Technique
from manualChecks.models    import ManualCheck
from wcag20.models          import WCAG20_SuccessCriterion
from markup.models          import ElementDefinition

from django.contrib.auth.models import User

json_data=open('oaa_exported_rules.json')

data = json.load(json_data)

json_data.close()

u = User.objects.all()[0]

Rule.objects.all().delete()
ManualCheck.objects.all().delete()
Technique.objects.all().delete()
InformationalLink.objects.all().delete()

def addTechnique(rule, id, title, url, date, editor):
  if title != "":
    if url != "":
      tech = Technique(rule=rule, technique_id=id, title=title, url=u, updated_date=date, updated_editor=editor)
    else:  
      tech = Technique(rule=rule, technique_id=id, title=title, updated_date=date, updated_editor=editor)
    tech.save()

def addManualCheck(rule, title, url, date, editor):
  if title != "": 
    if url != "":
      mc = ManualCheck(rule=rule, title=title, url=url, updated_date=date, updated_editor=editor)
    else:  
      mc = ManualCheck(rule=rule, title=title, updated_date=date, updated_editor=editor)
    mc.save()

def addInformationalLink(rule, type, title, url, date, editor):
  print "  Information link title: " + title
  print "  Information link url:   " + url
  if title != "": 
    if url != "":
      il = InformationalLink(rule=rule, type=str(type), title=title, url=url, updated_date=date, updated_editor=editor)
    else:  
      il = InformationalLink(rule=rule, type=str(type), title=title, updated_date=date, updated_editor=editor)
    il.save()

def addRuleResultMessage(rule, label, message, date, editor):
  print "  Rule Result Message: " + label + ": " + message

  if label == 'MANUAL_CHECK_S':
    rule.rule_result_mc_s      = message
  elif label == 'MANUAL_CHECK_P':
    rule.rule_result_mc_p      = message
  elif label == 'FAIL_S':
    rule.rule_result_fail_s    = message
  elif label == 'FAIL_P':
    rule.rule_result_fail_p    = message
  elif label == 'HIDDEN_S':
    rule.rule_result_hidden_s  = message
  elif label == 'HIDDEN_P':
    rule.rule_result_hidden_p  = message
  elif label == 'NOT_APPLICABLE':
     rule.rule_result_na       = message
     
  rule.save()

def addNodeResultMessage(rule, label, message, date, editor):
  print "  Node Result Message: " + label + ": " + message
  
  if label != "" and message != "": 
    nrm = NodeResultMessage(rule=rule, label=label, message=message, updated_date=date, updated_editor=editor)
    nrm.save()

for r in data['rules']:
   print "\nRule: " + r['nls_rule_id']

   resource_properties = ""
   if r['resource_properties'] != "":
     resource_properties = ' '.join(r['resource_properties'])
     print "  Resource Properties: " + resource_properties
     
   try:
     rule = Rule.objects.get(rule_id=r['rule_id'])
     print "  Updating Rule: " + r['nls_rule_id']
     rule.scope=r['scope']
     rule.language_dependancy=r['language_dependency']
     rule.cache_dependency=r['cache_dependency']
     rule.resource_properties=resource_properties
     rule.validation=r['validate']
     rule.wcag_primary = WCAG20_SuccessCriterion.get_by_wcag_number(r['wcag_primary'])
     rule.rule_category = RuleCategory.objects.get(category_num=r['rule_category'])
     rule.updated_date=r['last_updated']
     rule.updated_editor=u
   
   except ObjectDoesNotExist:  
     print "  Creating Rule: " + r['nls_rule_id']
     resource_properties = ",".join(r['resource_properties'])
     rule = Rule(rule_id=r['rule_id'],scope=r['scope'],language_dependancy=r['language_dependency'],cache_dependency=r['cache_dependency'],resource_properties=resource_properties,validation=r['validate'],updated_date=r['last_updated'],updated_editor=u)
     rule.wcag_primary = WCAG20_SuccessCriterion.get_by_wcag_number(r['wcag_primary'])
     rule.rule_category = RuleCategory.objects.get(category_num=r['rule_category'])
     rule.save()

   rule.wcag_related.clear() 
   for related in r['wcag_related']:
      rule.wcag_related.add(WCAG20_SuccessCriterion.get_by_wcag_number(related)) 

   rule.target_resources.clear()  
   for m in r['target_resources']:
     try: 
       rule.target_resources.add(ElementDefinition.get_by_title(m))
     except:
       print "  target resources exception for element definition: " + m  

   rule.save()

   rule.nls_rule_id    = r['nls_rule_id']
   rule.definition     = r['definition']
   rule.summary        = r['summary']
   
   rule.target_resource_desc = r['target_resource_desc']

   p = r['purpose']

   print "TYPE: " + str(type(p))
   l = len(p)

   if l > 0:
     rule.purpose_1 = r['purpose'][0]
   else:  
     rule.purpose_1 = ""
     
   if l > 1:
     rule.purpose_2 = r['purpose'][1]
   else:  
     rule.purpose_2 = ""
          
   if l > 2:
     rule.purpose_3 = r['purpose'][2]
   else:  
     rule.purpose_3 = ""
     
   if l > 3:
     rule.purpose_4 = r['purpose'][3]
   else:  
     rule.purpose_4 = ""
     
   i = 1
   Technique.objects.filter(rule=rule).delete()  
   for tech in r['techniques']:
     tech_id = r['rule_id'] + "_T" + str(i)
     i += 1
     addTechnique(rule, tech_id, tech, '', r['last_updated'], u)

   ManualCheck.objects.filter(rule=rule).delete()  
   for mc in r['manual_checks']:
     addManualCheck(rule, mc, '', r['last_updated'], u)

   informational_links = r['informational_links']
   
   InformationalLink.objects.filter(rule=rule).delete()  
   for info in r['informational_links']:
     addInformationalLink(rule, info['type'], info['title'], info['url'], r['last_updated'], u)

   for message in r['rule_result_messages']:
     addRuleResultMessage(rule, message, r['rule_result_messages'][message], r['last_updated'], u)

   NodeResultMessage.objects.filter(rule=rule).delete()  
   for message in r['node_result_messages']:
     addNodeResultMessage(rule, message, r['node_result_messages'][message], r['last_updated'], u)
   
   rule.save()
  