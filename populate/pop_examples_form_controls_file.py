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
example_info1.title       = '@input[type=file]@ - No labels on file fields'
example_info1.permanent_slug = ''

example_info1.description = """
* Form controls without @labels@ are inaccessible!
"""
example_info1.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='file')

example_info1.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "fail", "na", "", "", "")

example_info1.rule_references = [rr1]

example_info1.html        = """
 <div class="text">
    <div class="label">Up load file</div>
    <input type="file" name="name" />
</div>
"""

example_info1.script      = """"""

example_info1.style       = """
   <style type="text/css">
div.file div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
}

div.file input,
div.file textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: 1.25em;
}

  </style>
"""

example1 = create_example(example_info1)

# =============================
# Example 2
# =============================

example_info2             = example_object()
example_info1.title       = '@input[type=file]@ - Label using @label@ element encapsulating file fields'
example_info2.permanent_slug = ''

example_info2.description = """
* Text form controls where the @label@ element encapsulates the text box.
* Encapsulation is a poor accessibility practice since some screen readers read both the label content and the text content of the text box when the text box gets focus. This can be confusing to screen reader users since they cannot distinguish between the label and the content of the text control.
"""
example_info2.keyboard    = """
"""

example_info2.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T2", "", "")

example_info2.rule_references = [rr1]

example_info2.html        = """
<div class="file">
    <HL1><label></HL1><HL2>Up load file</HL2><br/>
    <input type="file" name="name" />
    <HL1></label></HL1>
</div> 
"""

example_info2.script      = """"""

example_info2.style       = """

  <style type="text/css">
div.file label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
  margin-bottom: 1.25em;
}

div.file input {
  margin: 0;
  padding: 0;
}
  </style>
"""

example2 = create_example(example_info2)

# =============================
# Example 3
# =============================

example_info3             = example_object()
example_info3.title       = '@input[type=file]@ - Labeling file fields using @title@ attribute'
example_info3.permanent_slug = ''

example_info3.description = """
* Text form controls using the title attribute to label the text box.
* This is a poor practice since it is not part of the HTML specifications to use title attribute to label form controls.
* The title attribute is used by some developers to improve accessibility since many screen readers will use the attribute if label element markup is not found.
* Using the title attribute to label form controls is usefule in some limited cases where hidden labeling techniques cannot be used in high density forms layed out in tables.
"""
example_info3.keyboard    = """
"""
example_info3.markup = [m1]

rr3 = rule_reference_object("CONTROL_1", "pass", "na", "", "", "")

example_info3.rule_references = [rr3]

example_info3.html        = """
<div class="file">
    <div class="label">Up load file</div>
    <input type="file" name="name" <HL1>title</HL1>="<HL2>Up load file</HL2>"/>
</div> 
"""

example_info3.script      = """"""

example_info3.style       = """
   <style type="text/css">
div.file div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
}

div.file input,
div.file textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: 1.25em;
}

  </style>
"""

example3 = create_example(example_info3)

# =============================
# Example 4


# =============================

example_info4             = example_object()
example_info4.title       = '@input[type=file]@ - Labeling using @label@ element and @for@ attribute to reference file fields'
example_info4.permanent_slug = ''

example_info4.description = """
* Text box form controls are labeled using the @label@ element, the @label.for@ attribute and the @input.id@ attribute.
* The @input.id@ attribute values on form controls need to be unique within the web page (Note: all id attribute values need to be unique for a eb page to validate).
* CSS is used to align labels above the text boxes and to provide vertical separation between the text boxes.
"""

example_info4.keyboard    = """
"""

example_info4.markup = [m1]

rr4 = rule_reference_object("CONTROL_1", "pass", "pass", "CONTROL_1_T1", "", "")

example_info4.rule_references = [rr4]

example_info4.html        = """
 <div class="file">
    <label <HL1>for</HL1>="<HL2>file</HL2>">Up load file</label>
    <input type="file" size="30" name="name" <HL1>id</HL1>="<HL2>file</HL2>"/>
</div>   
"""

example_info4.script      = """"""

example_info4.style       = """
  <style type="text/css">
div.select label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
  font-weight: bold;
  display: block;
}

div.select select  {
  margin: 0;
  padding: 0;
  display: block;
  margin-left: 20px;
  }

  </style>
"""

example4 = create_example(example_info4)

# =============================
# Example 5
# =============================

example_info5             = example_object()
example_info5.title       = '@input[type=file]@ - highlighting file fields when it receives keyboard focus'
example_info5.permanent_slug = ''

example_info5.description = """
* CSS styling of input to make it easier to identify when control has focus and so it scales better when zooming.
* CSS @font-size@ property with the value of 100% to support zooming. 
* CSS @background-color@ property on the CSS pseudo properties @:focus@ and @:active.to@ set background color of control when it receives keyboard focus.
* CSS @background-color@ property on the CSS pseudo property @:hover@ to mimic the styling effects of keyboard focus.
"""
example_info5.keyboard    = """
"""

m2 = ElementDefinition.objects.get(spec=spec_css21, element='background')
m3 = ElementDefinition.objects.get(spec=spec_css21, element='border-color')

example_info5.markup = [m1, m2, m3]

rr5 = rule_reference_object("CONTROL_1", "pass", "pass", "", "", "")

example_info5.rule_references = [rr5]

example_info5.html        = """
 <div class="file">
    <label for="file">Up load file</label>
    <input type="file" size="30" name="name" id="file"/>
</div>    
"""

example_info5.script      = """
  <style type="text/css">
div.file label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
}

div.file input {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: .5em;
  display: block;
  outline:transparent thin solid;
  font-size: 100%;
}


div.file input:active,
div.file input:focus,
{
  outline-color: black;
  background-color: yellow;
}

div.file input:hover {
  outline-color: black;
}

  </style>
"""

example_info5.style       = """
  <style type="text/css">
div.select {
  margin: 0;
  margin-left: 20px;
  padding: .25em;;
  border: thin solid transparent;
  width: 10em;
}


div.focus,
div.select:hover {
  border: thin solid gray;
  background-color: lightyellow;
}


div.select label {
  margin: 0;
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  display: block;
}

div.select select  {
  margin: 0;
  padding: 0;
  display: block;
  }


div.select select:hover,
div.select select:focus,
div.select select:active {
   background: lightyellow;
   border-color: gray;
}

  </style>
"""

example5 = create_example(example_info5)

