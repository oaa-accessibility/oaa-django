from django.db import models
from PIL import Image

import textile
import datetime

from utilities import OAAMarkupToText, OAAMarkupToHTML
from utilities import HTMLToSourceCodeFormat, OAAMarkupRemoveHighlightCode

# Example models

from rules.models          import Updated
from ruleCategories.models import RuleCategory
from wcag20.models         import WCAG20_SuccessCriterion
from markup.models         import ElementDefinition
from techniques.models     import Rule, Technique
from manualChecks.models   import ManualCheck

from django.core import urlresolvers

def validate_image_extension(image): 
  file_exts = ('.gif', '.png', '.jpg', '.jpeg') 
  
  if not splitext(image.name)[1].lower() in file_exts: 
     raise ValidationError('Image types accepted: %s' % ' '.join(file_exts)) 
            

def example_image_path_and_filename( instance, filename ):

   path = 'examples/images/' + filename
   
   return path

class ExampleImage(models.Model):
  image_id    = models.AutoField(primary_key=True)
  image       = models.ImageField(validators=[validate_image_extension], upload_to=example_image_path_and_filename)
  description = models.CharField(max_length=200, default="")

  class Meta:
        ordering = ['image_id']
 
  def __init__(self, *args, **kwargs): 
        super(ExampleImage, self).__init__(*args, **kwargs) 
        self.label = 'Image file' 
        self.helptext = 'Select a png, gif, jpg or jpeg image'     


  def update_image(self, *args, **kwargs):
    # This code deletes the current file so that references to updated images do not change if the same file name is used
    # Basically provides an wasy way to update an existing image with changing the URI
    try:
        this = ExampleImage.objects.get(image_id=self.image_id)
        this.image.delete()
    except: pass
    super(ExampleImage, self).save(*args, **kwargs)   


def validate_object_extension(object): 
  file_exts = ('.class', '.swf') 
  
  if not splitext(object.name)[1].lower() in file_exts: 
     raise ValidationError('Object types accepted: %s' % ' '.join(file_exts)) 
            

def example_object_path_and_filename( instance, filename ):

   path = 'examples/objects/' + filename
   
   return path


class ExampleObject(models.Model):
  object_id    = models.AutoField(primary_key=True)
  object       = models.FileField(validators=[validate_object_extension], upload_to=example_object_path_and_filename)
  description  = models.CharField(max_length=200, default="")

  def __init__(self, *args, **kwargs): 
        super(ExampleObject, self).__init__(*args, **kwargs) 
        self.label = 'Flash or Java Applet file' 
        self.helptext = 'Select a .swf or .class file'     

  def update_object(self, *args, **kwargs):
    # This code deletes the current file so that references to updated images do not change if the same file name is used
    # Basically provides an wasy way to update an existing image with changing the URI
    try:
        this = ExampleObject.objects.get(object_id=self.object_id)
        this.object.delete()
    except: pass
    super(ExampleObject, self).save(*args, **kwargs)   


def validate_style_extension(style): 
  file_exts = ('.css', ) 
  
  if not splitext(style.name)[1].lower() in file_exts: 
     raise ValidationError('Style types accepted: %s' % ' '.join(file_exts)) 
            
def example_style_path_and_filename( instance, filename ):

   path = 'examples/css/' + filename
   
   return path

class ExampleStyle(models.Model):
  style_id    = models.AutoField(primary_key=True)
  style       = models.FileField(validators=[validate_style_extension], upload_to=example_style_path_and_filename)
  description = models.CharField(max_length=200, default="")

  def __init__(self, *args, **kwargs): 
        super(ExampleStyle, self).__init__(*args, **kwargs) 
        self.label = 'CSS file' 
        self.helptext = 'Select a .css file'     

  def update_style(self, *args, **kwargs):
    # This code deletes the current file so that references to updated images do not change if the same file name is used
    # Basically provides an wasy way to update an existing image with changing the URI
    try:
        this = ExampleStyle.objects.get(style_id=self.style_id)
        this.style.delete()
    except: pass
    super(ExampleStyle, self).save(*args, **kwargs)   

def validate_script_extension(script): 
  file_exts = ('.js', '.json') 
  
  if not splitext(script.name)[1].lower() in file_exts: 
     raise ValidationError('Script types accepted: %s' % ' '.join(file_exts)) 


def example_script_path_and_filename( instance, filename ):

   path = 'examples/js/' + filename
   
   return path

class ExampleScript(models.Model):
  script_id   = models.AutoField(primary_key=True)
  script      = models.FileField(validators=[validate_script_extension], upload_to=example_script_path_and_filename)
  description = models.CharField(max_length=200, default="")

  def __unicode__(self):
      return str(self.script) 

  def __init__(self, *args, **kwargs): 
        super(ExampleScript, self).__init__(*args, **kwargs) 
        self.label = 'Javascript file' 
        self.helptext = 'Select a .js file'     

  def update_script(self, *args, **kwargs):
    # This code deletes the current script file so that references to updated scripts
    # do not change if the same file name is used
    # Basically provides an easy way to update an existing image with changing the URI
    try:
        this = ExampleScript.objects.get(script_id=self.script_id)
        this.script.delete()
    except: pass
    super(ExampleScript, self).save(*args, **kwargs)   


class ExampleGroup(Updated):
  example_group_id   = models.AutoField(primary_key=True)  
  order              = models.IntegerField(default=0)  
  slug               = models.SlugField()
  title              = models.CharField('Example Group Title (Singular)', max_length=256)
  title_html         = models.CharField(max_length=512, default="")
  title_text         = models.CharField(max_length=256, default="")
  design_issues      = models.TextField("Design Issues", null=True,blank=True)
  design_issues_html = models.TextField(default="")
  rule_category      = models.ForeignKey(RuleCategory,related_name='example_groups', blank=True, null=True)

  class Meta:
    ordering = ['order', 'title_text', ]
    verbose_name        ="Example Group"
    verbose_name_plural ="Example Groups"

    
  @models.permalink
  def get_absolute_url(self):
    return ('show_examples_for_example_group', [self.slug])
        
  def save(self):
    if self.title:
      self.title_html       = OAAMarkupToHTML(self.title)
      self.title_text       = OAAMarkupToText(self.title)
      
    if self.design_issues:  
      self.design_issues_html = textile.textile(self.design_issues)
            
            
    self.updated_date     = datetime.datetime.now()
    
    super(ExampleGroup, self).save() # Call the "real" save() method.  
  
  def __unicode__(self):
      return 'Example Group: ' + self.title_text 

  def get_example_count(self):
      count = 0

      for e in self.examples.all():
        count += 1
          
      return count



EXAMPLE_STATUS = (
    ('acc', 'Accepted'),
    ('pro', 'Proposed'),
    ('dep', 'Deprecated'),
)

EXAMPLE_STATUS_HTML_CODE = (
    ('acc', '<span class="acc">Accepted</span>'),
    ('pro', '<span class="pro">Proposed</span>'),
    ('dep', '<span class="dep">Deprecated</span>'),
)

class Example(Updated):
  example_id       = models.AutoField(primary_key=True)  
  permanent_slug   = models.SlugField(null=True,blank=True)
  title            = models.CharField(max_length=512)
  title_html       = models.CharField(max_length=1024, default="")
  title_text       = models.CharField(max_length=512, default="")
  description      = models.TextField("Describe features of example", null=True,blank=True)
  description_html = models.TextField(default="")
  keyboard         = models.TextField("Information on keyboard shortcuts", null=True, blank=True)
  keyboard_html    = models.TextField(default="")
  status           = models.CharField(max_length=8,choices=EXAMPLE_STATUS,default='acc')
  external_url     = models.URLField("External URL to example", max_length=512, blank=True)
  style            = models.TextField('CSS code', null=True,blank=True)
  style_code       = models.TextField(default='')
  style_source     = models.TextField(default='')
  html             = models.TextField('HTML code for inside body tag', null=True,blank=True)
  html_code        = models.TextField(default='')
  html_source      = models.TextField(default='')
  script           = models.TextField('Javascript code', null=True,blank=True)
  script_code      = models.TextField(default='')
  script_source    = models.TextField(default='')
  onload           = models.CharField(null=True,blank=True, max_length=128)
  title_override   = models.CharField(null=True,blank=True, max_length=512)
  markup           = models.ManyToManyField(ElementDefinition,       related_name='examples', blank=True, null=True)
  example_group    = models.ManyToManyField(ExampleGroup,            related_name='examples', blank=True, null=True)
  success_criteria = models.ManyToManyField(WCAG20_SuccessCriterion, related_name='examples', blank=True, null=True)
  order            = models.IntegerField(default=0)
  
  class Meta:
    ordering = ['title',]
    verbose_name        ="Example"
    verbose_name_plural ="Examples"
    
  @models.permalink
  def get_absolute_url(self):
    return ('show_example', [self.example_id])

  @models.permalink
  def get_permanent_url(self):
    return ('show_example_permanent', [self.permanent_slug])

  def save(self):
    if self.title:
      self.title_html       = OAAMarkupToHTML(self.title)
      self.title_text       = OAAMarkupToText(self.title)
      
    if self.description:  
      self.description_html = textile.textile(self.description)
      
    if self.keyboard:  
      self.keyboard_html = textile.textile(self.keyboard)
      
    if self.style:
      self.style_code   = OAAMarkupRemoveHighlightCode(self.style)
      self.style_source = HTMLToSourceCodeFormat(self.style)
      
    if self.html:
      self.html_code   = OAAMarkupRemoveHighlightCode(self.html)
      self.html_source = HTMLToSourceCodeFormat(self.html)

    if self.script:
      self.script_code   = OAAMarkupRemoveHighlightCode(self.script)
      self.script_source = HTMLToSourceCodeFormat(self.script)
      
      
    self.updated_date     = datetime.datetime.now()
    
    #self.rule_categories.clear()
    #self.success_criteria.clear()
    
   # for rr in self.rule_references.all():
    #  self.rule_categories.add(rr.rule.rule_category)
    #  self.success_criteria.add(rr.rule.wcag_primary)

    super(Example, self).save() # Call the "real" save() method.  
  
  def __unicode__(self):
      return 'Example : ' + self.title_text 

  def get_example_abbrev(self):
      return 'Example ' + self.example_group.rule_category.abbrev + "." + str(self.example_group.order) + "." + str(self.order)  

  def get_example_status(self):
    for shortp, longp in EXAMPLE_STATUS:
      if shortp == self.status:
        return longp
        
  def get_example_status_as_html(self):
    for shortp, longp in EXAMPLE_STATUS_HTML_CODE:
      if shortp == self.status:
        return longp 
        
  def get_rules_passed_count(self):
      count = 0

      for rr in self.rule_references.all():
        if rr.validation == "pass":
          count += 1
        else:  
          if rr.manual_check == "pass":
            count += 1
          
      return count

  def get_rules_failed_count(self):
      count = 0
      
      for rr in self.rule_references.all():
        if rr.validation == "fail":
          count += 1
        else:  
          if rr.manual_check == "fail":
            count += 1
          
      return count

  def get_admin_url(self):
    number = self.id - 583
    return urlresolvers.reverse('admin:examples_example_change', args=(number,))

class ExampleScriptReference(models.Model):
  script_ref_id = models.AutoField(primary_key=True)  
  example       = models.ForeignKey(Example, related_name='script_refs')
  script        = models.ForeignKey(ExampleScript, related_name='script_refs')

  class Meta:
    ordering = ['example__example_id',]
    verbose_name="Example Script Reference"

class ExampleStyleReference(models.Model):
  style_ref_id  = models.AutoField(primary_key=True)  
  example       = models.ForeignKey(Example, related_name='style_refs')
  style         = models.ForeignKey(ExampleStyle, related_name='style_refs')

  class Meta:
    ordering = ['example__example_id',]
    verbose_name="Example Style Reference"

RULE_REFERENCE_OPTIONS = (
    ('na',   'Not applicable'),
    ('pass', 'Passes rule requirements'),
    ('fail', 'Fails rule requirements'),
)

RULE_REFERENCE_OPTIONS_HTML = (
    ('na',   '<span class="na">n/a</span>'),
    ('pass', '<span class="pass">Pass</span>'),
    ('fail', '<span class="fail">Fail</span>'),
)

class ExampleRuleReference(models.Model):
  reference_id = models.AutoField(primary_key=True)  
  example      = models.ForeignKey(Example,        related_name='rule_references')
  rule         = models.ForeignKey(Rule,           related_name='rule_references')
  techniques   = models.ManyToManyField(Technique, related_name='rule_references')
  validation   = models.CharField(max_length=4,choices=RULE_REFERENCE_OPTIONS,default='na')
  manual_check = models.CharField(max_length=4,choices=RULE_REFERENCE_OPTIONS,default='na')
  note         = models.TextField("Notes on reference (use Textile markup)", null=True,blank=True)
  note_html    = models.TextField(blank=True, null=True)
  
  class Meta:
    ordering = ['example__example_id',]
    verbose_name="Example Rule Reference"

  def save(self):
    self.note_html = textile.textile(self.note)
    super(ExampleRuleReference, self).save() # Call the "real" save() method.
    self.example.success_criteria.add(self.rule.wcag_primary)

  def get_validation_html(self):
    for shortp, longp in RULE_REFERENCE_OPTIONS_HTML:
      if shortp == self.validation:
       return longp  
  
  def get_manual_check_html(self):
    for shortp, longp in RULE_REFERENCE_OPTIONS_HTML:
      if shortp == self.manual_check:
       return longp  
  
  def get_admin_url(self):
    number = self.reference_id
    return urlresolvers.reverse('admin:examples_examplerulereference_change', args=(number,))

EXAMPLE_USER_AGENT_AT = (
    ('jaws14',    'Jaws 14'),
    ('jaws15',    'Jaws 15'),
    ('nvda',      'NVDA'),
    ('vo',        'Voice Over'),
    ('wineye8',   'Window Eyes 8'),
    ('chromevox', 'ChromeVox'),
    ('winmag',    'Windows 8 Magnifier'),
    ('winnar',    'Windows 8 Narrator'),
    ('zt10',      'Zoomtext 10'),
    ('magic12',   'Magic Screen Magnifier 12'),
    ('osxzoom',   'OS X Zoom'),
    ('dragon',    'Dragon Natually Speaking 11'),
)

EXAMPLE_USER_AGENT_BROWSER_AT = (
    ('jaws14',    '<span class="at jaws">Jaws 14</span>'),
    ('jaws15',    '<span class="at jaws">Jaws 15</span>'),
    ('nvda',      '<span class="at nvda">NVDA</span>'),
    ('vo',        '<span class="at vo">Voice Over</span>'),
    ('wineye8',   '<span class="at we">Window Eyes 8</span>'),
    ('chromevox', '<span class="at cvox">ChromeVox</span>'),
    ('winmag',    '<span class="at winmag">Windows Magnifier</span>'),
    ('winnar',    '<span class="at winnar">Windows Narrator</span>'),
    ('zt10',      '<span class="at zt">Zoomtext 10</span>'),
    ('magic12',   '<span class="at magic">Magic Screen Magnifier 12</span>'),
    ('osxzoom',   '<span class="at zoom">OS X Zoom</span>'),
    ('dragon',    '<span class="at dragon">Dragon Natually Speaking 11</span>'),
)


EXAMPLE_USER_AGENT_BROWSER = (
    ('ie9',     'Internet Explorer 9'),
    ('ie10',    'Internet Explorer 10'),
    ('safari6', 'Safari 6.0'),
    ('safari7', 'Safari 7.0'),
    ('ff22',    'Firefox 22'),
    ('ff23',    'Firefox 23'),
    ('ff24',    'Firefox 24'),
    ('chrome',  'Chrome'),
)

EXAMPLE_USER_AGENT_BROWSER_HTML_CODE = (
    ('ie9',     '<span class="browser ie">Internet Explorer 9'),
    ('ie10',    '<span class="browser ie">Internet Explorer 10'),
    ('safari6', '<span class="browser safari">Safari 6.0'),
    ('safari7', '<span class="browser safari">Safari 7.0'),
    ('ff22',    '<span class="browser ff">Firefox 22'),
    ('ff23',    '<span class="browser ff">Firefox 23'),
    ('ff24',    '<span class="browser ff">Firefox 24'),
    ('chrome',  '<span class="browser chrome">Chrome'),
)

EXAMPLE_USER_AGENT_OS = (
    ('win7',   'Microsoft Windows 7'),
    ('win8',   'Microsoft Windows 8'),
    ('osx108', 'Apple OS X 10.8 Mountian Lion'),
    ('osx109', 'Apple OS X 10.9 Mavericks'),
    ('ios6',   'Apple iOS 6'),
    ('ios7',   'Apple iOS 7'),
    ('and42',  'Androide 4.2'),
    ('unix',   'Unix/Linux'),
)

EXAMPLE_USER_AGENT_OS_HTML_CODE = (
    ('win7',   '<span class="os win">Microsoft Windows 7</span>'),
    ('win8',   '<span class="os win">Microsoft Windows 8</span>'),
    ('osx108', '<span class="os osx">Apple OS X 10.8 Mountian Lion</span>'),
    ('osx109', '<span class="os osx">Apple OS X 10.9 Mavericks</span>'),
    ('ios6',   '<span class="os ios">Apple iOS 6</span>'),
    ('ios7',   '<span class="os ios">Apple iOS 7</span>'),
    ('and42',  '<span class="os androide">Androide 4.2</span>'),
    ('unix',   '<span class="os unix">Unix/Linux</span>'),
)

class ExampleUserAgent(models.Model):
  user_agent_id = models.AutoField(primary_key=True)
  name          = models.CharField(max_length=128)
  abbr          = models.CharField(max_length=16)
  at            = models.CharField(max_length=16, choices=EXAMPLE_USER_AGENT_AT)  
  browser       = models.CharField(max_length=16, choices=EXAMPLE_USER_AGENT_BROWSER)  
  os            = models.CharField(max_length=16, choices=EXAMPLE_USER_AGENT_OS)  
  show          = models.BooleanField("Show browser in compatibility lists", default=True)

  class Meta:
    ordering = ['os', 'browser', 'at', 'name']
    verbose_name        ="User Agent"
    verbose_name_plural ="User Agents"

  def showOS(self):
    for shortp, longp in EXAMPLE_USER_AGENT_OS:
      if shortp == self.os:
        return longp
        
  def showOSAsHTML(self):
    for shortp, longp in EXAMPLE_USER_AGENT_OS_HTML_CODE:
      if shortp == self.os:
        return longp        

  def showAT(self):
    for shortp, longp in EXAMPLE_USER_AGENT_AT:
      if shortp == self.at:
        return longp
        
  def showATAsHTML(self):
    for shortp, longp in EXAMPLE_USER_AGENT_AT_HTML_CODE:
      if shortp == self.at:
        return longp        

  def showBrowser(self):
    for shortp, longp in EXAMPLE_USER_AGENT_BROWSER:
      if shortp == self.browser:
        return longp
        
  def showBrowserAsHTML(self):
    for shortp, longp in EXAMPLE_USER_AGENT_BROWSER_HTML_CODE:
      if shortp == self.browser:
        return longp        
  
  
  
  def __unicode__(self):
      return str(self.os) + ': ' + str(self.name) + " " + str(self.version)




EXAMPLE_COMPATIBILITY_RESULT = (
    ('c',  'Complete'),
    ('ps', 'Partial Support'),
    ('ns', 'Not Supported'),
    ('u',  'Untested'),
)

EXAMPLE_COMPATIBILITY_RESULT_HTML_CODE = (
    ('c',  '<span class="c"><abbr title="Complete">C</abbr></span>'),
    ('ps', '<span class="p"><abbr title="Partial Support">PS</abbr></span>'),
    ('ns',  '<span class="n"><abbr title="No Support">NS</abbr></span>'),
    ('u',  '<span class="u"><abbr title="Untested">U</abbr></span>'),
)

class ExampleCompatibility(models.Model):
  impl_id     = models.AutoField(primary_key=True)
  user_agent  = models.ForeignKey(ExampleUserAgent, related_name="compatibilities")
  example     = models.ForeignKey(Example, related_name="compatibilities")
  notes       = models.TextField(null=True,blank=True)
  notes_html  = models.TextField(default="")
  result      = models.CharField(max_length=4,choices=EXAMPLE_COMPATIBILITY_RESULT,default="u")  

  class Meta: 
    ordering = ['result', 'example', 'user_agent',]
    verbose_name        ="Example Compatibility"
    verbose_name_plural ="Example Compatibilities"

  def get_compatibility_result(self):
    for shortp, longp in EXAMPLE_COMPATIBILITY_RESULT:
      if shortp == self.result:
        return longp
        
  def get_compatibility_result_as_html(self):
    for shortp, longp in EXAMPLE_COMPATIBILITY_RESULT_HTML_CODE:
      if shortp == self.result:
        return longp        
        
  def get_compatibility_result_as_html_list(self):
    html = "<li>" + user_agent.abbr + "(" + self.get_compatibility_result_as_html() + ")</li>"
    return html
  
  def __unicode__(self):
      return str(self.example) + ' with ' + str(self.user_agent) + ' (' + self.get_compatibility_result + ')'  

