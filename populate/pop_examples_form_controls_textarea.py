"""This textarea is for populating the database with projects,  users,  etc whenever
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
example_info.title       = "@textarea@ labelling techniques"
example_info.permanent_slug = 'textArea1'

example_info.description = """

h3. Basic labeling techniques

These labeling techniques when used properly should have the same visible and assistive technology labels the same. These techniques only make the assistive technology label the same, if the labelling element is placed close by.
When labels are the same users of assistive technology and people using the screen text can more easily collaborate and share information about the form.

* Use a @label@ element with a @for@ attribute that references a @textarea@'s @id@ attribute. 
* Use a @label@ element which encapsulates a @textarea@, and references the textarea with its textarea content.
* Have the @textarea@ reference another element on the screen using an @aria-labelledby@ attribute.

h3. Other labeling techniques

The following labeling techniques do NOT affect the text appearing near the textarea element, which potentially results in the visible label and the label used by assistive technology to be different.
When labels are different this is potentially confusing to people helping users of assistive technology trying to learn the functions of a web form.

* @aria-label@ attribute, labels the textarea element.
* @title@ attribute, should be used cautiously since the @title@ attribute is also used to generate a tooltip in many browsers 
"""
example_info.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='textarea', attribute='')

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T1", "", "")
rr2 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "CONTROL_1_T2", "CONTROL_1_T3")
rr3 = rule_reference_object("CONTROL_6", "pass", "na", "CONTROL_6_T1", "", "")

example_info.rule_references = [rr1]

example_info.html        = """
<form>
  <label <HL1>for="<HL2>textarea1</HL2>"</HL1>>This element labels the textarea element below using the label for attribute </label>
  <textarea id="textarea1"></textarea>
  <HL1><label><HL2>This element labels the textarea element below using encapsulation.</HL2> 
    <textarea id="textarea2"></textarea>
  </label></HL1>
  <label id="label3">This element labels the textarea element below using aria-labelledby.</label>
  <textarea <HL1>aria-labelledby="<HL2>label3</HL2>"</HL1> id="textarea3"></textarea>
  <label id="label4">The element below is referenced by an aria-label attribute and not by this label.</label>
  <textarea id="textarea4" <HL1>aria-label="<HL2>textarea4</HL2>"</HL1>></textarea>
  <label id="label5">The element below is referenced by an title attribute and not by this label.</label>
  <textarea id="textarea5" <HL1>title="<HL2>textarea5</HL2>"</HL1>></textarea>
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

#example_html textarea
{
  display: block;
  margin-bottom: .25em;
  margin-top: .25em;
}  
"""

example1 = create_example(example_info)

ExampleGroup.objects.get(slug='labeling').examples.add(example1)
