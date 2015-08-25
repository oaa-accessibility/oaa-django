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

example_info1             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info1.title       = '@input[type=text]@ - No labels on text fields and @textarea@ elements'
example_info1.permanent_slug = 'text1'

example_info1.description = """
* Form controls without labels are inaccessible!
"""
example_info1.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_html5 = LanguageSpec.objects.get(url_slug='html5')
spec_aria = LanguageSpec.objects.get(url_slug='aria10')
spec_css21 = LanguageSpec.objects.get(url_slug='css21')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='text')
m2 = ElementDefinition.objects.get(spec=spec_html4, element='textarea', attribute='')

example_info1.markup = [m1,m2]

rr1 = rule_reference_object("CONTROL_1", "fail", "fail", "", "", "")

example_info1.rule_references = [rr1]

example_info1.html        = """
<div class="text">
    <div class="label">Name</div>
    <input type="text" size="30" name="name" />
</div>

<div class="text">
    <div class="label">E-mail</div>
    <input type="text" size="25" name="email" />
</div>

<div class="text">
    <div class="label">Comment</div>
    <textarea rows="5" cols="50" name="comment"></textarea>
</div> 
"""

example_info1.script      = """"""

example_info1.style       = """
  <style type="text/css">
div.text div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
}

div.text input,
div.text textarea {
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
order += 1

example_info2             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info2.title       = '@input[type=text]@ - Labeling text fields and @textarea@ elements using @value@ attribute'
example_info2.permanent_slug = 'text2'

example_info2.description = """
* Form controls without labels are inaccessible!
* Using the @value@ attribute is poor labeling practice for all users since as soon as someone starts typing into the text box the @label@ disappears.
"""
example_info2.keyboard    = """
"""

example_info2.markup = [m1,m2]

rr2 = rule_reference_object("CONTROL_1", "fail", "fail", "", "", "")

example_info2.rule_references = [rr2]

example_info2.html        = """
<div class="text">
    <input type="text" size="30" name="email" value="Name"/>
</div>

<div class="text">
    <input type="text" size="25" name="email" value="E-mail"/>
</div>

<div class="text">
    <textarea rows="5" cols="50" name="comment">Comment</textarea>
</div> 
"""

example_info2.script      = """"""

example_info2.style       = """

  <style type="text/css">
div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: 1.25em;
}

  </style>
"""

example2 = create_example(example_info2)

# =============================
# Example 3
# =============================
order += 1

example_info3             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info3.title       = '@input[type=text]@ - Labeling using @label@ element encapsulate text field and @textarea@ elements'
example_info3.permanent_slug = 'text3'

example_info3.description = """
* Text form controls where the @label@ element encapsulates the text box.
* Encapsulation is a poor accessibility practice since some screen readers read both the @label@ content and the @text@ content of the text box when the text box gets focus. This can be confusing to screen reader users since they cannot distinguish between the @label@ and the content of the @text@ control.
"""
example_info3.keyboard    = """
"""
example_info3.markup = [m1,m2]

rr3 = rule_reference_object("CONTROL_1", "pass", "pass", "CONTROL_1_T1", "", "")

example_info3.rule_references = [rr3]

example_info3.html        = """
<div class="text">
    <HL1><label></HL1>Name<br/>
    <input type="text" size="30" name="name" />
    <HL1></label></HL1>
</div>

<div class="text">
    <HL1><label></HL1>E-mail<br/>
    <input type="text" size="25" name="email" />
    <HL1></label></HL1>
</div>

<div class="text">
    <HL1><label></HL1>Comment <br/>
    <textarea rows="5" cols="50" name="comment"></textarea>
    <HL1></label></HL1>
</div> 
"""

example_info3.script      = """"""

example_info3.style       = """
   <style type="text/css">
div.text label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
  margin-bottom: 1.25em;
}

div.text input {
  margin: 0;
  padding: 0;
}
  </style>
"""

example3 = create_example(example_info3)

# =============================
# Example 4
# =============================
order += 1

example_info4             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info4.title       = '@input[type=text]@ - Labeling text fields and @textarea@ elements using @title@ attribute'
example_info4.permanent_slug = 'text4'

example_info4.description = """
* Text form controls using the @title@ attribute to @label@ the text box.
* This is a poor practice since it is not part of the HTML specifications to use title attribute to @label@ form controls
* The @title@ attribute is used by some developers to improve accessibility since many screen readers will use the attribute if @label@ element markup is not found.
* Using the @title@ attribute to @label@ form controls is usefule in some limited cases where @hidden@ labeling techniques cannot be used in high density forms layed out in tables.
"""

example_info4.keyboard    = """
"""

example_info4.markup = [m1,m2]

rr4 = rule_reference_object("CONTROL_1", "pass", "pass", "", "", "")

example_info4.rule_references = [rr4]

example_info4.html        = """
<div class="text">
    <div class="label">Name</div>
    <input type="text" size="30" name="name" <HL1>title="<HL2>Name</HL2>"</HL1>/>
</div>

<div class="text">
    <div class="label">E-mail</div>
    <input type="text" size="25" name="email" <HL1>title="<HL2>E-mail</HL2>"</HL1>/>
</div>

<div class="text">
    <div class="label">Comment</div>
    <textarea rows="5" cols="50" name="comment" <HL1>title="<HL2>Comment</HL2>"</HL1>></textarea> 
"""

example_info4.script      = """"""

example_info4.style       = """
  <style type="text/css">
div.text div.label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  font-size: 100%;
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;@input[type=file]@ - Labeling using @label@ element and @for@ attribute to reference file fields'
  margin-left: 20px;
  margin-bottom: 1.25em;
}

  </style>
"""

example4 = create_example(example_info4)

# =============================
# Example 5
# =============================
order += 1

example_info5             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info5.title       = '@input[type=text]@ - Labeling using @label@ element and @for@ attribute to reference text fields and @textarea@ elements'
example_info5.permanent_slug = 'text5'

example_info5.description = """
* Text box form controls are labeled using the @label@ element, the @label.for@ attribute and the @input.id@ attribute.
* The @input.id@ attribute values on form controls need to be unique within the web page (Note: all id attribute values need to be unique for a eb page to validate).
* CSS is used to align @labels@ above the text boxes and to provide vertical separation between the text boxes.
"""
example_info5.keyboard    = """
"""

example_info5.markup = [m1,m2]

rr5 = rule_reference_object("CONTROL_1", "pass", "pass", "", "", "")

example_info5.rule_references = [rr5]

example_info5.html        = """
<div class="text">
    <<HL1>label for="<HL2>name</HL2>"</HL1> >Name</label>
    <input type="text" size="30" name="name" <HL1>id="<HL2>name</HL2>"</HL1>/>
</div>

<div class="text">
    <label for="email">E-mail</label>
    <input type="text" size="25" name="email" <HL1>id="<HL2>email</HL2>"</HL1>/>
</div>

<div class="text">
    <<HL1>label for="<HL2>comment</HL2>"</HL1>>Comment</label>
    <textarea rows="5" cols="50" name="comment" <HL1>id="<HL2>comment</HL2>"</HL1>></textarea>
</div> 
"""

example_info5.script      = """"""

example_info5.style       = """
  <style type="text/css">
div.text label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: 1.25em;
  display: block;
}

  </style>
"""

example5 = create_example(example_info5)

# =============================
# Example 6
# =============================
order += 1

example_info6             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info6.title       = '@input[type=text]@ - highlighting text fields and @textarea@ elements when they receive keyboard focus'
example_info6.permanent_slug = 'text6'

example_info6.description = """
* CSS styling of input to make it easier to identify when control has focus and so it scales better when zooming.
* CSS @font-size@ property with the value of 100% to support zooming. 
* CSS background-color property on the CSS pseudo properties @:focus@ and @:active.to@ set background color of control when it receives keyboard focus.
* CSS background-color property on the CSS pseudo property @:hover@ to mimic the styling effects of keyboard focus.
"""
example_info6.keyboard    = """
"""

m3 = ElementDefinition.objects.get(spec=spec_css21, element=':active')
m4 = ElementDefinition.objects.get(spec=spec_css21, element=':hover')
m5 = ElementDefinition.objects.get(spec=spec_css21, element=':focus')
m6 = ElementDefinition.objects.get(spec=spec_css21, element='background')
m7 = ElementDefinition.objects.get(spec=spec_css21, element='border-color')


example_info6.markup = [m1,m2,m3,m4,m5,m6,m7]

rr6 = rule_reference_object("CONTROL_1","pass", "pass", "", "", "")

example_info6.rule_references = [rr6]

example_info6.html        = """
 <div class="text">
    <HL1><label for="<HL2>name</HL2>"></HL1>Name</label>
    <input type="text" size="30" name="name" <HL1>id="<HL2>name</HL2>"</HL1>/>
</div>

<div class="text">
    <HL1><label for="<HL2>email</HL2>"></HL1> E-mail</label>
    <input type="text" size="25" name="email" <HL1>id="<HL2>email</HL2>"</HL1> />
</div>

<div class="text">
    <HL1><label for="<HL2>comment</HL2>"></HL1> Comment</label>
    <textarea rows="5" cols="50" name="comment" <HL1>id="<HL2>comment</HL2>"</HL1> ></textarea>
</div> 
"""

example_info6.script      = """"""

example_info6.style       = """
   <style type="text/css">
div.text label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: .5em;
  display: block;
  <HL1>font-size: 100%;</HL1>
}

<HL1>
input:active,
input:focus,
input:hover,
textarea:active,
textarea:focus,
textarea:hover{
  background-color: lightyellow;
  border-color: yellow;
}
</HL1>
  </style>
"""

example6 = create_example(example_info6)

# =============================
# Example 7 
# =============================
order += 1

example_info7             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info7.title       = '@input[type=text]@ - using CSS to right justify text fields and @textarea@ elements'
example_info7.permanent_slug = 'text7'

example_info7.description = """
* CSS styling of @label@ element for right justification of label with control.
"""
example_info7.keyboard    = """
"""

m8 = ElementDefinition.objects.get(spec=spec_css21, element='right')

example_info7.markup = [m1,m2,m3,m4,m5,m6,m7,m8]

rr4 = rule_reference_object("CONTROL_1", "pass", "pass", "", "", "")

example_info7.rule_references = [rr4]

example_info7.html        = """
 <div class="text">
    <HL1><label for="<HL2>name</HL2>"></HL1>Name</label>
    <input type="text" size="30" name="name" <HL1>id="<HL2>name</HL2>"</HL1>/>
</div>

<div class="text">
    <HL1><label for="<HL2>email"></HL1>E-mail</label>
    <input type="text" size="25" name="email" <HL1>id="<HL2>email</HL2>"</HL1>/>
</div>

<div class="text">
    <HL1><label for="<HL2>comment</HL2>"></HL1>Comment</label>
    <textarea rows="5" cols="50" name="comment" <HL1>id="<HL2>comment</HL2>"</HL1>></textarea>
</div> 
"""

example_info7.script      = """"""

example_info7.style       = """

  <style type="text/css">

<HL1>div.text {
  margin: 0;
  padding: 0;
  padding-bottom: 1.25em;
}</HL1>

div.text label {
  margin: 0;
  padding: 0;
  display: block;
  font-size: 100%;
  <HL1>padding-top: .1em;
  padding-right: .25em;
  width: 6em;
  text-align: right;
  float: left;</HL1>
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  display: block;
  font-size: 100%;
}

input:active,
input:focus,
input:hover,
textarea:active,
textarea:focus,
textarea:hover {
  background-color: lightyellow;
  border-color: yellow;
}

  </style>
"""

example7 = create_example(example_info7)

# =============================
# Example 8
# =============================
order += 1

example_info8             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info8.title       = '@input[type=text]@ - using CSS to left justify text fields and @textarea@ elements'
example_info8.permanent_slug = 'text8'

example_info8.description = """
* CSS styling of @label@ element for left justification of label with control
"""
example_info8.keyboard    = """
"""

m9 = ElementDefinition.objects.get(spec=spec_css21, element='left')

example_info8.markup = [m1,m2,m3,m4,m5,m6,m7,m9]

example_info8.html        = """
<div class="text">
    <HL1><label for="<HL2>name</HL2>"></HL1>Name</label>
    <input type="text" size="30" name="name" <HL1>id="<HL2>name</HL2>"</HL1>/>
</div>

<div class="text">
    <HL1><label for="<HL2>email</HL2>"></HL1>E-mail</label>
    <input type="text" size="25" name="email" <HL1>id="<HL2>email</HL2>"</HL1>/>
</div>

<div class="text">
    <HL1><label for="<HL2>comment</HL2>"></HL1>Comment</label>
    <textarea rows="5" cols="50" name="comment" <HL1>id="<HL2>comment</HL2>"</HL1> ></textarea>
</div> 
"""

example_info8.script      = """"""

example_info8.style       = """
  <style type="text/css">

<HL1>
div.text {
  margin: 0;
  padding: 0;
  padding-bottom: 1.25em;
}</HL1>

div.text label {
  margin: 0;
  padding: 0;
  display: block;
  font-size: 100%;
  <HL1>
  padding-top: .1em;
  padding-right: .25em;
  width: 6em;
  text-align: left;
  float: left;
  </HL1>
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  display: block;
  font-size: 100%;
}

input:active,
input:focus,
input:hover,
textarea:active,
textarea:focus,
textarea:hover {
  background-color: lightyellow;
  border-color: yellow;
}  </style>
"""

example8 = create_example(example_info8)

# =============================
# Example 9
# =============================
order += 1

example_info9             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info9.title       = '@input[type=text]@ - using an @img@ element @alt@ attribute to indicate required text field and @textarea@ elements'
example_info9.permanent_slug = 'text9'

example_info9.description = """
* The image "required" used to visually indicate a text box is required is included as part of the @label@.
* The value of the @alt@ attribute is "required".
"""
example_info9.keyboard    = """
"""


example_info9.markup = [m1,m2]

example_info9.html        = """
<div class="inst">
    <img src="images/required.png" alt="required imemail"/> Indicates required fields.
</div>

<div class="text">
    <label for="name">Name <img src="images/required.png" <HL1>alt="required"</HL1>/></label>
    <input type="text" size="30" name="name" id="name"/>
</div>

<div class="text">
    <label for="email">E-mail <img src="images/required.png" <HL1>alt="required"</HL1>/></label>
    <input type="text" size="25" name="email" id="email"/>
</div>


<div class="text">
    <label for="comment">Comment <img src="images/required.png" <HL1>alt="required"</HL1>/></label>
    <textarea rows="5" cols="50" id="comment" name="comment"></textarea>
</div> 
"""

example_info9.script      = """"""

example_info9.style       = """
   <style type="text/css">
div.inst {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: 1em;
}

div.text label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: .5em;
  display: block;
  font-size: 100%;
}

input:active,
input:focus,
input:hover,
textarea:active,
textarea:focus,
textarea:hover {
  background-color: lightyellow;
  border-color: yellow;
}

  </style>
"""

example9 = create_example(example_info9)

# =============================
# Example 10
# =============================
order += 1

example_info10             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info10.title       = '@input[type=text]@ - using an @img@ element a @label@ with @hidden@ attributes to indicate required text fields and @textarea@ element'
example_info10.permanent_slug = 'text10'

example_info10.description = """
* The image "required" out side the @label.element@ due to visual rendering of the image after the text box, in this case the @alt@ attribute value is set to empty, since the required information is "hidden" in the label element.
* The word "required" is included as part of the @label@, but is hidden using CSS absolute positioning.
* Note: Do not use the CSS display property with the @value@ "none" to hide the word "require". Using display property also hides the content from assistive technologies./li> 
"""
example_info10.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')
spec_html5 = LanguageSpec.objects.get(url_slug='html5')
spec_aria = LanguageSpec.objects.get(url_slug='aria10')

m10 = ElementDefinition.objects.get(spec=spec_css21, element='position')


example_info10.markup = [m1,m2,m10]

example_info10.html        = """
<div class="inst">
    <img src="images/required.png" alt="required imemail"/> Indicates required fields.
</div>

<div class="text">
    <label for="name">Name <span class="hidden">required</span></label>
    <div><input type="text" size="30" name="name" id="name"/><img src="images/required.png" alt=""/></div>
</div>

<div class="text">
    <label for="email">E-mail <span class="hidden">required</span></label>
    <div><input type="text" size="25" name="email" id="email"/><img src="images/required.png" alt=""/></div>
</div>

<div class="text">
    <label for="comment">Comment <span class="hidden">required</span> <img src="images/required.png" alt=""/></label>
    <textarea rows="5" cols="50" id="comment" name="comment"></textarea>
</div> 
"""

example_info10.script      = """"""

example_info10.style       = """
   <style type="text/css">

span.hidden  {
  position: absolute;
  top: -20em;
  left: -300em;
}


div.inst {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: 1em;
}

div.text label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: .5em;
  font-size: 100%;
}

div.text img {
  margin: 0;
  padding: 0;
  padding-left: .25em;
}

input:active,
input:focus,
input:hover,
textarea:active,
textarea:focus,
textarea:hover {
  background-color: lightyellow;
  border-color: yellow;
}

  </style>
"""

example10 = create_example(example_info10)

# =============================
# Example 11
# =============================
order += 1

example_info11             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info11.title       = '@input[type=text]@ - using an @img@ element a @label@ with @hidden@ attributes to indicate invalid text fields and @textarea@ element'
example_info11.permanent_slug = 'text11'

example_info11.description = """
* The @alt@ value of image "required invalid" is set to empty, since the invalid information is "hidden" in the @label@ element.
* The word "invalid" and the invalid message is included as part of the @label@, but is hidden using CSS @absolute@ positioning.
* The visible invalid information includes the word "invalid" to make sure people with visual impairments and color blindness are able to identify the purpose of the message.
* Note: Do not use the CSS display property with the value "none" to hide the word "require". Using display property also hides the content from assistive technologies./li> 
"""
example_info11.keyboard    = """
"""

m1 = ElementDefinition.objects.get(spec=spec_html4, element='input', value='text')

example_info11.markup = [m1,m2]

example_info11.html        = """
 <div class="inst">
    <img src="images/required.png" alt="required imemail"/> Indicates required fields.
</div>

<div class="text">
    <label for="name">Name <HL1><span class="hidden">Invalid: Names cannot contain numbers or punctuation characters</span></HL1></label>
    <div><input class="invalid" type="text" size="30" name="name" id="name" value="Mike4"/><img src="images/required-invalid.png" alt=""/></div>
    <div class="invalid"><strong>Invalid:</strong> Names cannot contain numbers or punctuation characters</div>
</div>

<div class="text">
    <label for="email">E-mail <HL1><span class="hidden">Invalid: you must supply a valid e-mail address for you to track any responses to the comment</span></HL1> </label>
    <div><input class="invalid" type="text" size="25" name="email" id="email" value="joe.smith#nowhere.net"/><img src="images/required-invalid.png" alt=""/></div>
    <div class="invalid"><strong>Invalid:</strong>You must supply a valid e-mail address for you to track any responses to the comment</div>
</div>

<div class="text">
    <label for="comment">Comment <HL1><span class="hidden">Invalid: You must include a comment</span></HL1></label>
    <textarea class="invalid" rows="5" cols="50" id="comment" name="comment"></textarea>
    <div class="invalid"><strong>Invalid:</strong> You must include a comment</div>
</div> 
"""

example_info11.script      = """"""

example_info11.style       = """
  <style type="text/css">
<HL1>
span.hidden  {
  position: absolute;
  top: -20em;
  left: -300em;
}

.invalid {
  color: red;
}

input.invalid,
textarea.invalid {
  color: black;
  background-color: #FFA0A0;
}
</HL1>
div.inst,
div.invalid {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: 1em;
}

div.text label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: .5em;
  font-size: 100%;
}

div.text img {
  margin: 0;
  padding: 0;
  padding-left: .25em;
}

input:active,
input:focus,
input:hover,
textarea:active,
textarea:focus,
textarea:hover {
  background-color: lightyellow;
  border-color: yellow;
}

  </style>
"""

example11 = create_example(example_info11)

# =============================
# Example 12
# =============================
order += 1

example_info12             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info12.title       = '@input[type=text]@ - @div@ element starts the tab inedex before the text fields and @textarea@ elements'
example_info12.permanent_slug = 'text12'

example_info12.description = """
* The tabindex technique to make instructions more accessible, but is considered a poor accessibility practice since it adds additional tab stops for all keyboard users and the tabindex technique is not supported by all browser and assistive technology combinations.
* The tabindex attribute with a value equal to or greater than 0 can be used in Internet Explorer and other browser to set focus to non-link and non-form controls as the user tabs through a web site. 
"""
example_info12.keyboard    = """
"""

example_info12.markup = [m1,m2]

example_info12.html        = """

<div class="inst" <HL1>tabindex="0" </HL1>>
  Name can only contain letters.    
</div>

<div class="text">
    <label for="name">Name </label>
    <input type="text" size="30" name="name" id="name" />
</div>

<div class="inst" <HL1>tabindex="0"</HL1>>
  E-mail will only be used to send you copy of your commment and allow us send you a response.  
</div>

<div class="text">
    <label for="email">E-mail </label>
    <input type="text" size="25" name="email" id="email" />
</div>

<div class="inst" <HL1>tabindex="0"</HL1>>
   Please comment on the services and resources you found on this web site.
</div>

<div class="text">
    <label for="comment">Comment </label>
    <textarea rows="5" cols="50" name="commnet" id="comment" ></textarea>
</div> 
"""

example_info12.script      = """"""

example_info12.style       = """
   <style type="text/css">

div.inst {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-top: .75em;
  margin-bottom: .25em;
  font-size: 80%;
  font-style: italic;
}


div.text label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
  font-weight: bold;
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: .5em;
  font-size: 100%;
}

div.text img {
  margin: 0;
  padding: 0;
  padding-left: .25em;
}

input:active,
input:focus,
input:hover,
textarea:active,
textarea:focus,
textarea:hover {
  background-color: lightyellow;
  border-color: yellow;
}

  </style>
"""

example12 = create_example(example_info12)

# =============================
# Example 13
# =============================
order += 1

example_info13             = example_object()
example_info.order       = order
example_info.example_groups = [eg_labeling]
example_info13.title       = '@input[type=text]@ - Instructions for text fields and @textarea@ elements using @hidden@ text'
example_info13.permanent_slug = 'text13'

example_info13.description = """
* The instructions appended to the end of the @label@ content as "@hidden@" text .
* The @hidden@ text technique requires redundant instructions but gives developers more flexibility for visual layout of the instructions. This can be a problem if the instructions are coded by hand, since the author must manually check for consistency. Consistency of hidden and visible instructions can be improved through scripting automation.
* The @hidden@ text technique provides greater interoperability for browsers and assistive technologies.
* No additional tab stops are introduced with the @hidden@ text technique.
"""
example_info13.keyboard    = """
"""


example_info13.markup = [m1,m2]

example_info13.html        = """
<div class="inst">
  Name can only contain letters.    
</div>

<div class="text">
    <label for="name">Name <span class="hidden"> can only contain letters</span></label>
    <input type="text" size="30" name="name" id="name" />
</div>

<div class="inst">
  E-mail will only be used to send you copy of your commment and allow us send you a response.  
</div>

<div class="text">
    <label for="email">E-mail <span class="hidden"> will only be used to send you copy of your commment and allow us send you a response. </span></label>
    <input type="text" size="25" name="email" id="email" />
</div>

<div class="inst">
   Please comment on the services and resources yu found on this web site.
</div>

<div class="text">
    <label for="comment">Comment <span class="hidden"> Please comment on the services and resources yu found on this web site. </span></label>
    <textarea rows="5" cols="50" name="commnet" id="comment" ></textarea>
</div> 
"""

example_info13.script      = """"""

example_info13.style       = """

  <style type="text/css">

span.hidden  {
  position: absolute;
  top: -20em;
  left: -300em;
}


div.inst {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-top: .75em;
  margin-bottom: .25em;
  font-size: 80%;
  font-style: italic;
}


div.text label {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  display: block;
  font-size: 100%;
  font-weight: bold;
}

div.text input,
div.text textarea {
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-bottom: .5em;
  font-size: 100%;
}

div.text img {
  margin: 0;
  padding: 0;
  padding-left: .25em;
}


input:active,
input:focus,
input:hover,
textarea:active,
textarea:focus,
textarea:hover {
  background-color: lightyellow;
  border-color: yellow;
}

  </style>
"""

example13 = create_example(example_info13)
