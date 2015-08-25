from django.core.urlresolvers import reverse

from rules.models    import Rule
from examples.models import Example
from rulesets.models import Ruleset
from markup.models   import LanguageSpec
from abouts.models   import About
   
class NavMainInfo:

   def __init__(self):
     self.last_rule            = ""
     self.last_example         = ""
     
     self.ruleset_summary_url  = ""
     self.rules_summary_url    = ""
     self.examples_summary_url = ""
   
def nav_main_information(request):

    nav_main_info = NavMainInfo()
 
    try:
      nav_main_info.rulesets_url = request.session['oaa_main_rulesets_url']
    except:
      nav_main_info.rulesets_url = reverse('show_rulesets') 

    try:
      nav_main_info.examples_url = request.session['oaa_main_examples_url']
    except:
      nav_main_info.examples_url = reverse('show_examples') 
       
    try:
      nav_main_info.markup_url = request.session['oaa_main_markup_url']
    except:
      nav_main_info.markup_url = reverse('show_markup', args=('html4',)) 
       
    try:
      nav_main_info.tools_url = request.session['oaa_main_tools_url']
    except:
      nav_main_info.tools_url = reverse('show_tool', args=('ai_firebug',)) 
       
    try:
      nav_main_info.abouts_url = request.session['oaa_main_abouts_url']
    except:
      nav_main_info.abouts_url = reverse('show_about', args=('purpose',)) 
       
    return { 'nav_main' : nav_main_info, }
    
