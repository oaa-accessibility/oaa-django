from django.db import models

# Ruleset models

import CONST
from utilities import OAAMarkupToHTML, OAAMarkupToText
import textile


from rules.models import Rule, Updated

## Rule Sets (e.g. WCAG20_ARIA_STRICT)
class Ruleset(Updated):
  ruleset_id         = models.CharField(max_length=64) 
  version            = models.CharField('Ruleset Version', max_length=16, default="unknown")
  slug               = models.SlugField(max_length=64, null=True,blank=True)
  title              = models.CharField('Ruleset Title', max_length=512)
  title_html         = models.CharField(max_length=2014, default="")
  title_text         = models.CharField(max_length=512, default="")
  web_resources      = models.TextField('Target Web Resources', default="")
  web_resources_html = models.TextField(default="", null=True,blank=True)
  description        = models.TextField(null=True,blank=True)
  description_html   = models.TextField(blank=True, default="")
  author             = models.CharField('Ruleset Author',max_length=64, default="unknown")
  author_url         = models.URLField('Ruleset Author URL',max_length=256, default="")

  class Meta:
    verbose_name        = "Ruleset"
    verbose_name_plural = "Rulesets"
    ordering = ['title_text']
    
  def save(self):
    if not self.slug:
      self.slug = self.ruleset_id
    self.title_html = OAAMarkupToHTML(self.title)
    self.title_text = OAAMarkupToText(self.title)
    if self.web_resources:
      self.web_resources_html = textile.textile(self.web_resources)
    if self.description:   
      self.description_html  = textile.textile(self.description)
    super(Ruleset, self).save() # Call the "real" save() method.  
    
  def __unicode__(self):
      return self.title_text 

  @models.permalink
  def get_absolute_url(self):
    return ('show_ruleset', [self.slug])     


## NLS descriptions of Rule Sets
class RulesetNLS(models.Model):
  ruleset          = models.ForeignKey(Ruleset, related_name='ruleset_nls')  
  language         = models.CharField('Language of text', max_length=6, choices=CONST.NLS_LANGUAGES, default='en') 
  title            = models.CharField('Ruleset Title', max_length=512)
  title_html       = models.CharField(max_length=2014, default="")
  title_text       = models.CharField(max_length=512, default="")
  description      = models.TextField(null=True,blank=True)
  description_html = models.TextField(blank=True, default="")

  def save(self):
    self.title_html = OAAMarkupToHTML(self.title)
    self.title_text = OAAMarkupToText(self.title)
    if self.web_resources:
      self.web_resources_html = textile.textile(self.web_resources)
    if self.description:   
      self.description_html   = textile.textile(self.description)
    super(RulesetNLS, self).save() # Call the "real" save() method.  


class RuleMapping(models.Model):
  ruleset  = models.ForeignKey(Ruleset, related_name='rule_mappings')  
  rule     = models.ForeignKey(Rule, related_name='rule_mappings')   
  required = models.BooleanField(default=True)      
  enabled  = models.BooleanField(default=True)      

  class Meta:
    ordering = ['ruleset', 'rule__wcag_primary']

