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

example_info1                = example_object()
example_info1.order          = 1
example_info1.example_group  = ExampleGroup.objects.get(slug="labeling")
example_info1.title          = "Grouping Label: Grouping label missing"
example_info1.permanent_slug = ''

example_info1.description = """
* Input controls use @label@ element to create an accessible names for each control
* Input controls share the same @label@ text content with other controls on the same page so have the same accessible name
* People using screen readers will not easily be able to identufy the shipping versus the billing controls since the controls share the same accessible name
* To make this example accessible other labeling techniques need to be used, such @fieldset/legend@, @aria-labelledby@ or @aria-label@
"""
example_info1.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='text')
m2 = ElementDefinition.objects.get(spec=spec_html4, element='label')

example_info1.markup = [m1, m2]

rr1 = rule_reference_object("CONTROL_10", "fail", "na",   "",             "", "")
rr2 = rule_reference_object("CONTROL_12", "na",   "fail", "",             "", "")
rr3 = rule_reference_object("CONTROL_6",  "pass", "na",   "CONTROL_6_T1", "", "")
rr4 = rule_reference_object("CONTROL_7",  "pass", "na",   "CONTROL_7_T1", "", "")

example_info1.rule_references = [rr1, rr2, rr3, rr4]

example_info1.html        = """

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

example_info1.script      = """"""

example_info1.style       = """
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

example1 = create_example(example_info1)
 
# =============================
# Example 2
# =============================

example_info2                = example_object()
example_info2.example_group  = ExampleGroup.objects.get(slug="labeling")
example_info2.title          = "Grouping Label: @fieldset/legend@ elements"
example_info2.permanent_slug = ''

example_info2.description = """
* Input controls use @label@ element to create an accessible names for each control
* Input controls share the same @label@ text content with other controls on the same page so have the same accessible name
* The accessible names for the input controls are made unique using @fieldset/legend@ elements
"""
example_info2.keyboard    = """
"""

m3 = ElementDefinition.objects.get(spec=spec_html4, element='legend')

example_info2.markup = [m1, m2, m3]

rr1 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T1", "", "")
rr2 = rule_reference_object("CONTROL_12", "na", "pass", "CONTROL_12_T1", "", "")
rr3 = rule_reference_object("CONTROL_6", "pass", "na", "CONTROL_6_T1", "", "")
rr4 = rule_reference_object("CONTROL_7", "pass", "na", "CONTROL_7_T1", "", "")

example_info2.rule_references = [rr1, rr2, rr3, rr4]

example_info2.html        = """
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

example_info2.script      = """"""

example_info2.style       = """
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

example2 = create_example(example_info2)

# =============================
# Example 3
# =============================

example_info3               = example_object()
example_info3.example_group = ExampleGroup.objects.get(slug="labeling")
example_info3.title         = "Grouping Label: @aria-labelledby@ attribute"
example_info3.permanent_slug = ''

example_info3.description = """
* Input controls use @aria-labelledby@ attribute to create an accessible names for each control
* The accessible names for the input controls are made unique by referencing both the group and input text 
"""
example_info3.keyboard    = """
"""

example_info3.markup = [m1, m2]

rr1 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T3", "", "")
rr2 = rule_reference_object("CONTROL_12", "na", "pass", "CONTROL_12_T3", "", "")

example_info3.rule_references = [rr1, rr2]

example_info3.html        = """
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

example_info3.script      = """"""

example_info3.style       = """
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

example3 = create_example(example_info3)
