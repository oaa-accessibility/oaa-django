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
eg_radio = ExampleGroup.objects.get(slug="radio")
eg_focus    = ExampleGroup.objects.get(slug="focus")

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio]
example_info.title       = '@input[type=radio]@ - No labels on radio buttons'
example_info.permanent_slug = 'radio1'

example_info.description = """
* Form controls without labels are inaccessible!
"""
example_info.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='radio')

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "fail", "na", "", "", "")
rr2 = rule_reference_object("CONTROL_3", "fail", "na", "", "", "")

example_info.rule_references = [rr1, rr2]

example_info.html        = """
 <div class="label">Select pizza crust</div>
<ul class="radio">
  <li><input type="radio" name="crust" value="deep"/>Deep dish</li>
  <li><input type="radio" name="crust" value="thick"/>Thick</li>
  <li><input type="radio" name="crust" value="hand"/>Hand thrown</li>
  <li><input type="radio" name="crust" value="thin"/>Thin</li>
</ul>  
"""

example_info.script      = """"""

example_info.style       = """
  <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-weight: bold;
}

ul.radio {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}


  </style>
"""

example1 = create_example(example_info)

# =============================
# Example 2
# =============================

order +=1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio]
example_info.title       = '@input[type=radio]@ - Labeling radio buttons using the @title@ attribute'
example_info.permanent_slug = 'radio2'

example_info.description = """
* Using the title attribute to define labels will work with assistive technologies but is not defined in the HTML specifications
"""
example_info.keyboard    = """
"""

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "", "", "")
rr2 = rule_reference_object("CONTROL_3", "fail", "na", "", "", "")

example_info.rule_references = [rr1, rr2]

example_info.html        = """
<div class="label">Select pizza crust</div>
<ul class="radio">
  <li><input type="radio" name="crust" value="deep" <HL1>title="<HL2>Deep dish</HL2>"</HL1>/>Deep dish</li>
  <li><input type="radio" name="crust" value="thick" <HL1>title="<HL2>Thick</HL2>"</HL1>/>Thick</li>
  <li><input type="radio" name="crust" value="hand" <HL1>title="<HL2>Hand thrown</HL2>"</HL1>/>Hand thrown</li>
  <li><input type="radio" name="crust" value="thin" <HL1>title="<HL2>Thin</HL2>"</HL1>/>Thin</li>
</ul> 
"""

example_info.script      = """"""
example_info.style       = """

   <style type="text/css">
div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-weight: bold;
}

ul.radio {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}


  </style>
"""

example2 = create_example(example_info)

# =============================
# Example 3
# =============================

order +=1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio]
example_info.title       = '@input[type=radio]@ - Label using @label@ element encapsulating radio buttons'
example_info.permanent_slug = 'radio3'

example_info.description = """
* Encapsulation is compatible with assistive technologies and is defined in HTML specifications.
* @Label@ element content increases the active area for changing the selection
* What makes this a poor practice is the inconsistency with the labeling requirements of other form controls which need to use the label by reference technique.
"""
example_info.keyboard    = """
"""
example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T2", "", "")
rr2 = rule_reference_object("CONTROL_3", "fail", "na", "", "", "")

example_info.rule_references = [rr1, rr2]

example_info.html        = """
<div class="label">Select pizza crust</div>
<ul class="radio">
  <li><HL1><label></HL1><input type="radio" name="crust" value="deep"/>Deep dish<HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="radio" name="crust" value="thick"/>Thick<HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="radio" name="crust" value="hand"/>Hand thrown<HL1></label></HL1></li>
  <li><HL1><label></HL1><input type="radio" name="crust" value="thin"/>Thin<HL1></label></HL1></li>
</ul> 
"""

example_info.script      = """"""
example_info.style       = """
   <style type="text/css">
div.radiogroup div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-weight: bold;
}

ul.radio  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}


  </style>
"""

example3 = create_example(example_info)

# =============================
# Example 4
# =============================

order+=1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio]
example_info.title       = '@input[type=radio]@ - Labeling using @label@ element and @for@ attribute to reference radio buttons'
example_info.permanent_slug = 'radio4'

example_info.description = """
* The label reference technique is compatible with assistive technologies and is defined in HTML specifications.
* The reference technique is consistent with how other input form controls are labeled and therefore developers only need to use one rule when using the @label@ element .
"""

example_info.keyboard    = """
"""

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "", "")
rr2 = rule_reference_object("CONTROL_3", "fail", "na", "", "", "")

example_info.rule_references = [rr1, rr2]

example_info.html        = """
 <div class="radiogroup">
  <div class="label">Select pizza crust</div>
  <ul class="radio">
    <li><input type="radio" name="crust" <HL1>id<="<HL2>crust1</HL2>"</HL1> value="deep"/><HL1><label for="<HL2>crust1</HL2>"></HL1>>Deep dish</label></li>
    <li><input type="radio" name="crust" <HL1>id="<HL2>crust2</HL2>"</HL1> value="thick"/><HL1><label for="<HL2>crust2</HL2>"></HL1> Thick</label></li>
    <li><input type="radio" name="crust" <HL1>id="<HL2>crust3</HL2>"</HL1> value="hand"/><HL1><label for="<HL2>crust3</HL2>"></HL1>Hand thrown</label></li>
    <li><input type="radio" name="crust" <HL1>id="<HL2>crust4</HL2>"</HL1> value="thin"/><HL1><label for="<HL2>crust4</HL2>"></HL1>Thin</label></li>
  </ul>
</div> 
"""

example_info.script      = """"""
example_info.style       = """
<style type="text/css">
div.radiogroup div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-weight: bold;
}

ul.radio  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}


  </style>
"""

example4 = create_example(example_info)

# =============================
# Example 5
# =============================

order += 1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio, eg_focus]
example_info.title       = '@input[type=radio]@ - highlighting radio buttons when they receive keyboard focus'
example_info.permanent_slug = 'radio5'

example_info.description = """
* Use javascripting to update styling of radio button @label@ with keyboard focus.
* Include @onFocus@ and @onBlur@ event handlers on @input@ element to update class value of parent @li@.
* Include CSS @:hover@ psuedo element to highlight the active area of the @label@ for selecting a radio button.
"""
example_info.keyboard    = """
"""

m2 = ElementDefinition.objects.get(spec=spec_css21, element="border-color")
m3 = ElementDefinition.objects.get(spec=spec_css21, element="background")

example_info.markup = [m1, m2, m3]

example_info.html        = """
<div class="radiogroup">
  <div class="label">Select pizza crust</div>
  <ul class="radio">
    <li><input type="radio" name="crust" id="crust1" value="deep" onfocus="radioFocus(event)" onblur="radioBlur(event)"/><label for="crust1">Deep dish</label></li>
    <li><input type="radio" name="crust" id="crust2" value="thick" onfocus="radioFocus(event)" onblur="radioBlur(event)"/><label for="crust2">Thick</label></li>
    <li><input type="radio" name="crust" id="crust3" value="hand" onfocus="radioFocus(event)" onblur="radioBlur(event)"/><label for="crust3">Hand thrown</label></li>
    <li><input type="radio" name="crust" id="crust4" value="thin" onfocus="radioFocus(event)" onblur="radioBlur(event)"/><label for="crust4">Thin</label></li>
  </ul>
</div> 
"""

example_info.script      = """
  <script type="text/javascript">

//
//   Add focus styling to the parent (LI) element of the radio button receiving focus
//
function radioFocus( event ) {
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
function radioBlur( event ) {
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
div.radiogroup div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-weight: bold;
}

ul.radio  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}


ul.radio li {
  border: 1px transparent solid;
}

ul.radio li:hover,
ul.radio li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 10em;
}

  </style>
  </style>
"""

example5 = create_example(example_info)

# =============================
# Example 6
# =============================

order += 1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio, eg_focus]
example_info.title       = '@input[type=radio]@ - highlighting radio buttons when they receive keyboard focus using JQUERY'
example_info.permanent_slug = 'radio6'

example_info.description = """
* Use JQeury javascript libary to update styling of radio button @label@ with keyboard focus and blur event handlers.
* Include CSS @:hover@ psuedo element to highlight the active area of the @label@ for selecting a radio button.
"""
example_info.keyboard    = """
"""


example_info.markup = [m1, m2, m3]



example_info.html        = """
 <div class="radiogroup">
  <div class="label">Select pizza crust</div>
  <ul class="radio">
    <li><input type="radio" name="crust" id="crust1" value="deep" /><label for="crust1">Deep dish</label></li>
    <li><input type="radio" name="crust" id="crust2" value="thick" /><label for="crust2">Thick</label></li>
    <li><input type="radio" name="crust" id="crust3" value="hand" /><label for="crust3">Hand thrown</label></li>
    <li><input type="radio" name="crust" id="crust4" value="thin" /><label for="crust4">Thin</label></li>
  </ul>
</div>
"""

example_info.script      = """
 <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('ul.radio li').focusin( function() {
    $(this).addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('ul.radio li').focusout( function() {
    $(this).removeClass('focus');
  }
  );

}
);

  </script>
"""

example_info.style       = """
  <style type="text/css">
div.radiogroup div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-weight: bold;
}

ul.radio  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}


ul.radio li {
  border: 1px transparent solid;
}

ul.radio li:hover,
ul.radio li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 10em;
}

  </style>
"""

example6 = create_example(example_info)

# =============================
# Example 7 
# =============================

order += 1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio]
example_info.title       = '@input[type=radio]@ - radio buttons with fieldset/legend elements for labelling'
example_info.permanent_slug = 'radio7'

rr2 = rule_reference_object("CONTROL_3", "pass", "na", "CONTROL_3_T1", "", "")

example_info.rule_references = [rr2]

example_info.description = """
* fieldset/legend elements are used to bind the group @label@ information to the radio buttons in the group.
* Screen readers read the @legend@ element content when the one of the radio buttons in the radio group receives keyboard focus.
* One problem with the legend element is the limited browser supporting in restyling the legend element with CSS. Browsers only render legend as a single line, making long legends run off the visible screen or over other page content.
"""
example_info.keyboard    = """
"""

example_info.markup = [m1]

example_info.html        = """

<HL1><fieldset class="radiogroup"></HL1>
<HL1><legend><HL2>Select pizza crust</HL2></legend></HL1>
  <ul class="radio">
    <li><input type="radio" name="crust" id="crust1" value="deep" /><label for="crust1">Deep dish</label></li>
    <li><input type="radio" name="crust" id="crust2" value="thick" /><label for="crust2">Thick</label></li>
    <li><input type="radio" name="crust" id="crust3" value="hand" /><label for="crust3">Hand thrown</label></li>
    <li><input type="radio" name="crust" id="crust4" value="thin" /><label for="crust4">Thin</label></li>
  </ul>
<HL1></fieldset></HL1>

<HL1><fieldset class="radiogroup"></HL1>
<HL1><legend><HL2>Select delivery methods</HL2></legend></HL1>
  <ul class="radio">
    <li><input type="radio" name="delivery" id="del1" value="in" /><label for="del1">Dine in</label></li>
    <li><input type="radio" name="delivery" id="del2" value="out" /><label for="del2">Carry out</label></li>
    <li><input type="radio" name="delivery" id="del3" value="delivery" /><label for="del3">Delivery</label></li>
  </ul>
<HL1></fieldset></HL1> 
"""

example_info.script      = """
  <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('ul.radio li').focusin( function() {
    $(this).addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('ul.radio li').focusout( function() {
    $(this).removeClass('focus');
  }
  );

}
);

  </script>
"""

example_info.style       = """
  <style type="text/css">

fieldset.radiogroup  {
  margin: 0;
  padding: 0;
  margin-bottom: 1.25em;
  padding: .125em;
}

fieldset.radiogroup legend {
  margin: 0;
  padding: 0;
  font-weight: bold;
  margin-left: 20px;
  font-size: 100%;
  color: black;
}


ul.radio  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.radio li {
  border: 1px transparent solid;
}

ul.radio li:hover,
ul.radio li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 10em;
}

  </style>
"""

example7 = create_example(example_info)

# =============================
# Example 8
# =============================

order += 1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio]
example_info.title       = '@input[type=radio]@ - using an @img@ element @alt@ attribute to indicate required radio buttons'
example_info.permanent_slug = 'radio8'

example_info.description = """
* The required image is part of the @legend@ content and the alt attribute content is added to the @legend@ content.
"""
example_info.keyboard    = """
"""

example_info.markup = [m1]

rr2 = rule_reference_object("CONTROL_3", "pass", "na", "CONTROL_3_T1", "", "")

example_info.rule_references = [rr2]

example_info.html        = """

<fieldset class="radiogroup">
  <legend>Select pizza crust <img src="images/required.png" <HL1>alt="<HL2>required</HL2>"</HL1> /></legend>
  <ul class="radio">
    <li><input type="radio" name="crust" id="crust1" value="deep" /><label for="crust1">Deep dish</label></li>
    <li><input type="radio" name="crust" id="crust2" value="thick" /><label for="crust2">Thick</label></li>
    <li><input type="radio" name="crust" id="crust3" value="hand" /><label for="crust3">Hand thrown</label></li>
    <li><input type="radio" name="crust" id="crust4" value="thin" /><label for="crust4">Thin</label></li>
  </ul>
</fieldset>

<fieldset class="radiogroup">
  <legend>Select delivery method <img src="images/required.png" <HL1>alt="<HL2>required</HL2>"</HL1> /></legend>
  <ul class="radio">
    <li><input type="radio" name="delivery" id="del1" value="in" /><label for="del1">Dine in</label></li>
    <li><input type="radio" name="delivery" id="del2" value="out" /><label for="del2">Carry out</label></li>
    <li><input type="radio" name="delivery" id="del3" value="delivery" /><label for="del3">Delivery</label></li>
  </ul>
</fieldset> 
"""

example_info.script      = """"""

example_info.style       = """
  <style type="text/css">
fieldset.radiogroup  {
  margin: 0;
  padding: 0;
  margin-bottom: 1.25em;
  border: none;
}

fieldset.radiogroup legend {
  margin: 0;
  padding: 0;
  font-weight: bold;
  padding-left: 20px;
}

ul.radio  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}

ul.radio li {
  border: 1px transparent solid;
}

ul.radio li:hover,
ul.radio li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 10em;
}
  </style>
"""

example8 = create_example(example_info)

# =============================
# Example 9
# =============================

order += 1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio]
example_info.title       = '@input[type=radio]@ - using an @span@ element in a @legend@ element to indicate required radio buttons'
example_info.permanent_slug = 'radio9'

example_info.description = """
* The "required" text is just made part of the @legend@ text.
* A @span@ element and CSS are used to style the "required" differently. 
"""
example_info.keyboard    = """
"""

rr2 = rule_reference_object("CONTROL_3", "pass", "na", "CONTROL_3_T1", "", "")

example_info.rule_references = [rr2]

example_info.markup = [m1]

example_info.html        = """
<fieldset class="radiogroup">
  <legend>Select pizza crust <span class="required">(required)</span></legend>
  <ul class="radio">
    <li><input type="radio" name="crust" id="crust1" value="deep" /><label for="crust1">Deep dish</label></li>
    <li><input type="radio" name="crust" id="crust2" value="thick" /><label for="crust2">Thick</label></li>
    <li><input type="radio" name="crust" id="crust3" value="hand" /><label for="crust3">Hand thrown</label></li>
    <li><input type="radio" name="crust" id="crust4" value="thin" /><label for="crust4">Thin</label></li>
  </ul>
</fieldset>

<fieldset class="radiogroup">
  <legend>Select delivery method <span class="required">(required)</span></legend>
  <ul class="radio">
    <li><input type="radio" name="delivery" id="del1" value="in" /><label for="del1">Dine in</label></li>
    <li><input type="radio" name="delivery" id="del2" value="out" /><label for="del2">Carry out</label></li>
    <li><input type="radio" name="delivery" id="del3" value="delivery" /><label for="del3">Delivery</label></li>
  </ul>
</fieldset> 
"""

example_info.script      = """
  <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('ul.radio li').focusin( function() {
    $(this).addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('ul.radio li').focusout( function() {
    $(this).removeClass('focus');
  }
  );

}
);

  </script>
"""

example_info.style       = """
  <style type="text/css">
fieldset.radiogroup  {
  margin: 0;
  padding: 0;
  margin-bottom: 1.25em;
  border: none;
}

fieldset.radiogroup legend {
  margin: 0;
  padding: 0;
  font-weight: bold;
  padding-left: 20px;
}

ul.radio  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}


.required {
  font-size: 75%;
  color: blue;
}


ul.radio li {
  border: 1px transparent solid;
}

ul.radio li:hover,
ul.radio li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 10em;
}
  </style>
"""

example9 = create_example(example_info)

# =============================
# Example 10
# =============================

order += 1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_radio]
example_info.title       = '@input[type=radio]@ - radio buttons with long @legend@ elements wrapped around multiple lines using @span@ elements'
example_info.permanent_slug = 'radio10'

example_info.description = """
* The @span@ element and CSS properties can be used to support the line wrapping of @legend@ element content.
* The first example is the standard rendering of long @legend@ content. The second example demonstrates how to implement line wrapping using the @span@ element.
"""
example_info.keyboard    = """
"""


example_info.markup = [m1]

example_info.html        = """

<fieldset class="radiogroup">
  <legend>Tracy caught 9 fish in the morning.   She threw 5 of them back because they were too small.  She caught 8 more in the afternoon. How many fish did Tracy have then?</legend>
  <ul class="radio">
    <li><input type="radio" name="a" id="a1" value="1" /><label for="a1">8</label></li>
    <li><input type="radio" name="a" id="a2" value="2" /><label for="a2">12</label></li>
    <li><input type="radio" name="a" id="a3" value="3" /><label for="a3">17</label></li>
    <li><input type="radio" name="a" id="a4" value="4" /><label for="a4">22</label></li>
  </ul>
</fieldset>

<fieldset class="radiogroup">
  <legend><span class="wrap">Trevor counted 77 coins in his bank.  He counted 29 quarters.  The rest are dimes.  How many more dimes than quarters does Trevor have?</span></legend>
  <ul class="radio">
    <li><input type="radio" name="b" id="b1" value="1" /><label for="b1">17</label></li>
    <li><input type="radio" name="b" id="b2" value="2" /><label for="b2">29</label></li>
    <li><input type="radio" name="b" id="b3" value="3" /><label for="b3">19</label></li>
    <li><input type="radio" name="b" id="b4" value="4" /><label for="b4">48</label></li>
  </ul>
</fieldset> 
"""

example_info.script      = """
  <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('ul.radio li').focusin( function() {
    $(this).addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('ul.radio li').focusout( function() {
    $(this).removeClass('focus');
  }
  );

}
);

  </script>
"""

example_info.style       = """
  <style type="text/css">
fieldset.radiogroup  {
  margin: 0;
  padding: 0;
  margin-bottom: 1.25em;
  border: none;
}

ul.radio  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  list-style: none;
}


fieldset.radiogroup legend span.wrap {
  font-size: 100%;
  color:  black;
  font-weight: bold;
  display: block;
  width: 100%;
  white-space: normal;
}


ul.radio li {
  border: 1px transparent solid;
}

ul.radio li:hover,
ul.radio li.focus  {
  background-color: lightyellow;
  border: 1px gray solid;
  width: 10em;
}

  </style>
"""

example10 = create_example(example_info)
