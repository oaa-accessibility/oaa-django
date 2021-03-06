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
example_info1.title       = "@input[type='button']@ labelling techniques"
example_info1.permanent_slug = ''

example_info1.description = """

h3. Basic labeling techniques

These labeling techniques affect the text appearing on the button, which make the visible and assistive technology labels the same.
When labels are the same users of assistive technology and people using the screen text can more easily collaborate and share information about the form.

* The input of type button has the default label of "button"
* Using the @value@ attribute you can make the label of the button more descriptive of what is being submitted (i.e. 'Purchase Now') 
* Using the @value@ attribute you can make the label of the button unique when there is more than one button on the page 

h3. Other labeling techniques

The following labeling techniques do NOT affect the text appearing on the button, which potentially results in the visible label and the label used by assistive technology to be different.
When labels are different this is potentially confusing to people helping users of assistive technology trying to learn the functions of a web form.

* @aria-label@ attribute, similar to using @title@ attribute, but does not affect the visual label for the button
* @aria-labelledby@ attribute, allows other text content on the page to be used to generate a label for the button, does not affect the text shown on the button.
* @title@ attribute, should be used cautiously since the @title@ attribute is also used to generate a tooltip in many browsers 
"""
example_info1.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='button')

example_info1.markup = [m1]

rr1 = rule_reference_object("CONTROL_4", "na", "pass", "CONTROL_4_T1", "", "")
rr2 = rule_reference_object("CONTROL_1", "na", "pass", "CONTROL_1_T1", "", "")
rr3 = rule_reference_object("CONTROL_5", "na", "pass", "CONTROL_5_T1", "", "")

example_info1.rule_references = [rr1,rr2,rr3]

example_info1.html        = """
<div class="button">
     <input <HL1>type="button"</HL1> value="Submit Query" onclick="alert('Label: Submit')"/>
</div>
 
<div class="button">
     <input type="button" <HL1>value="Purchase Now!"</HL1>onclick="alert('Label: Purchase Now!')"/>
</div>

<div class="button">
     <input type="button" value="Submit Query" <HL1>aria-label="Purchase Now!"</HL1>onclick="alert('Label: Purchase Now!')"/>
</div>

<br></br>

<div class="button">
   <table>
     <caption>Purchase Options Example #1</caption>
     <tr>
       <th>Description of Item</th>
       <th>Purchase</th>
     </tr>
     <tr>
       <td id="id_item_1">item #1 description</td>
       <td><input id="id_button_1" type="button" value="add to cart" aria-labelledby="id_item_1 id_button_1" onclick="alert('Label: item #1 description add to cart')"/></td>
     </tr>
     <tr>
       <td id="id_item_2">item #2 description</td>
       <td><input id="id_button_2" type="button" value="add to cart" aria-labelledby="id_item_2 id_button_2" onclick="alert('Label: item #2 description add to cart')"/></td>
     </tr>
     <tr>
       <td id="id_item_3">item #2 description</td>
       <td><input id="id_button_3" type="button" value="add to cart" aria-labelledby="id_item_3 id_button_3" onclick="alert('Label: item #3 description add to cart')"/></td>
     </tr>
   </table>
</div>

<br></br>

<div class="button">
   <table>
     <caption>Purchase Options Example #2</caption>
     <tr>
       <th>Description of Item</th>
       <th>Purchase</th>
     </tr>
     <tr>
       <td>item #1 description</td>
       <td><input type="button" value="add to cart" title="Purchase item #1" onclick="alert('Label: Purchase item #1')"/></td>
     </tr>
     <tr>
       <td>item #2 description</td>
       <td><input type="button" value="add to cart" title="Purchase item #2" onclick="alert('Label: Purchase item #2')"/></td>
     </tr>
     <tr>
       <td>item #3 description</td>
       <td><input type="button" value="add to cart" title="Purchase item #3" onclick="alert('Label: Purchase item #3')"/></td>
     </tr>
   </table>
</div>
"""

example_info1.script      = """"""

example_info1.style       = """

#example_html div.button {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: .5em;
  font-size: 100%;
  font-weight: bold;
}

#example_html  th
{
  border-bottom: thin solid gray;
  margin-right: 10em;
  text-align: left;
  font-size: 90%;
}

#example_html table tr.even
{
  background-color: #EEEEEE;
}

#example_html table caption
{
  text-align: left;
  font-size: 100%;
  margin-top: 1em;
  font-weight: normal;
}  
"""

example1 = create_example(example_info1)

ExampleGroup.objects.get(slug='label_basic').examples.add(example1)
