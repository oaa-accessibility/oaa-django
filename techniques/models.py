from django.db import models
from django.contrib.auth.models import User
import re

from django.core import urlresolvers

# Create your models here.

import CONST
from utilities import OAAMarkupToHTML, OAAMarkupToText
import textile


from rules.models import Rule, Updated

TECHNIQUE_TYPE = (
  ('PR', 'Preferred technique, should be used whenever possible'),
  ('SP', 'Special case, should only be used when preferred techniques are not possible'),
)

class Technique(Updated):
  technique_id =  models.CharField('Technique ID', max_length=64, unique=True) 
  rule         = models.ForeignKey(Rule, related_name="techniques")
  type         = models.CharField('Technique Type',  max_length=2,   choices=TECHNIQUE_TYPE, default='PR')
  title        = models.CharField('Technique Title', max_length=512)
  title_html   = models.CharField(max_length=1024, default="")
  abbrev       = models.CharField('Technique Abbreviation', max_length=128, null=True,blank=True )
  abbrev_html  = models.CharField(max_length=256, default="")
  notes        = models.TextField('Technique Notes', null=True,blank=True)
  notes_html   = models.TextField(default="")
  url          = models.URLField('Technique URL', null=True, blank=True)
  
  class Meta:
    verbose_name        = "Technique"
    verbose_name_plural = "Techniques"
    ordering = ['rule', 'type']
  
  def save(self):
    if self.title:
      self.title_html = OAAMarkupToHTML(self.title)
    if self.abbrev:
      self.abbrev_html = OAAMarkupToHTML(self.abbrev)
    if self.notes:
      self.notes_html  = textile.textile(self.notes)
    super(Technique, self).save() # Call the "real" save() method.
    
  def __unicode__(self):
      return str(self.rule.nls_rule_id) + ': ' + self.title 
      
  def get_admin_url(self):
    return urlresolvers.reverse('admin:techniques_technique_change', args=(self.id,))
  

## Non-English description of technique
class TechniqueNLS(Updated):
  technique  = models.ForeignKey(Technique)
  language   = models.CharField('Technique Language', max_length=6, choices=CONST.NLS_LANGUAGES, default='en')   
  title        = models.CharField('Technique Title', max_length=512)
  title_html   = models.CharField(max_length=1024, default="no title")
  abbrev       = models.CharField('Technique Abbreviation', max_length=128, null=True,blank=True )
  abbrev_html  = models.CharField(max_length=256, default="")
  notes       = models.TextField('Technique Description', null=True,blank=True)
  notes_html  = models.TextField(default="")
  url        = models.URLField('Technique URL', null=True, blank=True)

  class Meta:
    verbose_name        = "Technique NLS"
    verbose_name_plural = "Technique NLS"
    ordering = ['technique', 'language', 'title']

  def save(self):
    if self.title:
      self.title_html = OAAMarkupToHTML(self.title)
    if self.abbrev:
      self.abbrev_html = OAAMarkupToHTML(self.abbrev)
    if self.notes:
      self.notes_html  = textile.textile(self.notes)
    super(TechniqueNLS, self).save() # Call the "real" save() method.

class TechniqueGroup(Updated):
  techniques = models.ManyToManyField(Technique, related_name='technique_groups')  
  title      = models.CharField('Technique Group Title',    max_length=512)
  title_html = models.CharField(max_length=512, default="")
  description       = models.TextField('Technique Group Description', null=True, blank=True)
  description_html  = models.TextField(default="")

  def save(self):
    if self.title:
      self.title_html = OAAMarkupToHTML(self.title)
    if self.description:  
      self.description_html  = textile.textile(self.description)
    super(TechniqueGroup, self).save() # Call the "real" save() method.

## Non-English description of technique group
class TechniqueGroupNLS(Updated):
  technique_group  = models.ForeignKey(TechniqueGroup)
  language         = models.CharField('Technique Group Language', max_length=8, choices=CONST.NLS_LANGUAGES, default='en')   
  title            = models.CharField('Technique Group Title',    max_length=512)
  title_html       = models.CharField(max_length=512, default="")
  desc             = models.TextField('Technique Group Description', null=True,blank=True)
  desc_html        = models.TextField(blank=True, default="")

  def save(self):
    if self.title:
      self.title_html = OAAMarkupToHTML(self.title)
    if self.description:  
      self.description_html  = textile.textile(self.description)
    super(TechniqueGroupNLS, self).save() # Call the "real" save() method.

