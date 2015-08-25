import sys,os
sys.path.append(os.path.abspath('..'))

from django.core.management import setup_environ 
import coding.settings as settings
setup_environ(settings)

"""This file is for populating the database with markup information
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from tools.models import Tool
from django.contrib.auth.models import User

editor = User.objects.all()[0]

Tool.objects.all().delete()

def create_tool(slug, title, abbrev, description):
  try:
    tool = Tool.objects.get(tool_slug=slug)
    print "  Updating Tool: " + slug 
    tool.title        = title
    tool.abbrev       = abbrev
    tool.description  = description
    updated_editor     = editor
  except ObjectDoesNotExist:
    print "  Creating Tool: " + slug 
    tool = Tool(tool_slug=slug, title=title, abbrev=abbrev, description=description, updated_editor=editor)
  tool.save()
  return tool

description = """
Description of AInspector Sidebar for Firefox
"""
  
create_tool("ai_sidebar", "AInspector Sidebar for Firefox", "AInspector Sidebar", description)  

description = """
Description of AInspector Extension for Firebug
"""
  
create_tool("ai_firebug", "AInspector Extension for Firebug", "AInspector Firebug", description)  

description = """
Description of Functional Accessibility Evaluator 2.0
"""
  
create_tool("fae20", "Functional Accessibility Evaluation (FAE) 2.0", "FAE 2.0", description)  

