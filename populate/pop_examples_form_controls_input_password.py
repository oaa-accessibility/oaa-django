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


# =============================
# Example 1
# =============================


example_info1             = example_object()
example_info1.title       = "@input[type='password']@ labelling techniques"
example_info1.permanent_slug = ''

example_info1.description = """

h3. Basic labeling techniques

These labeling techniques when used properly should have the same visible and assistive technology labels the same. These techniques only make the assistive technology label the same, if the labelling element is placed close by.
When labels are the same users of assistive technology and people using the screen text can more easily collaborate and share information about the form.

* Use a @label@ element with a @for@ attribute that references a @input[type='password']@'s @id@ attribute. 
* Use a @label@ element which encapsulates a @input[type='password']@, and references the input with its password content.
* Have the @input[type='password']@ reference another element on the screen using an @aria-labelledby@ attribute.

h3. Other labeling techniques

The following labeling techniques do NOT affect the text appearing near the password element, which potentially results in the visible label and the label used by assistive technology to be different.
When labels are different this is potentially confusing to people helping users of assistive technology trying to learn the functions of a web form.

* @aria-label@ attribute, labels the password element.
* @title@ attribute, should be used cautiously since the @title@ attribute is also used to generate a tooltip in many browsers 
"""
example_info1.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='password')

example_info1.markup = [m1]

rr1 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T1", "", "")
rr2 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "CONTROL_1_T2", "CONTROL_1_T3")
rr3 = rule_reference_object("CONTROL_6", "pass", "na", "CONTROL_6_T1", "", "")

example_info1.rule_references = [rr1]

example_info1.html        = """
<form>
  <label <HL1>for="<HL2>password1</HL2>"</HL1>>This element labels the password element below using the label for attribute </label>
  <input type="password" id="password1"/>
  <HL1><label><HL2>This element labels the password element below using encapsulation.</HL2> 
    <input type="password" id="password2"/>
  </label></HL1>
  <label id="label3">This element labels the password element below using aria-labelledby.</label>
  <input type="password" <HL1>aria-labelledby="<HL2>label3</HL2>"</HL1> id="password3"/>
  <label id="label4">The element below is referenced by an aria-label attribute and not by this label.</label>
  <input type="password" id="password4" <HL1>aria-label="<HL2>password4</HL2>"</HL1>/>
  <label id="label5">The element below is referenced by an title attribute and not by this label.</label>
  <input type="password" id="password5" <HL1>title="<HL2>password5</HL2>"</HL1>/>
</form>

"""

example_info1.script      = """"""

example_info1.style       = """
#example_html label
{
  display: block;
  margin-bottom: .25em;
  margin-top: .25em;
}  

#example_html input
{
  display: block;
  margin-bottom: .25em;
  margin-top: .25em;
}  
"""

example1 = create_example(example_info1)

ExampleGroup.objects.get(slug='label_basic').examples.add(example1)
