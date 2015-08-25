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

eg_labeling = ExampleGroup.objects.get(slug="aria-live")

example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info.title       = '@select@  element - @Select@ elements with no accessible label'
example_info.permanent_slug = 'select1'

example_info.description = """
* Form controls without labels are inaccessible!
"""
example_info.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='select', attribute='')

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "fail", "na", "", "", "")

example_info.rule_references = [rr1]

example_info.html        = """
<div class="label">Select pizza crust</div>
<select name="crust">
    <option>Deep dish</option>
    <option>Thick</option>
    <option>Hand thrown</option>
    <option>Thin</option>
</select> 
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

select  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
}

  </style>
"""

example1 = create_example(example_info)

# =============================
# Example 2
# =============================
order += 1

example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info.title       = '@select@  element - Labeling @select@ elements using @title@ attribute'
example_info.permanent_slug = 'select2'

example_info.description = """
* Using the title attribute to define labels will work with assistive technologies but is not defined in the HTML specifications
"""
example_info.keyboard    = """
"""

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "", "", "")
rr2 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T1", "", "")
rr3 = rule_reference_object("CONTROL_12", "na", "pass", "CONTROL_12_T1", "", "")

example_info.rule_references = [rr1, rr2, rr3]

example_info.html        = """
 <div class="label">Select pizza crust</div>
<select name="crust" <HL1>title="<HL2>Select Pizza Crust</HL2>"</HL1>>
    <option>Deep dish</option>
    <option>Thick</option>
    <option>Hand thrown</option>
    <option>Thin</option>
</select> 
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

select  {
  margin: 0;
  padding: 0;
  margin-left: 20px;
}

  </style>
"""

example2 = create_example(example_info)

# =============================
# Example 3
# =============================
order += 1
example_info             = example_object()
example_info.title       = '@select@  element - Labeling using @label@ element encapsulate @select@ elements'
example_info.permanent_slug = 'select2'

example_info.description = """
* Encapsulation is compatible with assistive technologies and is defined in HTML specifications.
* label element content increases the active area for changing the selection
* What makes this a poor practice is the inconsistency with the labeling requirements of other form controls which need to use the label by reference technique.
"""
example_info.keyboard    = """
"""
example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T2", "", "")
rr2 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T1", "", "")
rr3 = rule_reference_object("CONTROL_12", "na", "pass", "CONTROL_12_T1", "", "")

example_info.rule_references = [rr1, rr2, rr3]

example_info.html        = """
<HL1><label></HL1> <HL2>Select pizza crust</HL2>
  <select name="crust" >
    <option>Deep dish</option>
    <option>Thick</option>
    <option>Hand thrown</option>
    <option>Thin</option>
  </select>
<HL1></label></HL1>
"""

example_info.script      = """"""

example_info.style       = """
   <style type="text/css">
label {
  margin: 0;
  padding: 0;
  margin-left: 20px;The label reference technique is compatible with assistive technologies and is defined in HTML specifications.
  font-size: 100%;
  font-weight: bold;
  display: block;
}

select  {
  margin: 0;
  padding: 0;
  display: block;
  }

  </style>
"""

example3 = create_example(example_info)

# =============================
# Example 4
# =============================
order += 1

example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info.title       = '@select@  element - Labeling using @label@ element and @for@ attribute to reference @select@ elements'
example_info.permanent_slug = 'select4'

example_info.description = """
* The label reference technique is compatible with assistive technologies and is defined in HTML specifications.
* The reference technique is consistent with how other input form controls are labeled and therefore developers only need to use one rule when using the label element .
"""

example_info.keyboard    = """
"""

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "", "")
rr2 = rule_reference_object("CONTROL_10", "pass", "na", "CONTROL_10_T1", "", "")
rr3 = rule_reference_object("CONTROL_12", "na", "pass", "CONTROL_12_T1", "", "")

example_info.rule_references = [rr1, rr2, rr3]

example_info.html        = """
<div class="select">
    <HL1><label for="<HL2>crust</HL2>">Select Pizza Crust</label></HL1>
    <select name="crust" <HL1>id="<HL2>crust</HL2>"</HL1>>
    <option>Deep dish</option>
    <option>Thick</option>
    <option>Hand thrown</option>
    <option>Thin</option>
  </select>
</div>    
"""

example_info.script      = """"""

example_info.style       = """
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

example4 = create_example(example_info)

# =============================
# Example 5
# =============================
order += 1

example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info.title       = '@select@  element - highlighting @select@ elements when they receive keyboard focus'
example_info.permanent_slug = 'select5'

example_info.description = """
* Use javascripting to update styling of checkboxes label with keyboard focus.
* Include onFocus and onBlur event handlers on input element to update class value of parent li.
* Include CSS :hover psuedo element to highlight the active area of the label for selecting a checkbox.
"""
example_info.keyboard    = """
"""

m2 = ElementDefinition.objects.get(spec=spec_css21, element='background', attribute='')
m3 = ElementDefinition.objects.get(spec=spec_css21, element='border-color', attribute='')
m4 = ElementDefinition.objects.get(spec=spec_css21, element=':active', attribute='')
m5 = ElementDefinition.objects.get(spec=spec_css21, element=':focus', attribute='')
m6 = ElementDefinition.objects.get(spec=spec_css21, element=':hover', attribute='')

example_info.markup = [m1, m2, m3, m4, m5, m6]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "", "")

example_info.rule_references = [rr1]

example_info.html        = """
<div class="select">
    <label for="crust">Select Pizza Crust</label>
    <select name="crust" id="crust" onfocus="parentFocus(event)" onblur="parentBlur(event)">
    <option>Deep dish</option>
    <option>Thick</option>
    <option>Hand thrown</option>
    <option>Thin</option>
  </select>
</div>     
"""

example_info.script      = """
  <script type="text/javascript">

//
//   Add focus styling to the parent (DIV) element of the radio button receiving focus
//
function parentFocus( event ) {
  // Get event object  if using Internet Explorer
  var e = event || window.event;
  
  // Check the object for W3C DOM event object, if not use IE event object to update the class of the parent element
  if( e.target )
    e.target.parentNode.className = "select focus";
  else
    e.srcElement.parentNode.className = "select focus";
  
}

//
//   Remove focus styling from the parent (DIV) element of the radio button receiving focus
//
function parentBlur( event ) {
  // Get event object  if using Internet Explorer
  var e = event || window.event;
  
  var node;
  
  // Check the object for W3C DOM event object, if not use IE event object to update the class of the parent element
  if( e.target )
    e.target.parentNode.className = "select";
  else
    e.srcElement.parentNode.className = "select";

}
  </script>
"""

example_info.style       = """
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

example5 = create_example(example_info)

# =============================
# Example 6
# =============================
order += 1

example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info.title       = '@select@  element - highlighting @select@ elements when they receive keyboard focus using JQUERY'
example_info.permanent_slug = 'select6'

example_info.description = """
* Use javascripting to update styling of checkboxes label with keyboard focus.
* Include onFocus and onBlur event handlers on input element to update class value of parent li.
* Include CSS :hover psuedo element to highlight the active area of the label for selecting a checkbox.
"""
example_info.keyboard    = """
"""


example_info.markup = [m1, m2, m3, m4, m5, m6]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "", "")

example_info.rule_references = [rr1]

example_info.html        = """
 <div class="select">
    <label for="crust">Select Pizza Crust</label>
    <select name="crust" id="crust">
    <option>Deep dish</option>
    <option>Thick</option>
    <option>Hand thrown</option>
    <option>Thin</option>
  </select>
</div>   
"""

example_info.script      = """
   <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('select').focusin( function() {
    $(this).parent().addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('select').focusout( function() {
    $(this).parent().removeClass('focus');
  }
  );

}
);

  </script>
"""

example_info.style       = """
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

example6 = create_example(example_info)

# =============================
# Example 7 
# =============================
order += 1

example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info.title       = '@select@  element - using CSS to right justify @select@ elements'
example_info.permanent_slug = 'select7'

example_info.description = """
* CSS styling of label element for positioning off screen.
* The label will not be rendered visullly, but is still readible by screen readers.
* NEVER use display: none or visibility: hidden to hide labels for the visual rendering, since it will also hide the label from screen readers.
"""
example_info.keyboard    = """
"""

m7 = ElementDefinition.objects.get(spec=spec_css21, element='right', attribute='')

example_info.markup = [m1, m2, m3, m4, m5, m6, m7]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "", "")

example_info.rule_references = [rr1]

example_info.html        = """

 <div class="select">
    <label for="crust">Select Pizza Crust</label>
    <select name="crust" id="crust" >
      <option>Deep dish</option>
      <option>Thick</option>
      <option>Hand thrown</option>
      <option>Thin</option>
    </select>
</div>  

<div class="select">
    <label for="delivery">Select Pizza Deilvery</label>
    <select name="delivery" id="delivery">
        <option>Dine in</option>
        <option>Carry out</option>
        <option>Home delivery</option>
        <option>Express air</option>
    </select>
</div>   
"""

example_info.script      = """
  <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('select').focusin( function() {
    $(this).parent().addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('select').focusout( function() {
    $(this).parent().removeClass('focus');
  }
  );

}
);

  </script>
  </script>
"""

example_info.style       = """
  <style type="text/css">
div.select {
  margin: 0;
  margin-left: 20px;
  padding: .25em;;
  border: thin solid transparent;
  width: 20em;
}

div.focus,
div.select:hover {
  border: thin solid gray;
  background-color: lightyellow;
}

div.select label {
  margin: 0;
  padding: 0;
  padding-right: .25em;
  font-size: 100%;
  font-weight: bold;
  display: block;
  width: 10em;
  text-align: right;
  float: left;
  
}

div.select select  {
  margin: 0;
  padding: 0;
  font-size; 100%;
  display: block;  
  }

div.select select:hover,
div.select select:focus,
div.select select:active {
  background-color: lightyellow;
  border-color: gray;
}
  </style>
"""

example7 = create_example(example_info)

# =============================
# Example 8
# =============================
order += 1
example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info.title       = '@select@  element - using CSS to left justify @select@ elments'
example_info.permanent_slug = 'select8'

example_info.description = """
None Provided
"""
example_info.keyboard    = """
"""

m7 = ElementDefinition.objects.get(spec=spec_css21, element='left', attribute='')

example_info.markup = [m1, m2, m3, m4, m5, m6, m7]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "", "")

example_info.rule_references = [rr1]

example_info.html        = """
<div class="select">
    <label for="crust">Select Pizza Crust</label>
    <select name="crust" id="crust" >
      <option>Deep dish</option>
      <option>Thick</option>
      <option>Hand thrown</option>
      <option>Thin</option>
    </select>
</div>  

<div class="select">
    <label for="delivery">Select Pizza Deilvery</label>
    <select name="delivery" id="delivery">
        <option>Dine in</option>
        <option>Carry out</option>
        <option>Home delivery</option>
        <option>Express air</option>
    </select>
</div>   
"""

example_info.script      = """
   <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('select').focusin( function() {
    $(this).parent().addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('select').focusout( function() {
    $(this).parent().removeClass('focus');
  }
  );

}
);

  </script>
"""

example_info.style       = """
   <style type="text/css">
div.select {
  margin: 0;
  margin-left: 20px;
  padding: .25em;;
  border: thin solid transparent;
  width: 20em;
}

div.focus,
div.select:hover {
  border: thin solid gray;
  background-color: lightyellow;  
}

div.select label {
  margin: 0;
  padding: 0;
  padding-right: .25em;
  font-size: 100%;
  font-weight: bold;
  display: block;
  width: 10em;
  text-align: left;
  float: left;
  
}

div.select select  {
  margin: 0;
  padding: 0;
  font-size; 100%;
  display: block;  
  }

div.select select:hover,
div.select select:focus,
div.select select:active {
  background-color: lightyellow;
  border-color: gray;
}
  </style>
"""

example8 = create_example(example_info)

# =============================
# Example 9
# =============================
order += 1

example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info.title       = '@select@  element - using CSS to move @select@ elments offscreen'
example_info.permanent_slug = 'select9'

example_info.description = """
None Provided
"""
example_info.keyboard    = """
"""

m7 = ElementDefinition.objects.get(spec=spec_css21, element='position', attribute='')

example_info.markup = [m1, m2, m3, m4, m5, m6, m7]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "", "")

example_info.rule_references = [rr1]


example_info.html        = """
 <div class="select">
    <label for="crust">Select Pizza Crust</label>
    <select name="crust" id="crust" >
      <option>Deep dish</option>
      <option>Thick</option>
      <option>Hand thrown</option>
      <option>Thin</option>
    </select>
</div>  

<div class="select">
    <label for="delivery">Select Pizza Deilvery</label>
    <select name="delivery" id="delivery">
        <option>Dine in</option>
        <option>Carry out</option>
        <option>Home delivery</option>
        <option>Express air</option>
    </select>
</div>    
"""

example_info.script      = """
   <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('select').focusin( function() {
    $(this).parent().addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('select').focusout( function() {
    $(this).parent().removeClass('focus');
  }
  );

}
);

  </script>
"""

example_info.style       = """

  <style type="text/css">
div.select {
  margin: .25em;
  padding: .25em;;
  border: thin solid transparent;
  width: 7em;
}

div.focus,
div.select:hover {
  border: thin solid gray;
  background-color: lightyellow;  
}

div.select label {
  position: absolute;
  top: -30em;
  left: -300em;
}

div.select select  {
  margin: 0;
  padding: 0;
  font-size; 100%;
  display: block;  
  }

div.select select:hover,
div.select select:focus,
div.select select:active {
  background-color: lightyellow;
  border-color: gray;
}
  </style>
"""

example9 = create_example(example_info)

# =============================
# Example 10
# =============================
order += 1

example_info0             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info0.title       = '@select@  element - Onchange event for @option@ elements of @select@ elements'
example_info0.permanent_slug = 'select10'

example_info0.description = """
* OnChange event is a problem for keyboard users and users of screen reader technology to explore the options and trigger the onchange event on the option of their choice.
* Many web browsers trigger the onchange event when the user types Up and down arrow keys or when the select box loses focus, which can cause a change in focus.
* Some web browsers have alternatives to the Up and Down arrow keys to view options without triggering the onChange event.
"""
example_info0.keyboard    = """
"""

example_info0.markup = [m1]

example_info0.html        = """

<!--
Example using inline event handler
This technique of adding event handlers is considered obsolete
-->

<div class="select">
    <label for="crust">Pick Your Favorite News Source</label>
    <select name="crust" id="select1" <HL1>onchange="goto_url(event)</HL1>">
        <option value="http://www.cnn.com/">CNN</option>
        <option value="http://cbsnews.com/">CBS News</option>
        <option value="http://abcnews.go.com/">ABC News</option>
        <option value="http://news.google.com/">Google News</option>
        <option value="http://www.reuters.com/">Reuters</option>
        <option value="http://news.yahoo.com/">Yahoo News</option>
        <option value="http://news.bbc.co.uk/">BBC News</option>
        <option value="http://www.worldnews.com/">World News</option>
        <option value="http://www.msnbc.com/">MSN NBC</option>
        <option value="http://www.foxnews.com/">FOX News</option>
        <option value="http://www.usatoday.com/">USA Today</option>
    </select>
</div>


<!--
    Example using jquesry to add onchange event handler    
-->


<div class="select">
    <label for="crust">Pick Your Favorite Favorite President of the 20th Century</label>
    <select name="crust" id="select2">
        <option value="http://www.whitehouse.gov/about/presidents/theodoreroosevelt">Theodore Roosevelt  
            <option value="http://www.whitehouse.gov/about/presidents/williamhowardtaft">William Howard Taft</option>  
            <option value="http://www.whitehouse.gov/about/presidents/woodrowwilson">Woodrow Wilson</option>  
            <option value="http://www.whitehouse.gov/about/presidents/warrenharding">Warren G. Harding</option>  
            <option value="http://www.whitehouse.gov/about/presidents/calvincoolidge">Calvin Coolidge</option>  
            <option value="http://www.whitehouse.gov/about/presidents/herberthoover">Herbert Hoover</option>  
            <option value="http://www.whitehouse.gov/about/presidents/franklindroosevelt">Franklin D. Roosevelt</option>  
            <option value="http://www.whitehouse.gov/about/presidents/harrystruman">Harry S. Truman</option>  
            <option value="http://www.whitehouse.gov/about/presidents/dwightdeisenhower">Dwight D. Eisenhower</option>
            <option value="http://www.whitehouse.gov/about/presidents/johnfkennedy">John F. Kennedy</option>      
            <option value="http://www.whitehouse.gov/about/presidents/lyndonbjohnson">Lyndon B. Johnson</option>
            <option value="http://www.whitehouse.gov/about/presidents/richardnixon">Richard M. Nixon</option>    
            <option value="http://www.whitehouse.gov/about/presidents/geraldford">Gerald R. Ford</option>  
            <option value="http://www.whitehouse.gov/about/presidents/jimmycarter">James Carter</option>    
            <option value="http://www.whitehouse.gov/about/presidents/ronaldreagan">Ronald Reagan</option>        
            <option value="http://www.whitehouse.gov/about/presidents/georgehwbush">George H. W. Bush</option>
            <option value="http://www.whitehouse.gov/about/presidents/williamjclinton">William J. Clinton</option>
    </select>
</div> 
"""

example_info0.script      = """
  <script type="text/javascript">
// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {
  <script type="text/javascript">
//
//   go to url function
//
function goto_url( event ) {
  // Get event object  if using Internet Explorer
  var e = event || window.event;
  
  // Check the object for W3C DOM event object, if not use IE event object to update the class of the parent element
  if( e.target ) {
    var node = e.target;
  } else {
    var node = e.srcElement;
  } // endif
  
  window.location.href = node.options[node.selectedIndex].value;
  
}

// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "focus" value to class attribute
  $('select').focusin( function() {
    $(this).parent().addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('select').focusout( function() {
    $(this).parent().removeClass('focus');
  }
  );

  // Add the onchange event to second select box
  $('select#select2').change( function() {
    window.location.href = $(this).val();
  }
  );

}
);



  </script>
"""

example_info0.style       = """
  <style type="text/css">
div.select {
  margin: 0;
  margin-left: 20px;
  padding: .25em;;
  border: thin solid transparent;
  width: 40em;
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
  border: 1px transparent solid;
  }


div.select select:hover,
div.select select:focus,
div.select select:active {
   border-color: black;
}

  </style>
"""

example10 = create_example(example_info0)

# =============================
# Example 11
# =============================
order += 1

example_info1             = example_object()
example_info1.title       = 'select - Onchange event for @option@ elements of @select@ elements '
example_info1.permanent_slug = 'select11'

example_info1.description = """
* Using a "go" button as an alternative to the onChange event supports keyboard and screen reader users to explore the options and trigger the action.
"""
example_info1.keyboard    = """
"""


example_info1.markup = [m1]

example_info1.html        = """

<!--
Example using inline event handler
This technique of adding event handlers is considered obsolete
-->

<div class="select">
    <label for="select_news">Pick Your Favorite News Source</label>
    <select name="select_news" id="select_news" >
        <option value="http://www.cnn.com/">CNN</option>
        <option value="http://cbsnews.com/">CBS News</option>
        <option value="http://abcnews.go.com/">ABC News</option>
        <option value="http://news.google.com/">Google News</option>
        <option value="http://www.reuters.com/">Reuters</option>
        <option value="http://news.yahoo.com/">Yahoo News</option>
        <option value="http://news.bbc.co.uk/">BBC News</option>
        <option value="http://www.worldnews.com/">World News</option>
        <option value="http://www.msnbc.com/">MSN NBC</option>
        <option value="http://www.foxnews.com/">FOX News</option>
        <option value="http://www.usatoday.com/">USA Today</option>
    </select>
    <input <HL1>onclick="onClickNews(event)"</HL1> type="button" value="Go"/>
</div>


<!--
    Example using jquery to add onchange event handler    
-->


<div class="select select_president">
    <label for="select_president_1">Pick Your Favorite Favorite President of the 20th Century</label>
    <select name="select_president_1" id="select_president_1" ">
        <option value="http://www.whitehouse.gov/about/presidents/theodoreroosevelt" selected="">Theodore Roosevelt  
            <option value="http://www.whitehouse.gov/about/presidents/williamhowardtaft">William Howard Taft</option>  
            <option value="http://www.whitehouse.gov/about/presidents/woodrowwilson">Woodrow Wilson</option>  
            <option value="http://www.whitehouse.gov/about/presidents/warrenharding">Warren G. Harding</option>  
            <option value="http://www.whitehouse.gov/about/presidents/calvincoolidge">Calvin Coolidge</option>  
            <option value="http://www.whitehouse.gov/about/presidents/herberthoover">Herbert Hoover</option>  
            <option value="http://www.whitehouse.gov/about/presidents/franklindroosevelt">Franklin D. Roosevelt</option>  
            <option value="http://www.whitehouse.gov/about/presidents/harrystruman">Harry S. Truman</option>  
            <option value="http://www.whitehouse.gov/about/presidents/dwightdeisenhower">Dwight D. Eisenhower</option>
            <option value="http://www.whitehouse.gov/about/presidents/johnfkennedy">John F. Kennedy</option>      
            <option value="http://www.whitehouse.gov/about/presidents/lyndonbjohnson">Lyndon B. Johnson</option>
            <option value="http://www.whitehouse.gov/about/presidents/richardnixon">Richard M. Nixon</option>    
            <option value="http://www.whitehouse.gov/about/presidents/geraldford">Gerald R. Ford</option>  
            <option value="http://www.whitehouse.gov/about/presidents/jimmycarter">James Carter</option>    
            <option value="http://www.whitehouse.gov/about/presidents/ronaldreagan">Ronald Reagan</option>        
            <option value="http://www.whitehouse.gov/about/presidents/georgehwbush">George H. W. Bush</option>
            <option value="http://www.whitehouse.gov/about/presidents/williamjclinton">William J. Clinton</option>
    </select>
    <button <HL1>onclick="onClickPresident(event)"</HL1>>More information <span class="button_label">on Theodore Roosevelt</span></button>
</div>

<!--
    Updated portion of label is no visible in the graphical rendering by using off screeen positioning    
-->

<div class="select select_president">
    <label for="select_president_2">Pick Your Favorite Favorite President of the 20th Century</label>
    <select name="select_president_2" id="select_president_2" ">
        <option value="http://www.whitehouse.gov/about/presidents/theodoreroosevelt" selected="">Theodore Roosevelt  
            <option value="http://www.whitehouse.gov/about/presidents/williamhowardtaft">William Howard Taft</option>  
            <option value="http://www.whitehouse.gov/about/presidents/woodrowwilson">Woodrow Wilson</option>  
            <option value="http://www.whitehouse.gov/about/presidents/warrenharding">Warren G. Harding</option>  
            <option value="http://www.whitehouse.gov/about/presidents/calvincoolidge">Calvin Coolidge</option>  
            <option value="http://www.whitehouse.gov/about/presidents/herberthoover">Herbert Hoover</option>  
            <option value="http://www.whitehouse.gov/about/presidents/franklindroosevelt">Franklin D. Roosevelt</option>  
            <option value="http://www.whitehouse.gov/about/presidents/harrystruman">Harry S. Truman</option>  
            <option value="http://www.whitehouse.gov/about/presidents/dwightdeisenhower">Dwight D. Eisenhower</option>
            <option value="http://www.whitehouse.gov/about/presidents/johnfkennedy">John F. Kennedy</option>      
            <option value="http://www.whitehouse.gov/about/presidents/lyndonbjohnson">Lyndon B. Johnson</option>
            <option value="http://www.whitehouse.gov/about/presidents/richardnixon">Richard M. Nixon</option>    
            <option value="http://www.whitehouse.gov/about/presidents/geraldford">Gerald R. Ford</option>  
            <option value="http://www.whitehouse.gov/about/presidents/jimmycarter">James Carter</option>    
            <option value="http://www.whitehouse.gov/about/presidents/ronaldreagan">Ronald Reagan</option>        
            <option value="http://www.whitehouse.gov/about/presidents/georgehwbush">George H. W. Bush</option>
            <option value="http://www.whitehouse.gov/about/presidents/williamjclinton">William J. Clinton</option>
    </select>
    <button <HL1>onclick="onClickPresident(event)"</HL1>>More information <span class="button_label offscreen">on Theodore Roosevelt</span></button>
</div> 
"""

example_info1.script      = """
   <script type="text/javascript">
//
//   go to news function
//
function onClickNews( event ) {

  select = document.getElementById('select_news');
  
  window.location.href = select.options[select.selectedIndex].value;  
  
}


//
//   go to president function
//
function onKeyDownPresident1( event ) {
  
  select = document.getElementById('select_president_1');
    
  button_label = document.getElementById('button_label_1');
  
  button_label.innerHTML = select.options[select.selectedIndex].innerHTML;
  
}

//
//   go to president function
//
function onClickPresident1( event ) {
  
  select = document.getElementById('select_president_1');
    
  window.location.href = select.options[select.selectedIndex].value;
  
}

//
//   go to president function
//
function onKeyDownPresident2( event ) {
  
}

//
//   go to president function
//
function onClickPresident2( event ) {
  
  select = document.getElementById('select_president_2');
    
  window.location.href = select.options[select.selectedIndex].value;
  
}



// Using JQuery selectors to add onFocus and onBlur event handlers

$(document).ready( function() {

  // Add the "onchange" event to select box  to update label
  $('div.select_president select').keydown( function() {
    
    var select = document.getElementById($(this).attr('id'));
    
    $(this).parent().find('button span').text( select.options[select.selectedIndex].innerHTML );
      
  }
  );

  // Add the "onchange" event to select box  to update label
  $('div.select_president button').click( function() {
    
    var select = $(this).parent().find('select');
    
    window.location.href = $(select).val();
    
  }
  );



  // Add the "focus" value to class attribute
  $('div.select select').focusin( function() {
    $(this).parent().addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('div.select select').focusout( function() {
    $(this).parent().removeClass('focus');
  }
  );

  // Add the "focus" value to class attribute
  $('div.select button').focusin( function() {
    $(this).parent().addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('div.select button').focusout( function() {
    $(this).parent().removeClass('focus');
  }
  );

  // Add the "focus" value to class attribute
  $('div.select input').focusin( function() {
    $(this).parent().addClass('focus');
  }
  );

  // Remove the "focus" value to class attribute
  $('div.select input').focusout( function() {
    $(this).parent().removeClass('focus');
  }
  );


}
);



  </script>
"""

example_info1.style       = """
 <style type="text/css">
div.select {
  margin: 0;
  margin-left: 20px;
  padding: .25em;;
  border: thin solid transparent;
  width: 40em;
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

div.select select,
div.select button,
div.select input,
{
  margin: 0;
  padding: 0;
  display: inline;
  border: 1px transparent solid;
  }

div.select select:hover,
div.select select:focus,
div.select select:active,
div.select button:hover,
div.select button:focus,
div.select button:active,
div.select select:active,
div.select input:hover,
div.select input:focus,
div.select input:active{
   border-color: black;
}

.offscreen {
  position: absolute;
  top: -20em;
  left: -300em;
}
  </style>
"""

example11 = create_example(example_info1)
