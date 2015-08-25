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
eg_checkbox = ExampleGroup.objects.get(slug="checkbox")
eg_focus    = ExampleGroup.objects.get(slug="focus")

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_checkbox]
example_info.title          = '@input[type=checkbox]@ - No labels on checkboxes'
example_info.permanent_slug = ''

example_info.description = """
* Form controls without @labels@ are inaccessible!
"""
example_info.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='checkbox')

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "fail", "na", "", "", "")

example_info.rule_references = [rr1]

example_info.html        = """
<div class="label">Select pizza toppings</div>
<ul class="checkbox">
    <li><input type="checkbox"  value="pepperoni"/>Pepperoni</li>
    <li><input type="checkbox" value="sausage" />Sausage</li>
    <li><input type="checkbox" value="mushrooms"/>Mushrooms</li>
    <li><input type="checkbox" value="onions"/>Onions</li>
    <li><input type="checkbox" value="gpeppers"/>Green Peppers</li>
    <li><input type="checkbox" value="xcheese"/>Exrtra Cheese</li>
</ul> 
"""

example_info.script      = """"""

example_info.style       = """
   <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
  font-weight: bold;
}

ul.checkbox   {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}
  </style>
"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script2      = ExampleScript.objects.get(script='examples/js/jquery-2.0.2.min.js')
add_script_reference( example1, script2 )

# =============================
# Example 2
# =============================

order +=  1

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_checkbox]
example_info.title          = '@input[type=checkbox]@ - Labeling checkbox using @title@ attribute'
example_info.permanent_slug = ''

example_info.description = """
* Using the @title@ attribute to define @labels@ will work with assistive technologies but is not defined in the @HTML@ specifications
"""
example_info.keyboard    = """
"""

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "", "", "")
rr2 = rule_reference_object("CONTROL_10", "pass", "na", "", "", "")

example_info.rule_references = [rr1, rr2]

example_info.html        = """
<div class="label">Select pizza toppings</div>
<ul class="checkbox">
  <li><input type="checkbox"  value="pepperoni" <HL1>title="<HL2>Pepperoni</HL2>"</HL1>/>Pepperoni</li>
  <li><input type="checkbox" value="sausage"  <HL1>title="<HL2>Sausage</HL2>"</HL1>/>Sausage</li>
  <li><input type="checkbox" value="mushrooms" <HL1>title="<HL2>Mushrooms</HL2>"</HL1>/>Mushrooms</li>
  <li><input type="checkbox" value="onions" <HL1>title="<HL2>Onions</HL2>"</HL1>/>Onions</li>
  <li><input type="checkbox" value="gpeppers" <HL1>title="<HL2>Green Peppers</HL2>"</HL1>/>Green Peppers</li>
  <li><input type="checkbox" value="xcheese" <HL1>title="<HL2>Extra Cheese</HL2>"</HL1>/>Extra Cheese</li>
</ul> 
"""

example_info.script      = """"""

example_info.style       = """
   <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
  font-weight: bold;
}

ul.checkbox   {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}
  </style>
"""

example2 = create_example(example_info)


# =============================
# Example 3
# =============================

order +=  1

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_checkbox]
example_info.title          = '@input[type=checkbox]@ - Labeling using @label@ element encapsulating @input[type=checkbox]@'
example_info.permanent_slug = ''

example_info.description = """
* Encapsulation is compatible with assistive technologies and is defined in HTML specifications.
* @Label@ element content increases the active area for changing the selection
* What makes this a poor practice is the inconsistency with the labeling requirements of other form controls which need to use the @label@ by reference technique.
"""
example_info.keyboard    = """
"""
example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T2", "", "")
rr2 = rule_reference_object("CONTROL_10", "pass", "na", "", "", "")

example_info.rule_references = [rr1, rr2]

example_info.html        = """
 <div class="label">Select pizza toppings</div>
<ul class="checkbox">
  <li><HL1><label></HL1><input type="checkbox"  value="pepperoni"/><HL2>Pepperoni</HL2><HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="sausage" /><HL2>Sausage</HL2><HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="mushrooms"/><HL2>Mushrooms<HL1></HL2></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="onions"/><HL2>Onions</HL2><HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="gpeppers"/><HL2>Green Peppers</HL2><HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="checkbox" value="xcheese"/><HL2>Extra Cheese</HL2><HL1></label></HL1></li>
</ul> 
"""

example_info.script      = """"""

example_info.style       = """
  <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
  font-weight: bold;
}

ul.checkbox   {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}
  </style>
"""

example3 = create_example(example_info)

# =============================
# Example 4
# =============================

order +=  1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_checkbox]
example_info.title       = '@input[type=checkbox]@ - Labeling using @label@ element and @for@ attribute to reference checkbox'
example_info.permanent_slug = ''

example_info.description = """
* The @label@ reference technique is compatible with assistive technologies and is defined in @HTML@ specifications.
* The reference technique is consistent with how other input form controls are labeled and therefore developers only need to use one rule when using the @label@ element .
"""

example_info.keyboard    = """
"""

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "na", "pass", "CONTROL_1_T1", "", "")
rr2 = rule_reference_object("CONTROL_10", "na", "pass", "", "", "")

example_info.rule_references = [rr1, rr2]

example_info.html        = """
<div class="label">Select pizza toppings</div>
<ul class="checkbox">
  <li><input type="checkbox" <HL1>id="<HL2>cb1</HL2>"</HL1> value="pepperoni"/><label <HL1>for="<HL2>cb1</HL2>"</HL1>>Pepperoni<HL1></label></HL1></li>
  <li></HL1><input type="checkbox" <HL1>id="<HL2>cb2</HL2>"</HL1> value="sausage" /><label <HL1>for="<HL2>cb2</HL2>"</HL1>>Sausage<HL1></label></HL1></li>
  <li></HL1><input type="checkbox" <HL1>id="<HL2>cb3</HL2>"</HL1> value="mushrooms"/><label <HL1>for="<HL2>cb3</HL2>"</HL1>>Mushrooms<HL1></label></HL1></li>
  <li></HL1><input type="checkbox" <HL1>id="<HL2>cb4</HL2>"</HL1> value="onions"/><label <HL1>for="<HL2>cb4</HL2>"</HL1>>Onions<HL1></label></HL1></li>
  <li></HL1><input type="checkbox" <HL1>id="<HL2>cb5</HL2>"</HL1> value="gpeppers"/><label <HL1>for="<HL2>cb5</HL2>"</HL1>>Green Peppers<HL1></label></li>
  <li><input type="checkbox" <HL1>id="<HL2>cb6</HL2>"</HL1> value="xcheese"/><<HL1>label for="<HL2>cb6</HL2>"</HL1>>Extra Cheese<HL1></label></HL1></li>
</ul> 
"""

example_info.script      = """"""

example_info.style       = """
   <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
  font-weight: bold;
}

ul.checkbox   {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}
  </style>
"""

example4 = create_example(example_info)

# =============================
# Example 5
# =============================

order +=  1

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_checkbox, eg_focus]
example_info.title          = '@input[type=checkbox]@ - highlighting checkbox when it receives keyboard focus'
example_info.permanent_slug = ''

example_info.description = """
* Use javascripting to update styling of @checkboxes label@ with keyboard focus.
* Include @onFocus@ and @onBlur@ event handlers on input element to update class value of parent @li@.
* Include CSS @:hover@ psuedo element to highlight the active area of the @label@ for selecting a @checkbox@.
"""
example_info.keyboard    = """
"""



spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_css21, element='background')
m2 = ElementDefinition.objects.get(spec=spec_css21, element='border-color')
m3 = ElementDefinition.objects.get(spec=spec_css21, element=':hover')
m4 = ElementDefinition.objects.get(spec=spec_html4, element='label')
m5 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='checkbox')

example_info.markup = [m1, m2, m3, m4, m5]

example_info.html = """
<div class="label">Select pizza toppings</div>
<ul class="checkbox">
  <li><input type="checkbox" id="cb1" value="pepperoni" <HL1>onfocus="parentFocus(event)" onblur="parentBlur(event)"</HL1>/><label for="cb1">Pepperoni</label></li>
  <li><input type="checkbox" id="cb2" value="sausage" <HL1>onfocus="parentFocus(event)" onblur="parentBlur(event)"</HL1>/><label for="cb2">Sausage</label></li>
  <li><input type="checkbox" id="cb3" value="mushrooms" <HL1>onfocus="parentFocus(event)" onblur="parentBlur(event)"</HL1>/><label for="cb3">Mushrooms</label></li>
  <li><input type="checkbox" id="cb4" value="onions" <HL1>onfocus="parentFocus(event)" onblur="parentBlur(event)"</HL1>/><label for="cb4">Onions</label></li>
  <li><input type="checkbox" id="cb5" value="gpeppers" <HL1>onfocus="parentFocus(event)" onblur="parentBlur(event)"</HL1>/><label for="cb5">Green Peppers</label></li>
  <li><input type="checkbox" id="cb6" value="xcheese" <HL1>onfocus="parentFocus(event)" onblur="parentBlur(event)"</HL1>/><label for="cb6>">Extra Cheese</label></li>
</ul> 
"""

example_info.script      = """
//   Add focus styling to the parent (LI) element of the radio button receiving focus
//
function parentFocus( event ) {
  // Get event object  if using Internet Explorer
  var e = event || window.event;
  
  // Check the object for W3C DOM event object, if not use IE event object to update the class of the parent element
  if( e.target )
    e.target.parentNode.className = "focus";
  else
    e.srcElement.parentNode.className = "focus";
  
}

//
//   Remove focus styling from the parent (LI) element of the radio button receiving focus
//
function parentBlur( event ) {
  // Get event object  if using Internet Explorer
  var e = event || window.event;
  
  var node;
  
  // Check the object for W3C DOM event object, if not use IE event object to update the class of the parent element
  if( e.target )
    e.target.parentNode.className = "";
  else
    e.srcElement.parentNode.className = "";

}
  </script>
"""

example_info.style       = """
   <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
  font-weight: bold;
}

ul.checkbox   {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}

<HL1>
ul.checkbox li {
  border: 1px transparent solid;
}

ul.checkbox li:hover,
ul.checkbox li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 10em;
}
</HL1>
  </style>
"""

example5 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example5).delete()
script2      = ExampleScript.objects.get(script='examples/js/jquery-2.0.2.min.js')
add_script_reference( example5, script2 )

# =============================
# Example 6
# =============================

order +=  1

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_checkbox, eg_focus]
example_info.title          = '@input[type=checkbox]@ - highlighting checkbox when it receives keyboard focus using JQUERY'
example_info.permanent_slug = ''

example_info.description = """
* Use javascripting to update styling of @checkboxes label@ with keyboard focus using JQUERY.
* Through scripting add @onFocus@ and @onBlur@ event handlers on @input@ element to update class value of parent @li@.
* Include CSS @:hover@ psuedo element to highlight the active area of the @label@ for selecting a @checkbox@.
"""
example_info.keyboard    = """
"""


example_info.markup = [m1, m2, m3, m4, m5]

example_info.html        = """
 <div class="label">Select pizza toppings</div>
<ul class="checkbox">
  <li><input type="checkbox" id="cb1" value="pepperoni" /><label for="cb1">Pepperoni</label></li>
  <li><input type="checkbox" id="cb2" value="sausage"   /><label for="cb2">Sausage</label></li>
  <li><input type="checkbox" id="cb3" value="mushrooms" /><label for="cb3">Mushrooms</label></li>
  <li><input type="checkbox" id="cb4" value="onions"   /><label for="cb4">Onions</label></li>
  <li><input type="checkbox" id="cb5" value="gpeppers" /><label for="cb5">Green Peppers</label></li>
  <li><input type="checkbox" id="cb6" value="xcheese"  /><label for="cb6>">Extra Cheese</label></li>
</ul>
"""

example_info.script      = """
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('ul.checkbox li input').focusin( function() {
    $(this).parent().addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('ul.checkbox li input').focusout( function() {
    $(this).parent().removeClass('focus');
  }
  );

}
);
"""

example_info.style       = """
  <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
  font-weight: bold;
}

ul.checkbox   {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}

<HL1>
ul.checkbox li {
  border: 1px transparent solid;
}

ul.checkbox li:hover,
ul.checkbox li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 10em;
}
</HL1>
  </style>
"""

example6 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example6).delete()
script2      = ExampleScript.objects.get(script='examples/js/jquery-2.0.2.min.js')
add_script_reference( example6, script2 )

# =============================
# Example 7 
# =============================

order +=  1

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_checkbox]
example_info.title          = '@input[type=checkbox]@ - Adding a group label using fieldset/legend elements'
example_info.permanent_slug = ''

example_info.description = """
* fieldset/legend elements are used to bind the group @label@ information to the checkboxes in the group.
* Screen readers read the @legend@ element content when the one of the checkboxes in the group receives keyboard focus.
* One problem with the @legend@ element is the limited browser supporting in restyling the legend element with CSS. Browsers only render legend as a single line, making long legends run off the visible screen or over other page content.
"""
example_info.keyboard    = """
"""

example_info.markup = [m1, m2, m3, m4, m5]

rr1 = rule_reference_object("CONTROL_8", "na", "pass", "CONTROL_8_T1", "", "")
rr2 = rule_reference_object("CONTROL_7", "na", "pass", "CONTROL_7_T1", "", "")
rr3 = rule_reference_object("CONTROL_6", "na", "pass", "CONTROL_6_T1", "", "")

example_info.rule_references = [rr1, rr2, rr3]

example_info.html        = """

<HL1><fieldset class="group"></HL1>
<HL1><legend></HL1><HL2>Select standard pizza toppings</HL2><HL1></legend></HL1>
<ul class="checkbox">
  <li><input type="checkbox" id="cb1" value="pepperoni" /><label for="cb1">Pepperoni</label></li>
  <li><input type="checkbox" id="cb2" value="sausage" /><label for="cb2">Sausage</label></li>
  <li><input type="checkbox" id="cb3" value="mushrooms" /><label for="cb3">Mushrooms</label></li>
  <li><input type="checkbox" id="cb4" value="onions" /><label for="cb4">Onions</label></li>
  <li><input type="checkbox" id="cb5" value="gpeppers" /><label for="cb5">Green Peppers</label></li>
  <li><input type="checkbox" id="cb6" value="xcheese" /><label for="cb6>">Extra Cheese</label></li>
</ul>
<HL1></fieldset></HL1>


<HL1><fieldset class="group"></HL1>
<HL1><legend></HL1><HL2><span class="rem">premium</span> pizza toppings (extra cost)</HL2><HL1></legend></HL1>
<ul class="checkbox">
  <li><input type="checkbox" id="cb7" value="proscuitto" /><label for="cb7">Proscuitto</label></li>
  <li><input type="checkbox" id="cb8" value="portobello" /><label for="cb8">Portobello Mushrooms</label></li>
  <li><input type="checkbox" id="cb9" value="ypeppers" /><label for="cb9">Yellow Peppers</label></li>
  <li><input type="checkbox" id="cb10" value="bcheese" /><label for="cb10">Blue Cheese</label></li>
  <li><input type="checkbox" id="cb11" value="shrimps" /><label for="cb11">Shrimps</label></li>
  <li><input type="checkbox" id="cb12" value="sundried" /><label for="cb12">Sun Dried Tomatoes</label></li>
</ul>
<HL1></fieldset></HL1>
"""

example_info.script      = """
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('ul.checkbox li').focusin( function() {
    $(this).addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('ul.checkbox li').focusout( function() {
    $(this).removeClass('focus');
  }
  );

}
);
"""

example_info.style       = """
   <style type="text/css">

fieldset.group  {
  margin: 0;
  padding: 0;
  margin-bottom: 1.25em;
  padding: .125em;
}

fieldset.group legend {
  margin: 0;
  padding: 0;
  font-weight: bold;
  margin-left: 20px;
  font-size: 100%;
  color: black;
}


ul.checkbox  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}

ul.checkbox li {
  border: 1px transparent solid;
}

ul.checkbox li label {
  margin-left: ;
}
ul.checkbox li:hover,
ul.checkbox li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 12em;
}


  </style>
"""

example7 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example7).delete()
script2      = ExampleScript.objects.get(script='examples/js/jquery-2.0.2.min.js')
add_script_reference( example7, script2 )

# =============================
# Example 8
# =============================

order +=  1

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_checkbox]
example_info.title          = '@input[type=checkbox]@ - Indicating a required control using an @img@ element with an @alt@ attribute set to required'
example_info.permanent_slug = ''

example_info.description = """
* The required image is part of the @legend@ content and the @alt@ attribute content is added to the @legend@ content.
"""

example_info.keyboard    = """
"""


example_info.markup = [m1, m2, m3, m4, m5]

rr1 = rule_reference_object("CONTROL_8", "pass", "na", "CONTROL_8_T1", "", "")
rr2 = rule_reference_object("CONTROL_7", "pass", "na", "CONTROL_7_T1", "", "")
rr3 = rule_reference_object("CONTROL_6", "pass", "na", "CONTROL_6_T1", "", "")
rr4 = rule_reference_object("CONTROL_6", "pass", "na", "CONTROL_1_T1", "", "")


example_info.rule_references = [rr1, rr2, rr3, rr4]

example_info.html        = """
<p class="inst"><img src="images/required.png" alt="required" /> You must select at least one item</p>

<fieldset class="group">
  <legend>Select standard pizza toppings <HL1><img src="images/required.png" alt="<HL2>you must select at least one item</HL2>"</HL1> /></legend>
<ul class="checkbox">
  <li><input type="checkbox" id="cb1" value="cheese" "/><label for="cb1">Cheese</label></li>
  <li><input type="checkbox" id="cb2" value="pepperoni" "/><label for="cb2">Pepperoni</label></li>
  <li><input type="checkbox" id="cb3" value="sausage" /><label for="cb3">Sausage</label></li>
  <li><input type="checkbox" id="cb4" value="mushrooms" /><label for="cb4">Mushrooms</label></li>
  <li><input type="checkbox" id="cb5" value="onions" /><label for="cb5">Onions</label></li>
  <li><input type="checkbox" id="cb6" value="gpeppers" /><label for="cb6">Green Peppers</label></li>
</ul>
</fieldset>

<fieldset class="group">
  <legend>Select <span class="prem">premium</span> pizza toppings (extra cost)</legend>
<ul class="checkbox">
  <li><input type="checkbox" id="cb7" value="proscuitto" /><label for="cb7">Proscuitto</label></li>
  <li><input type="checkbox" id="cb8" value="portobello" /><label for="cb8">Portobello Mushrooms</label></li>
  <li><input type="checkbox" id="cb9" value="ypeppers" /><label for="cb9">Yellow Peppers</label></li>
  <li><input type="checkbox" id="cb10" value="bcheese" /><label for="cb10">Blue Cheese</label></li>
  <li><input type="checkbox" id="cb11" value="shrimps" /><label for="cb11">Shrimps</label></li>
  <li><input type="checkbox" id="cb12" value="sundried" /><label for="cb12">Sun Dried Tomatoes</label></li>
</ul>
</fieldset> 
"""

example_info.script      = """
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('ul.checkbox li').focusin( function() {
    $(this).addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('ul.checkbox li').focusout( function() {
    $(this).removeClass('focus');
  }
  );

}
);
"""

example_info.style       = """
   <style type="text/css">
fieldset.group  {
  margin: 0;
  padding: 0;
  margin-bottom: 1.25em;
  padding: .125em;
  
  border-style:none;

  }

fieldset.group legend {
  margin: 0;
  padding: 0;
  font-weight: bold;
  margin-left: 20px;
  font-size: 100%;
  color: black;

}
ul.checkbox  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.checkbox li input {
  margin-right: .25em;
}

ul.checkbox li {
  border: 1px transparent solid;
}

ul.checkbox li label {
  margin-left: ;
}

ul.checkbox li:hover,
ul.checkbox li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 12em;
}

<HL1>
p.inst {
margin: 0;
  padding: 0;
  margin-bottom: .75em;
  margin-left: 20px;
  font-size: 100%;
  color: black;
}

span.prem {
  font-family:fantasy;
  font-style:italic;
  letter-spacing: .05em;
}
</HL1>
  </style>
"""

example8 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example8).delete()
script2      = ExampleScript.objects.get(script='examples/js/jquery-2.0.2.min.js')
add_script_reference( example8, script2 )
# =============================
# Example 9
# =============================

order +=  1

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_checkbox]
example_info.title          = '@input[type=checkbox]@ - Indicating a required control using text content'
example_info.permanent_slug = ''

example_info.description = """
* The "required" text is just made part of the @legend@ text.
* A @span@ element and CSS are used to style the "required" differently. 
"""
example_info.keyboard    = """
"""


example_info.markup = [m1, m2, m3, m4, m5]

rr1 = rule_reference_object("CONTROL_8", "pass", "na", "CONTROL_8_T1", "", "")
rr2 = rule_reference_object("CONTROL_7", "pass", "na", "CONTROL_7_T1", "", "")
rr3 = rule_reference_object("CONTROL_6", "pass", "na", "CONTROL_6_T1", "", "")
rr4 = rule_reference_object("CONTROL_6", "pass", "na", "CONTROL_1_T1", "", "")


example_info.rule_references = [rr1, rr2, rr3, rr4]

example_info.html        = """
<HL1><p class="inst"></HL1><img src="images/required.png" alt="required" /><HL2>You must select at least one item</HL2></p>

<fieldset class="group">
  <legend>Select standard pizza toppings <img src="images/required.png" alt="you must select at least one item" /></legend>
<ul class="checkbox">
  <li><input type="checkbox" id="cb1" value="cheese" "/><label for="cb1">Cheese</label></li>
  <li><input type="checkbox" id="cb2" value="pepperoni" "/><label for="cb2">Pepperoni</label></li>
  <li><input type="checkbox" id="cb3" value="sausage" /><label for="cb3">Sausage</label></li>
  <li><input type="checkbox" id="cb4" value="mushrooms" /><label for="cb4">Mushrooms</label></li>
  <li><input type="checkbox" id="cb5" value="onions" /><label for="cb5">Onions</label></li>
  <li><input type="checkbox" id="cb6" value="gpeppers" /><label for="cb6">Green Peppers</label></li>
</ul>
</fieldset>

<fieldset class="group">
  <legend>Select <span class="prem">premium</span> pizza toppings (extra cost)</legend>
<ul class="checkbox">
  <li><input type="checkbox" id="cb7" value="proscuitto" /><label for="cb7">Proscuitto</label></li>
  <li><input type="checkbox" id="cb8" value="portobello" /><label for="cb8">Portobello Mushrooms</label></li>
  <li><input type="checkbox" id="cb9" value="ypeppers" /><label for="cb9">Yellow Peppers</label></li>
  <li><input type="checkbox" id="cb10" value="bcheese" /><label for="cb10">Blue Cheese</label></li>
  <li><input type="checkbox" id="cb11" value="shrimps" /><label for="cb11">Shrimps</label></li>
  <li><input type="checkbox" id="cb12" value="sundried" /><label for="cb12">Sun Dried Tomatoes</label></li>
</ul>
</fieldset> 
"""

example_info.script      = """
   <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('ul.checkbox li').focusin( function() {
    $(this).addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('ul.checkbox li').focusout( function() {
    $(this).removeClass('focus');
  }
  );

}
);

  </script>
"""

example_info.style       = """
   <style type="text/css">
fieldset.group  {
  margin: 0;
  padding: 0;
  margin-bottom: 1.25em;
  padding: .125em;
  
  border-style:none;

  }

fieldset.group legend {
  margin: 0;
  padding: 0;
  font-weight: bold;
  margin-left: 20px;
  font-size: 100%;
  color: black;

}
ul.checkbox  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;			
}

ul.checkbox li input {
  margin-right: .25em;
}

ul.checkbox li {
  border: 1px transparent solid;
}

ul.checkbox li label {
  margin-left: ;
}

ul.checkbox li:hover,
ul.checkbox li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 12em;
}


p.inst {
margin: 0;
  padding: 0;
  margin-bottom: .75em;
  margin-left: 20px;
  font-size: 100%;
  color: black;
}

span.prem {
  font-family:fantasy;
  font-style:italic;
  letter-spacing: .05em;
}
  </style>
"""

example9 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example9).delete()
script2      = ExampleScript.objects.get(script='examples/js/jquery-2.0.2.min.js')
add_script_reference( example9, script2 )
