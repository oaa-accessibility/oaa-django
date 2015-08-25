from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import re

# Rule Category models

import CONST

## Rule Categories (e.g. abbrev, audio, headings, images, links...)  
class RuleCategory(models.Model):
  category_num  = models.IntegerField(unique=True)
  category_id   = models.CharField(max_length=64) 
  abbrev        = models.CharField(max_length=2, default="x")
  title         = models.CharField(max_length=256)
  title_plural  = models.CharField("Title Plural", max_length=256)
  description   = models.TextField(null=True,blank=True)
  slug          = models.SlugField()
  order         = models.IntegerField()

  class Meta:
    verbose_name        = "Rule Category"
    verbose_name_plural = "Rule Categories"
    ordering = ['order','title']
    
  def __unicode__(self):
    return self.title

  def get_examples_url(self):
    return reverse('show_examples_for_rule_category', args=(self.slug,))
    
    
  def get_example_count(self):
    count = 0
    
    for eg in self.example_groups.all():
      count += eg.get_example_count()
        
    return count    

## NLS Descriptions of Rule Categories
class RuleCategoryNLS(models.Model):
  rule_category = models.ForeignKey(RuleCategory) 
  language      = models.CharField('Language of text', max_length=6, choices=CONST.NLS_LANGUAGES, default='en') 
  title         = models.CharField(max_length=250)
  description   = models.TextField(null=True,blank=True)

  class Meta:
    verbose_name        = "Rule Category NLS"
    verbose_name_plural = "Rule Categories NLS"
    ordering = ['language', 'rule_category', 'title']

  def __unicode__(self):
    return self.title

