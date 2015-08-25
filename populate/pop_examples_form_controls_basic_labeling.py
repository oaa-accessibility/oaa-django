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

order = 1
eg_labeling = ExampleGroup.objects.get(slug="labeling")


example_info                = example_object()
example_info.title          = order
example_info.example_groups = [eg_labeling]
example_info.title          = "@button@ Element Labeling Techniques"
example_info.permanent_slug = ''

example_info.description = """

h3. Basic labeling techniques

These labeling techniques affect the text appearing on the button, which makes the button visible and assistive technology labels the same.
When labels are the same users of assistive technology and people using the screen text can more easily collaborate and share information about the form.

* The button element has the default label of "button"
* Using the default text attribute you can make the label of the button more descriptive of what is being submitted (i.e. 'Purchase Now') 
* Value cannot be used to label a @button@ element

h3. Other labeling techniques

The following labeling techniques do NOT affect the text appearing on the button, which potentially results in the visible label and the label used by assistive technology being different.
When labels are different this is potentially confusing to people helping users of assistive technology trying to learn the functions of a web form.

* @aria-label@ attribute, similar to using @title@ attribute, but does not affect the visual label for the button
* @aria-labelledby@ attribute, allows other text content on the page to be used to generate a label for the button, does not affect the text shown on the button.
* @title@ attribute, should be used cautiously since the @title@ attribute is also used to generate a tooltip in many browsers 
"""
example_info.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='button', attribute='')

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_4", "pass", "na", "CONTROL_4_T1", "", "")
rr2 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "", "")
rr3 = rule_reference_object("CONTROL_5", "pass", "na", "CONTROL_5_T1", "", "")

example_info.rule_references = [rr1,rr2,rr3]

example_info.html        = """
<div class="button">
     <button value="Submit Query" onclick="alert('Label: Submit')"><HL1>Press button</HL1></button>
</div>
 
<div class="button">
     <button <HL1>value="Purchase Now!"</HL1>onclick="alert('Label: Purchase Now!')">Purchase now</button>
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
       <td><button id="id_button_1"   aria-labelledby="id_item_1 id_button_1" onclick="alert('Label: item #1 description add to cart')">add to cart</button></td>
     </tr>
     <tr>
       <td id="id_item_2">item #2 description</td>
       <td><button id="id_button_2"   aria-labelledby="id_item_2 id_button_2" onclick="alert('Label: item #2 description add to cart')">add to cart</button></td>
     </tr>
     <tr>
       <td id="id_item_3">item #2 description</td>
       <td><button id="id_button_3"   aria-labelledby="id_item_3 id_button_3" onclick="alert('Label: item #3 description add to cart')">add to cart</button></td>
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
       <td><button  title="Purchase item #1" onclick="alert('Label: Purchase item #1')"/>add to cart</button></td>
     </tr>
     <tr>
       <td>item #2 description</td>
       <td><button  title="Purchase item #2" onclick="alert('Label: Purchase item #2')"/>add to cart</button></td>
     </tr>
     <tr>
       <td>item #3 description</td>
       <td><button  title="Purchase item #3" onclick="alert('Label: Purchase item #3')"/>add to cart</button></td>
     </tr>
   </table>
</div>
"""

example_info.script      = """"""

example_info.style       = """
   <style type="text/css">

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
  </style>
"""

example1 = create_example(example_info)


# =============================
# Example 2
# =============================

order = order + 1

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_labeling]
example_info.title          = "Grouping Label: Grouping label missing"
example_info.permanent_slug = ''

example_info.description = """
* Input controls use @label@ element to create an accessible names for each control
* Input controls share the same @label@ text content with other controls on the same page so have the same accessible name
* People using screen readers will not easily be able to identufy the shipping versus the billing controls since the controls share the same accessible name
* To make this example accessible other labeling techniques need to be used, such @fieldset/legend@, @aria-labelledby@ or @aria-label@
"""
example_info.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='text')
m2 = ElementDefinition.objects.get(spec=spec_html4, element='label')

example_info.markup = [m1, m2]

rr1 = rule_reference_object("CONTROL_10", "fail", "na",   "",             "", "")
rr2 = rule_reference_object("CONTROL_12", "na",   "fail", "",             "", "")
rr3 = rule_reference_object("CONTROL_6",  "pass", "na",   "CONTROL_6_T1", "", "")
rr4 = rule_reference_object("CONTROL_7",  "pass", "na",   "CONTROL_7_T1", "", "")

example_info.rule_references = [rr1, rr2, rr3, rr4]

example_info.html        = """

<h3>Shipping and Bill Addresses</h3>
<form>

  <div class="group">

    <div class="legend">Shipping Address</div>
  
    <div class="text">
      <label for="name1">Name</label>
      <input type="text" id="name1" size="30"/>
    </div>
    
    <div class="text">
      <label for="address1">Address</label>
      <input type="text" id="address1" size="30"/>
    </div>
    
    <div class="text">
      <label for="city1">City</label>
      <input type="text" id="city1" size="30"/>
    </div>
    
    <div class="text">
      <label for="state1">State</label>
      <input type="text" id="state1" size="12"/>
    </div>
    
    <div class="text">
       <label for="zip1">Zip</label>
       <input type="text" id="zip1" size="12"/>
    </div>
    
  </div>

  <div class="group">

    <div class="legend">Billing Address</div>
  
    <div class="text">
      <label for="name2">Name</label>
          <input type="text" id="name2" size="30"/>
    </div>
      
    <div class="text">
      <label for="address2">Address</label>
      <input type="textinput" id="address2" size="30"/>
    </div>
        
    <div class="text">
      <label for="city2">City</label>
      <input type="text" id="city2" size="30"/>
    </div>
        
    <div class="text">
      <label for="state2">State</label>
      <input type="text" id="state2" size="12"/>
    </div>
       
    <div class="text">
      <label for="zip2">Zip</label>
      <input type="text" id="zip2" size="12"/>
    </div>
        
  </div>
    
</form> 
"""

example_info.script      = """"""

example_info.style       = """
div.group { 
  padding: .75em; 
} 

legend, 
div.group div.legend { 
  font-weight: bold; 
} 

div.text label, 
div.text div 
{ 
  margin-top: .5em; 
  display: block; 
  width: 8em; 
} 
"""

create_example(example_info)
 
# =============================
# Example 3
# =============================

order = order + 1

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_labeling]
example_info.title          = "Grouping Label: @fieldset/legend@ elements"
example_info.permanent_slug = ''

example_info.description = """
* Input controls use @label@ element to create an accessible names for each control
* Input controls share the same @label@ text content with other controls on the same page so have the same accessible name
* The accessible names for the input controls are made unique using @fieldset/legend@ elements
"""
example_info.keyboard    = """
"""

m3 = ElementDefinition.objects.get(spec=spec_html4, element='legend')

example_info.markup = [m1, m2, m3]

rr1 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T1", "", "")
rr2 = rule_reference_object("CONTROL_12", "na", "pass", "CONTROL_12_T1", "", "")
rr3 = rule_reference_object("CONTROL_6", "pass", "na", "CONTROL_6_T1", "", "")
rr4 = rule_reference_object("CONTROL_7", "pass", "na", "CONTROL_7_T1", "", "")

example_info.rule_references = [rr1, rr2, rr3, rr4]

example_info.html        = """
<h3>Shipping and Bill Addresses</h3>
<form>
  <HL1><fieldset></HL1>  
    <HL1><legend></HL1>Shipping Address<HL1></legend></HL1>
    <div class="text">
      <label for="name1">Name</label>
      <input type="text" id="name1" size="30"/>
    </div>
    
    <div class="text">
      <label for="address1">Address</label>
      <input type="text" id="address1" size="30"/>
    </div>
    
    <div class="text">
      <label for="city1">City</label>
      <input type="text" id="city1" size="30"/>
    </div>
    
    <div class="text">
      <label for="state1">State</label>
      <input type="text" id="state1" size="12"/>
    </div>
    
    <div class="text">
    </div>
       <label for="zip1">Zip</label>
       <input type="text" id="zip1" size="12"/>
  <HL1></fieldset></HL1>

  <HL1><fieldset></HL1>
    <HL1><legend></HL1>Billing Address<HL1></legend></HL1>
    <div class="text">
      <label for="name2">Name</label>
          <input type="text" id="name2" size="30"/>
    </div>
      
    <div class="text">
      <label for="address2">Address</label>
      <input type="text" id="address2" size="30"/>
    </div>
        
    <div class="text">
      <label for="city2">City</label>
      <input type="text" id="city2" size="30"/>
    </div>
        
    <div class="text">
      <label for="state2">State</label>
      <input type="text" id="state2" size="12"/>
    </div>
       
    <div class="text">
      <label for="zip2">Zip</label>
      <input type="text" id="zip2" size="12"/>
    </div>
    
  <HL1></fieldset></HL1>
    
</form> 
"""

example_info.script      = """"""

example_info.style       = """
div.text label, 
div.text div 
{ 
  margin-top: .5em; 
  display: block; 
  width: 8em; 
} 

fieldset {
  margin-bottom: 1em;
}
"""

create_example(example_info)

# =============================
# Example 3
# =============================

example_info               = example_object()
example_info.example_groups= [eg_labeling]
example_info.title         = "Grouping Label: @aria-labelledby@ attribute"
example_info.permanent_slug = ''

example_info.description = """
* Input controls use @aria-labelledby@ attribute to create an accessible names for each control
* The accessible names for the input controls are made unique by referencing both the group and input text 
"""
example_info.keyboard    = """
"""

example_info.markup = [m1, m2]

rr1 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T3", "", "")
rr2 = rule_reference_object("CONTROL_12", "na", "pass", "CONTROL_12_T3", "", "")

example_info.rule_references = [rr1, rr2]

example_info.html        = """
<h3>Shipping and Bill Addresses</h3>
<form>
  <div class="group">
  
    <label <HL1>id="<HL2>sa_label</HL2>"</HL1> class="legend">Shipping Address</label>
    
    <div class="text">
      <label id="name1_label">Name</label>
      <input <HL1>aria-labelledby="<HL2>name1_label sa_label</HL2>"</HL1> type="text" id="name1" size="30"/>
    </div>
    
    <div class="text">
      <label id="address1_label">Address</label>
      <input <HL1>aria-labelledby="<HL2>address1_label sa_label</HL2>"</HL1> type="text" id="address1" size="30"/>
    </div>
    
    <div class="text">
      <label id="city1_label">City</label>
      <input <HL1>aria-labelledby="<HL2>city1_label sa_label</HL2>"</HL1> type="text" id="city1" size="30"/>
    </div>
    
    <div class="text">
      <label id="state1_label">State</label>
      <input <HL1>aria-labelledby="<HL2>state1_label sa_label</HL2>"</HL1> type="text" id="state1" size="12"/>
    </div>
    
    <div class="text">
       <label id="zip1_label">Zip</label>
       <input <HL1>aria-labelledby="<HL2>zip1_label sa_label</HL2>"</HL1> type="text" id="zip1" size="12"/>
    </div>
    
  </div>

  <div class="group">
  
    <label <HL1>id="<HL2>ba_label</HL2>"</HL1> class="legend">Billing Address</label>
    
    <div class="text">
      <label id="name2_label">Name</label>
      <input <HL1>aria-labelledby="<HL2>name2_label ba_label</HL2>"</HL1> type="text" id="name2" size="30"/>
    </div>
      
    <div class="text">
      <label id="address2_label">Address</label>
      <input <HL1>aria-labelledby="<HL2>address2_label ba_label</HL2>"</HL1> type="text" id="address2" size="30"/>
    </div>
        
    <div class="text">
      <label id="city2_label">City</label>
      <input <HL1>aria-labelledby="<HL2>city2_label ba_label</HL2>"</HL1> type="text" id="city2" size="30"/>
    </div>
        
    <div class="text">
      <label id="state2_label">State</label>
      <input <HL1>aria-labelledby="<HL2>state2_label ba_label</HL2>"</HL1> type="text" id="state2" size="12"/>
    </div>
       
    <div class="text">
      <label id="zip2_label">Zip</label>
      <input <HL1>aria-labelledby="<HL2>zip2_label ba_label</HL2>"</HL1> type="text" id="zip2" size="12"/>
    </div>
        
  </div>
  
</form> 
"""

example_info.script      = """"""

example_info.style       = """
div.group { 
  border: black thin solid; 
  padding: .75em; 
  margin-bottom: 1em;
} 

legend, 
div.group div.legend { 
  font-weight: bold; 
} 

div.text label, 
div.text div 
{ 
  margin-top: .5em; 
  display: block; 
  width: 8em; 
} 
"""

create_example(example_info)
