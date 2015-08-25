"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

import sys,os
sys.path.append(os.path.abspath('..'))

from django.core.management import setup_environ 
import coding.settings as settings
setup_environ(settings)

from django.core.exceptions import ObjectDoesNotExist
from markup.models import LanguageSpec, ElementDefinition
from pop_examples_common import *
from examples.models import ExampleGroup




# =============================
# Example 1
# =============================

order = 1
eg_focus = ExampleGroup.objects.get(slug="focus")

example_info               = example_object()
example_info.order         = order
example_info.example_groups= [eg_focus]
example_info.title         = 'Highlighting keyboard focus using css'
example_info.permanent_slug = ''

example_info.description = """
* Use CSS @:focus@, @:active@ and @:hover@ to highlight focus on an input button.
"""
example_info.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_css21, element='border-color')
m2 = ElementDefinition.objects.get(spec=spec_css21, element='background')
m3 = ElementDefinition.objects.get(spec=spec_css21, element=':focus')

example_info.markup = [m1,m2,m3]

example_info.html        = """
 <div class="button">
    <input type="button" value="Press me" onclick='alert("You pressed me!")'/>
</div>

<div class="button">
     <input type="submit" onclick='alert("You pressed me!")'/>
</div>

<div class="button">  
    <button onclick='alert("You pressed me!")'>Example Button</button>
</div> 
"""

example_info.script      = """" """

example_info.style       = """
   <style type="text/css">
div.button {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: .5em;
  font-size: 100%;
  font-weight: bold;
}

div.button button:focus,
div.button button:active,
div.button input:active,
div.button input:focus {
  border-color: black;
  border-style: solid;
  background: yellow;
}

div.button button:hover,
div.button input:hover {
  border-color: black;
  border-style: solid;
}
  </style>
"""

create_example(example_info)

