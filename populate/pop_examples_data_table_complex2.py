"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples_common import *


# =============================
# Example 1
# =============================

order = 1

eg_dtables = ExampleGroup.objects.get(slug="dtables")

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_dtables]
example_info.title       = 'Data Table 4'
example_info.permanent_slug = 'dtable4'

example_info.description = """

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
rr2 = rule_reference_object("LAYOUT_2", "fail", "fail", "LAYOUT_2_T3", "", "")
rr3 = rule_reference_object("LAYOUT_1", "fail", "fail", "", "", "")


example_info.rule_references = [rr1,rr2,rr3]

example_info.html     = """

<table role="presentation">
 <tr role="presentation">
    <td colspan="2" role="presentation">
      <h1 align="center">Midwestern University</h1>
    </td>
 </tr>

  <tr role="presentation">
    <td role="presentation">
      <h2>Navigation Menu</h2>
      <ul>
        <li><a href="">LINK 1</a>
        <li><a href="">LINK 2</a>
      </ul>
    </td>

    <td role="presentation">
    <table role="presentation">
        <tr role="presentation">
          <td role="presentation"><h2>Study</h2></td>
            <td role="presentation"><h2>Dining</h2></td>
            <td role="presentation"><h2>Clubs</h2></td>
            <td role="presentation"><h2>Events</h2></td>
          </tr>

        <tr>
          <td role="presentation">
            <h4>24/7 computer lab</h4>
              <p>The computer lab in the basement is always available to students</p>
            <h4>Meeting rooms</h4>
              <p>Need a quiet room to host a meeting or review session? There are plenty of meeting rooms available.</p>
          </td>
      
          <td role="presentation">
            <h4>Union Cafe</h4>
              <p>Breakfast: pancakes, waffles, omeletes<br>Lunch and Dinner: burgers, hot dogs, sandwiches</p>
            <h4>Union Bakery</h4>
              <p>Donuts, bagels, muffins, coffee</p>
            <h4>Taste of Italy</h4>
              <p>Authentic pizza and pasta</p>
          </td>

          <td role="presentation">
            <p>There are over 100 registered clubs on campus. Find one that fits you!</p>
            <h4>Want to start your own club?</h4>
            <p>Stop by Union room 149 anytime M-F 9am-5pm for more information on how to start your own organization</p>
          </td>

          <td role="presentation">
            <h4>Student Art Show: 5pm every Tuesday</h4>
              <p>Art students and professors showcase their artwork</p>
            <h4>Q&A with the president: 7pm Tuesday, January 28 at 7pm</h4>
              <p>The president of the University will be hosting a Q&A session in the Union Ballroom. All students are welcome to attend.</p>
            <h4>Free bowling night: 7-10pm Thursday, February 6</h4>
              <p>Come down to the bowling alley in the Union basement for free games of bowling!</p>
          </td>
        </tr>
      </table>
    </td>   
  </tr>
  <tr role="presentation">
    <td colspan="2" role="presentation">
      <p><h6>2014 Midwestern University Union <br>456 Main Street Cornland, Illinois 60123</h6>
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

#example_html table tr td h4 {
  color: #000080;
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
}

"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='dtables').examples.add(example1)
