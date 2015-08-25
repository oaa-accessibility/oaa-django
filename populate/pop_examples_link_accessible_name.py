"""This select is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

import sys,os
sys.path.append(os.path.abspath('..'))

from django.core.management import setup_environ 
import coding.settings as settings
setup_environ(settings)

from django.core.exceptions import ObjectDoesNotExist
from markup.models import LanguageSpec, ElementDefinition
from pop_examples_common import *


# =============================
# Example 1
# =============================
eg_links = ExampleGroup.objects.get(slug="links")

example_info1             = example_object()
example_info1.example_groups = [eg_links]
example_info1.title       = "@link@ accessible naming techniques"
example_info1.permanent_slug = 'link6'

example_info1.description = """

h3. Basic accessible naming techniques

These accessible naming techniques when used properly should have the same visible and assistive technology acessible names the same.
When accessible names are the same users of assistive technology and people using the screen text can more easily collaborate and share information about the form.

* Use the child text element of a link element. 

h3. Other accessible naming techniques

The following accessible naming techniques do NOT affect the text appearing in the link element. Possibly leading to differing accessible name for Visible and assistive technologies.
When accessible names are different this is potentially confusing to people helping users of assistive technology trying to learn the functions of a web form.

*  @aria-label@ attribute
*  @aria-labelledby@ attribute, must reference another element.
*  @title@ attribute, should be used cautiously since the @title@ attribute is also used to generate a tooltip in many browsers
* encapsulated image element @alt@ attribute, makes the accessible name for the link the same as the images @alt@ attribute
"""
example_info1.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='a', attribute='href')

example_info1.markup = [m1]

rr1 = rule_reference_object("LINK_1", "pass", "na", "LINK_1_T1", "", "")
rr2 = rule_reference_object("LINK_2", "pass", "na", "LINK_2_T1", "", "")
rr3 = rule_reference_object("LINK_3", "pass", "na", "LINK_3_T1", "", "")
rr4 = rule_reference_object("LINK_4", "na", "pass", "LINK_4_T1", "", "")

example_info1.rule_references = [rr1, rr2, rr3, rr4]

example_info1.html        = """
  <h3>The accessible name of the link below is determind by child text content.</h3>
  <HL1><a class="exampleLink" href=""><HL2>Link 1</HL2></a></HL1>
  <h3>The accessible name of the link below is determind by its aria-label attribute.</h3>
  <a class="exampleLink" href="" <HL1>aria-label="<HL2>Link 2</HL2>"</HL1>>Link 2</a>
  <h3>The accessible name of the link below is determind by its aria-labelledby attribute. The aria-labelled by references a hidden div element.</h3>
  <div hidden <HL1>id="<HL2>div-aria</HL2>"</HL1>>Link 3</div> <a class="exampleLink" href="" <HL1>aria-labelledby="<HL2>div-aria</HL2>"</HL1>>Link 3</a>
  <h3>The link below encapsulates an image and its accessible name is determined by that images alt.</h3>
  <a class="exampleLink" href=""><img src="http://photography.naturestocklibrary.com/orca-stock-photo.jpg" <HL1>alt="<HL2>Link 4</HL2>"</HL1>/></a>
  <h3>The accessible name of the link below is determined by its title attribute.</h3>
  <a class="exampleLink" href="" <HL1>title="<HL2>Link 5</HL2>"</HL1>>Link 5</a>
"""

example_info1.script      = """"""



example_info1.style       = """

#example_html {
  background-color: #FFFFFF;
}

#example_html a.exampleLink
{
  margin-bottom: .25em;
  margin-top: 1em;
  color: blue;
  text-decoration: underline;
}  
"""

example1 = create_example(example_info1)
ExampleGroup.objects.get(slug='links').examples.add(example1)
