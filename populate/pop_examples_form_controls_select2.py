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
order = 1

eg_labeling = ExampleGroup.objects.get(slug="aria-live")

example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info.title       = "@select@ labelling techniques"
example_info.permanent_slug = 'select21'

example_info.description = """

h3. Basic labeling techniques

These labeling techniques when used properly should have the same visible and assistive technology labels the same. These techniques only make the assistive technology label the same, if the labelling element is placed close by.
When labels are the same users of assistive technology and people using the screen text can more easily collaborate and share information about the form.

* Use a @label@ element with a @for@ attribute that references a @select@'s @id@ attribute. 
* Use a @label@ element which encapsulates a @select@, and references the select with its select content.
* Have the @select@ reference another element on the screen using an @aria-labelledby@ attribute.

h3. Other labeling techniques

The following labeling techniques do NOT affect the text appearing near the select element, which potentially results in the visible label and the label used by assistive technology to be different.
When labels are different this is potentially confusing to people helping users of assistive technology trying to learn the functions of a web form.

* @aria-label@ attribute, labels the select element.
* @title@ attribute, should be used cautiously since the @title@ attribute is also used to generate a tooltip in many browsers 
"""
example_info.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='select', attribute='')

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T1", "", "")
rr2 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "CONTROL_1_T2", "CONTROL_1_T3")
rr3 = rule_reference_object("CONTROL_6", "pass", "na", "CONTROL_6_T1", "", "")

example_info.rule_references = [rr1]

example_info.html        = """
<form>
  <label <HL1>for="<HL2>select1</HL2>"</HL1>>This element labels the select element below using the label for attribute </label>
  <select id="select1">
    <option>option 1</option>
    <option>option2</option>
  <select>
  <HL1><label><HL2>This element labels the select element below using encapsulation.</HL2> 
    <select id="select2">
      <option>option 1</option>
      <option>option2</option>
      </select>
  </label></HL1>
  <label id="label3">This element labels the select element below using aria-labelledby.</label>
  <select <HL1>aria-labelledby="<HL2>label3</HL2>"</HL1> id="select3">
    <option>option 1</option>
    <option>option2</option>
  </select>
  <label id="label4">The element below is referenced by an aria-label attribute and not by this label.</label>
  <select id="select4" <HL1>aria-label="<HL2>select4</HL2>"</HL1>>
    <option>option 1</option>
    <option>option2</option>
  </select>
  <label id="label5">The element below is referenced by an title attribute and not by this label.</label>
  <select id="select5" <HL1>title="<HL2>select5</HL2>"</HL1>>
    <option>option 1</option>
    <option>option2</option>
  </select>
</form>

"""

example_info.script      = """"""

example_info.style       = """
#example_html label
{
  display: block;
  margin-bottom: .25em;
  margin-top: .25em;
}  

#example_html select
{
  display: block;
  margin-bottom: .25em;
  margin-top: .25em;
}  
"""

example1 = create_example(example_info)

ExampleGroup.objects.get(slug='labeling').examples.add(example1)
