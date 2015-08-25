from django.db import models
from django.contrib.auth.models import User

import datetime
from utilities import OAAMarkupToText, OAAMarkupToHTML
import textile

from rules.models import Updated

class Tool(Updated):
  tool_id     = models.AutoField(primary_key=True)  
  tool_slug   = models.SlugField(null=True,blank=True)
  abbrev       = models.CharField('Tool Name Abbreviation ', max_length=128)
  title        = models.CharField('Tool Name', max_length=512)
  title_html   = models.CharField(max_length=1024, default="")
  title_text   = models.CharField(max_length=512, default="")
  description      = models.TextField("Content (textile markup)", null=True,blank=True)
  description_html = models.TextField(default="", blank=True, null=True)
  url              = models.URLField(max_length=512, blank=True, null=True)

  class Meta:
    verbose_name        = "Tool"
    verbose_name_plural = "Tools"
    ordering = ['tool_slug']
  
  def save(self):
    if self.title:
      self.title_html    = OAAMarkupToHTML(self.title)
      self.title_text    = OAAMarkupToText(self.title)
    if self.description: 
      self.description_html  = textile.textile(self.description)
    self.updated_date  = datetime.datetime.now()
    super(Tool, self).save() # Call the "real" save() method.
    
  def __unicode__(self):
      return self.title_text 

  @models.permalink
  def get_absolute_url(self):
    return ('show_tool', [self.tool_slug]) 