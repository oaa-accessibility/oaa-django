"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples_common import *


# =============================
# Example 1
# =============================

order = 1

eg_ltables = ExampleGroup.objects.get(slug="ltables")

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_ltables]
example_info.title       = 'Inaccessible Layout Table'
example_info.permanent_slug = 'ltable2'

example_info.description = """
An example of a layout table that is inaccessible.
"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

example_info.aria_labelledby = True
example_info.aria_styling = True


m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')

example_info.markup = [m1]

rr1 = rule_reference_object("LAYOUT_3", "pass", "pass", "LAYOUT_3_T1", "", "")
rr2 = rule_reference_object("LAYOUT_2", "fail", "fail", "", "", "")
rr3 = rule_reference_object("LAYOUT_1", "fail", "fail", "", "", "")


example_info.rule_references = [rr1,rr2,rr3]

example_info.html     = """

<table role="presentation">
 <tr role="presentation">
    <td colspan="5" role="presentation">
      <h1 align="center">Midwestern University</h1>
    </td>
 </tr>

  <tr role="presentation">
    <td rowspan="2" role="presentation">
      <h2>Navigation Menu</h2>
      <ul>
        <li><a href="">LINK 1</a>
        <li><a href="">LINK 2</a>
      </ul>
    </td>
          <td role="presentation"><h2>Study</h2></td>
          <td role="presentation"><h2>Dining</h2></td>
          <td role="presentation"><h2>Clubs</h2></td>
          <td role="presentation"><h2>Events</h2></td>
  </tr>  
          <tr role="presentation">
          <td role="presentation">
            <h3>24/7 computer lab</h3>
              <p>The computer lab in the basement is always available to students</p>
            <h3>Meeting rooms</h3>
              <p>Need a quiet room to host a meeting or review session? There are plenty of meeting rooms available.</p>
          </td>
      
          <td role="presentation">
            <h3>Union Cafe</h3>
              <p>Breakfast: pancakes, waffles, omeletes<br>Lunch and Dinner: burgers, hot dogs, sandwiches</p>
            <h3>Union Bakery</h3>
              <p>Donuts, bagels, muffins, coffee</p>
            <h3>Taste of Italy</h3>
              <p>Authentic pizza and pasta</p>
          </td>

          <td role="presentation">
            <p>There are over 100 registered clubs on campus. Find one that fits you!</p>
            <h3>Want to start your own club?</h3>
            <p>Stop by Union room 149 anytime M-F 9am-5pm for more information on how to start your own organization</p>
          </td>

          <td role="presentation">
            <h3>Student Art Show: 5pm every Tuesday</h3>
              <p>Art students and professors showcase their artwork</p>
            <h3>Q&A with the president: 7pm Tuesday, January 28 at 7pm</h3>
              <p>The president of the University will be hosting a Q&A session in the Union Ballroom. All students are welcome to attend.</p>
            <h3>Free bowling night: 7-10pm Thursday, February 6</h3>
              <p>Come down to the bowling alley in the Union basement for free games of bowling!</p>
          </td>
        </tr>

  <tr role="presentation">
    <td colspan="5" role="presentation">
      <p><h4>2014 Midwestern University Union <br>456 Main Street Cornland, Illinois 60123</h4>
    </td>
  </tr>
</table>

"""

example_info.script   = """

"""

example_info.style    = """
#example_html table {
  border-left: 1px solid #808080;
  border-right: 1px solid #808080;
  border-bottom: 1px solid #808080;
}

#example_html table tr td h3 {
  color: #000080;
}

#example_html table h1 {
  background-color: #000080;
  color: #FFFFFF;
}

#example_html table h2 {
  color: #000080;
}

#example_html table td, table th {
  padding: .125em;
  margin: 0;
  width: 10%;
  background-color: #FFFFFF;
  border-right: 1px solid #C0C0C0;
  border-top: 1px solid #C0C0C0;
  border-bottom: 1px solid #C0C0C0;
  vertical-align: text-top;
}

"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='ltables').examples.add(example1)
