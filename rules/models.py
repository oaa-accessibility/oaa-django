from django.db import models
from django.contrib.auth.models import User

import re
import CONST
from utilities import OAAMarkupToText, OAAMarkupToHTML
import textile


from markup.models          import ElementDefinition
from ruleCategories.models  import RuleCategory
from wcag20.models          import WCAG20_SuccessCriterion

## Helper class that includes the updated date and creator
class Updated(models.Model):
  updated_date   = models.DateTimeField(auto_now=True, editable=False)
  updated_editor = models.ForeignKey(User, editable=True)




## Rule 
RULE_SCOPE = (
  ('0', 'Unknown'), 
  ('1', 'Element'),
  ('2', 'Page'),
  ('3', 'Website'),
)

RULE_CACHE_DEPENDENCIES = (
  ('unknown',                  'Unknown'),
  ('abbreviations_cache',      'Abbreviations Cache'),
  ('color_contrast_cache',     'Color Contrast Cache'),
  ('controls_cache',           'Controls Cache'),
  ('headings_landmarks_cache', 'Headings/Landmarks Cache'),
  ('images_cache',             'Images Cache'),
  ('languages_cache',          'Languages Cache'),
  ('links_cache',              'Links Cache'),
  ('lists_cache',              'Lists Cache'),
  ('media_cache',              'Media Cache'),
  ('tables_cache',             'Tables Cache'),
)

class Rule(Updated):
  rule_id             = models.CharField('Rule ID', max_length=64, unique=True) 
  scope               = models.CharField('Rule Scope', max_length=1, choices=RULE_SCOPE, default='0')
  wcag_primary        = models.ForeignKey(WCAG20_SuccessCriterion, related_name='rules')
  wcag_related        = models.ManyToManyField(WCAG20_SuccessCriterion, related_name='related_rules')  
  target_resources    = models.ManyToManyField(ElementDefinition, related_name='rules') 
  mc_properties       = models.CharField('Comma separated list of cache properties for manual check views', max_length=250)
  resource_properties = models.CharField('Comma separated list of cache properties and attributes used by the rule', max_length=250)
  rule_category       = models.ForeignKey(RuleCategory, related_name='rules') 
  language_dependancy = models.CharField('Language codes separated by commas', max_length=100, default='')
  cache_dependency    = models.CharField('Cache the validation function uses', max_length=25, choices=RULE_CACHE_DEPENDENCIES, default='unknown')
  validation          = models.TextField('Javascript code for validation function', null=True,blank=True)

  nls_rule_id     = models.CharField('Translated Rule ID', max_length=64) 
  
  definition      = models.CharField('Rule Definition', max_length=512)
  definition_html = models.CharField(max_length=512, default="")
  summary         = models.CharField('Rule Summary (shorter version of definition)', max_length=128)
  summary_html    = models.CharField(max_length=256, default="")
  summary_text    = models.CharField(max_length=128, default="")
  
  target_resource_desc      = models.CharField('Summary of the types of element definitions this rule tests', max_length=512)
  target_resource_desc_html = models.CharField(max_length=512)
  
  purpose_1      = models.CharField('Purpose 1 (i.e how does the rule help people with disabilites)', max_length=512)
  purpose_1_html = models.CharField(max_length=512, default="")
  purpose_2      = models.CharField('Purpose 2', null=True, blank=True, max_length=512)
  purpose_2_html = models.CharField(max_length=512, default="")
  purpose_3      = models.CharField('Purpose 3', null=True, blank=True, max_length=512)
  purpose_3_html = models.CharField(max_length=512, default="")
  purpose_4      = models.CharField('Purpose 4', null=True, blank=True, max_length=512)
  purpose_4_html = models.CharField(max_length=512, default="")
  
  rule_result_mc_s     = models.CharField('Rule Result Message: One manual check'            , null=True, blank=True, max_length=512)
  rule_result_mc_p     = models.CharField('Rule Result Message: More than one manual check'  , null=True, blank=True, max_length=512)
  rule_result_fail_s   = models.CharField('Rule Result Message: One failed element'          , null=True, blank=True, max_length=512)
  rule_result_fail_p   = models.CharField('Rule Result Message: More than one failed element', null=True, blank=True, max_length=512)
  rule_result_hidden_s = models.CharField('Rule Result Message: One hidden element'          , null=True, blank=True, max_length=512)
  rule_result_hidden_p = models.CharField('Rule Result Message: More than one hidden element', null=True, blank=True, max_length=512)
  rule_result_na       = models.CharField('Rule Result Message: Not Applicable Message'      , null=True, blank=True, max_length=512)
  
  class Meta:
    verbose_name        = "Rule"
    verbose_name_plural = "Rules"
    ordering = ['rule_id']

  @models.permalink
  def get_absolute_url(self):
    return ('show_rule', [self.rule_id])         

  def __unicode__(self):
      return self.summary_text

  def save(self):
    self.definition_html              = OAAMarkupToHTML(self.definition)
    self.summary_html                 = OAAMarkupToHTML(self.summary)
    self.summary_text                 = OAAMarkupToText(self.summary)
    if self.target_resource_desc:
      self.target_resource_desc_html    = OAAMarkupToHTML(self.target_resource_desc)
    if self.purpose_1:
      self.purpose_1_html               = OAAMarkupToHTML(self.purpose_1)
    if self.purpose_2:
      self.purpose_2_html               = OAAMarkupToHTML(self.purpose_2)
    if self.purpose_2:
      self.purpose_3_html               = OAAMarkupToHTML(self.purpose_3)
    if self.purpose_2:
      self.purpose_4_html               = OAAMarkupToHTML(self.purpose_4)
    super(Rule, self).save() # Call the "real" save() method.

  def number_of_examples(self):
    num = 0;
    
    for rr in self.rule_references.all():
      num += 1
    
    return num

  def examples(self):
    examples = [];
    
    for rr in self.rule_references.all():
      examples.push(rr.example)
    
    return examples
       
   
  def wcag20_requirements(self):
    return "%s - %s"%(self.wcag_primary.number(),self.wcag_related_list())

  def target_resources_as_string(self):
    lst = []
    for t in self.target_resources.all():
      lst.append("'%s'"%t.title())

    return ", ".join(lst)

  def get_next_rule_by_rule_category(self):
    rules = Rule.objects.order_by('rule_category','wcag_primary')
    nr = 0
    for r in reversed(rules):
      if r == self:
        return nr
      else: 
        nr = r
          
    return 0      

  def get_previous_rule_by_rule_category(self):
    rules = Rule.objects.order_by('rule_category','wcag_primary')
    pr = 0
    for r in rules:
      if r == self:
        return pr
      else: 
        pr = r
        
    return pr      

  def get_next_rule_by_wcag_success_criteria(self):
    rules = Rule.objects.order_by('wcag_primary','rule_category')
    nr = 0
    for r in reversed(rules):
      if r == self:
        return nr
      else: 
        nr = r
          
    return 0      

  def get_previous_rule_by_wcag_success_criteria(self):
    rules = Rule.objects.order_by('wcag_primary','rule_category',)
    pr = 0
    for r in rules:
      if r == self:
        return pr
      else: 
        pr = r
   
    return pr      





## NLS description of rule
class RuleNLS(Updated):
  rule         = models.ForeignKey(Rule)
  
  language     = models.CharField('Language of text', max_length=6, choices=CONST.NLS_LANGUAGES, default='en') 
  
  nls_rule_id  = models.CharField('Translated Rule ID', max_length=64) 
  
  definition      = models.CharField('Rule Definition', max_length=512)
  definition_html = models.CharField(max_length=512, default="")
  summary         = models.CharField('Rule Summary (shorter version of definition)', max_length=128)
  summary_html    = models.CharField(max_length=128, default="")
  
  target_resource_desc      = models.CharField('Summary of the types of element definitions this rule tests', max_length=512)
  target_resource_desc_html = models.CharField(max_length=512)
  
  purpose_1      = models.CharField('Purpose 1 (i.e how does the rule help people with disabilites)', max_length=512)
  purpose_1_html = models.CharField(max_length=512, default="")
  purpose_2      = models.CharField('Purpose 2', null=True, blank=True, max_length=512)
  purpose_2_html = models.CharField(max_length=512, default="")
  purpose_3      = models.CharField('Purpose 3', null=True, blank=True, max_length=512)
  purpose_3_html = models.CharField(max_length=512, default="")
  purpose_4      = models.CharField('Purpose 4', null=True, blank=True, max_length=512)
  purpose_4_html = models.CharField(max_length=512, default="")
  
  rule_result_mc_s      = models.CharField('Rule Result Message: One manual check'            , null=True, blank=True, max_length=512)
  rule_result_mc_p      = models.CharField('Rule Result Message: More than one manual check'  , null=True, blank=True, max_length=512)
  rule_result_fail_s    = models.CharField('Rule Result Message: One failed element'          , null=True, blank=True, max_length=512)
  rule_result_fail_p    = models.CharField('Rule Result Message: More than one failed element', null=True, blank=True, max_length=512)
  rule_result_hidden_s  = models.CharField('Rule Result Message: One hidden element'          , null=True, blank=True, max_length=512)
  rule_result_hidden_p  = models.CharField('Rule Result Message: More than one hidden element', null=True, blank=True, max_length=512)
  rule_result_na        = models.CharField('Rule Result Message: Not Applicable Message'      , null=True, blank=True, max_length=512)
  
  def save(self):
    self.definition_html              = OAAMarkupToHTML(self.definition)
    self.summary_html                 = OAAMarkupToHTML(self.summary)
    self.summary_text                 = OAAMarkupToText(self.summary)
    if self.target_resource_desc:
      self.target_resource_desc_html    = OAAMarkupToHTML(self.target_resource_desc)
    if self.purpose_1:
      self.purpose_1_html               = OAAMarkupToHTML(self.purpose_1)
    if self.purpose_2:
      self.purpose_2_html               = OAAMarkupToHTML(self.purpose_2)
    if self.purpose_2:
      self.purpose_3_html               = OAAMarkupToHTML(self.purpose_3)
    if self.purpose_2:
      self.purpose_4_html               = OAAMarkupToHTML(self.purpose_4)
    super(RuleNLS, self).save() # Call the "real" save() method.

  class Meta:
        ordering = ['rule', 'language', 'summary']
        verbose_name="Rule (NLS)"
        verbose_name_plural="Rules (NLS)"

  
  def get_absolute_url(self):
      return ('show_rule', [self.human_id])     

  def show_rule_id(self):
      return 'Rule ' + str(self.human_id) 

  def link_text(self):
      return 'Rule ' + str(self.human_id)

  def short_description(self):
      return 'Rule ' + str(self.human_id) + ': ' + self.getDescription() 

  def purpose_list(self):
    lst = []
    if self.purpose_1 != None and self.purpose_1 != "":
      lst.append("'%s'"%self.purpose_1)
    if self.purpose_2 != None and self.purpose_2 != "":
      lst.append("'%s'"%self.purpose_2)
    if self.purpose_3 != None and self.purpose_3 != "":
      lst.append("'%s'"%self.purpose_3)
    if self.purpose_4 != None and self.purpose_4 != "":
      lst.append("'%s'"%self.purpose_4)
    return ",".join(lst)

  def techniques_list(self):
    lst = []
    return ",".join(lst)

  def manual_checks_list(self):
    lst = []
    return ",".join(lst)
    
  def __unicode__(self):
      return 'Rule ' + str(self.nls_rule_id) + ': ' + self.getSummary() 

## Information link
INFORMATIONAL_LINK_TYPE = (
    ('0', 'Unknown'),
    ('1', 'W3C Specification'),
    ('2', 'WCAG 2.0 Technique'),
    ('3', 'Technique'),
    ('4', 'Example'),
    ('5', 'Manual Check Proceedure'),
    ('6', 'Authoring Tool'),
    ('7', 'Code Library or Product Documentation'),
    ('8', 'Other Resource'),
)

## Information link
NODE_RESULT_LABEL_CHOICES = (
    ('ELEMENT_PASS_1',   'ELEMENT_PASS_1'),
    ('ELEMENT_PASS_2',   'ELEMENT_PASS_2'),
    ('ELEMENT_PASS_3',   'ELEMENT_PASS_3'),
    ('ELEMENT_PASS_4',   'ELEMENT_PASS_4'),
    ('ELEMENT_PASS_5',   'ELEMENT_PASS_5'),
    ('ELEMENT_FAIL_1',   'ELEMENT_FAIL_1'),
    ('ELEMENT_FAIL_2',   'ELEMENT_FAIL_2'),
    ('ELEMENT_FAIL_3',   'ELEMENT_FAIL_3'),
    ('ELEMENT_FAIL_4',   'ELEMENT_FAIL_4'),
    ('ELEMENT_FAIL_5',   'ELEMENT_FAIL_5'),
    ('ELEMENT_MC_1',     'ELEMENT_MC_1'),
    ('ELEMENT_MC_2',     'ELEMENT_MC_2'),
    ('ELEMENT_MC_3',     'ELEMENT_MC_3'),
    ('ELEMENT_MC_4',     'ELEMENT_MC_4'),
    ('ELEMENT_MC_5',     'ELEMENT_MC_5'),
    ('ELEMENT_HIDDEN_1', 'ELEMENT_HIDDEN_1'),
    ('ELEMENT_HIDDEN_2', 'ELEMENT_HIDDEN_2'),
    ('PAGE_PASS_1', 'PAGE_PASS_1'),
    ('PAGE_PASS_2', 'PAGE_PASS_2'),
    ('PAGE_PASS_3', 'PAGE_PASS_3'),
    ('PAGE_PASS_4', 'PAGE_PASS_4'),
    ('PAGE_PASS_5', 'PAGE_PASS_5'),
    ('PAGE_FAIL_1', 'PAGE_FAIL_1'),
    ('PAGE_FAIL_2', 'PAGE_FAIL_2'),
    ('PAGE_FAIL_3', 'PAGE_FAIL_3'),
    ('PAGE_FAIL_4', 'PAGE_FAIL_4'),
    ('PAGE_FAIL_5', 'PAGE_FAIL_5'),
    ('PAGE_MC_1',   'PAGE_MC_1'),
    ('PAGE_MC_2',   'PAGE_MC_2'),
    ('PAGE_MC_3',   'PAGE_MC_3'),
    ('PAGE_MC_4',   'PAGE_MC_4'),
    ('PAGE_MC_5',   'PAGE_MC_5'),
    ('WEBSITE_PASS_1', 'WEBSITE_PASS_1'),
    ('WEBSITE_PASS_2', 'WEBSITE_PASS_2'),
    ('WEBSITE_PASS_3', 'WEBSITE_PASS_3'),
    ('WEBSITE_PASS_4', 'WEBSITE_PASS_4'),
    ('WEBSITE_PASS_5', 'WEBSITE_PASS_5'),
    ('WEBSITE_FAIL_1', 'WEBSITE_FAIL_1'),
    ('WEBSITE_FAIL_2', 'WEBSITE_FAIL_2'),
    ('WEBSITE_FAIL_3', 'WEBSITE_FAIL_3'),
    ('WEBSITE_FAIL_4', 'WEBSITE_FAIL_4'),
    ('WEBSITE_FAIL_5', 'WEBSITE_FAIL_5'),
    ('WEBSITE_MC_1',   'WEBSITE_MC_1'),
    ('WEBSITE_MC_2',   'WEBSITE_MC_2'),
    ('WEBSITE_MC_3',   'WEBSITE_MC_3'),
    ('WEBSITE_MC_4',   'WEBSITE_MC_4'),
    ('WEBSITE_MC_5',   'WEBSITE_MC_5'),
)

class NodeResultMessage(Updated):
  rule         = models.ForeignKey(Rule, related_name="node_result_messages")
  label        = models.CharField('Label',  choices=NODE_RESULT_LABEL_CHOICES, max_length=32)
  message      = models.CharField('Message', max_length=512)

  class Meta:
        ordering = ['label',]
        verbose_name="Node Result Message"
        verbose_name_plural="Node Result Message"

class NodeResultMessageNLS(Updated):
  rule_nls     = models.ForeignKey(RuleNLS, related_name="node_result_messages")
  label        = models.CharField('Label',  choices=NODE_RESULT_LABEL_CHOICES, max_length=32)
  message      = models.CharField('Message', max_length=512)

  class Meta:
        ordering = ['label', ]
        verbose_name="Node Result Message (NLS)"
        verbose_name_plural="Node Result Message (NLS)"

## Information link
INFORMATIONAL_LINK_TYPE = (
    ('0', 'Unknown'),
    ('1', 'W3C Specification'),
    ('2', 'WCAG 2.0 Technique'),
    ('3', 'Technique'),
    ('4', 'Example'),
    ('5', 'Manual Check Proceedure'),
    ('6', 'Authoring Tool'),
    ('7', 'Code Library or Product Documentation'),
    ('8', 'Other Resource'),
)

class InformationalLink(Updated):
  rule         = models.ForeignKey(Rule, related_name="informational_links")
  title        = models.CharField('Information Link Title', max_length=512)
  title_html   = models.CharField(max_length=512)
  type         = models.CharField('Type of Information Link',choices=INFORMATIONAL_LINK_TYPE, default='0', max_length=8)  
  url          = models.URLField('Information Link URL', max_length=512);

  class Meta:
        ordering = ['rule', 'title', 'type', 'url']
        verbose_name="Informational Link"
        verbose_name_plural="Informational Links"

  def save(self):
    self.title_html = OAAMarkupToHTML(self.title)
    super(InformationalLink, self).save() # Call the "real" save() method.
