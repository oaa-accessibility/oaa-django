"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples_common import *

 
# =============================
# Example 1
# =============================

order = 2

eg_dtables = ExampleGroup.objects.get(slug="dtables")

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_dtables]
example_info.title       = 'Simple Data Table with row and column headers th'
example_info.permanent_slug = 'dtable7'

example_info.description = """
Simple example of a bus schedule made with a data table using th headers.
"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

example_info.aria_labelledby = True
example_info.aria_styling = True

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-describedby')

example_info.markup = [m1]

rr1 = rule_reference_object("TABLE_1", "pass", "pass", "TABLE_1_T1", "", "")
rr3 = rule_reference_object("TABLE_5", "pass", "pass", "TABLE_5_T1", "", "")
rr4 = rule_reference_object("TABLE_6", "pass", "pass", "TABLE_6_T1", "", "")
rr5 = rule_reference_object("TABLE_2", "pass", "pass", "TABLE_2_T1", "", "")



example_info.rule_references = [rr1,rr3,rr4,rr5]

example_info.html     = """
  <table>
  <caption>Bus Schedule for First Street and Illinois Avenue</caption>
    <tr>
      <th>Route</th>
      <th>Departure Time</th>
      <th>Estimated Arrival</th>   
    </tr>
   
    <tr class='red'>
      <th>25 North Red</th>
      <td>Due</td>
      <td>4:51 PM</td>
    </tr>

    <tr class="red">
      <th>25 South Red</th>
      <td>7 minutes</td>
      <td>4:58 PM</td>
    </tr>

    <tr class="yellow">
      <th>55 W Yellow Shuttle</th>
      <td>9 minutes</td>
      <td>5:00 PM</td>
    </tr>

    <tr class="yellow">
      <th>55 E Yellow Shuttle</th>
      <td>12 minutes</td>
      <td>5:03 PM</td>
    </tr>

    <tr class='air'>
      <th>Airport Express Inbound</th>
      <td>15 minutes</td>
      <td>5:06 PM</td>
    </tr>
 </table> 
"""

example_info.script   = """






"""

example_info.style    = """
#example table caption {
  color: #000099;
}

#example_html table{
  border-left: 3px solid #808080;
  border-right: 3px solid #808080;
  border-bottom: 3px solid #808080;
  border-top: 3px solid #808080;
}

#example_html table td,#example_html table th {
  padding: .125em;
  margin: 0;
  width: 10%;
  border-right: 1px solid #C0C0C0;
  border-top: 1px solid #C0C0C0;
  border-bottom: 1px solid #C0C0C0;
  padding: 5px 5px 5px 5px;
}

#example_html table tr.red {
  background-color: #F08080;
}

#example_html table tr.yellow {
  background-color: #FFEC8B;
}

#example_html table tr.air {
  background-color: #CCFFFF;
}

#example_html table tr.top {
  background-color: #FFFFFF;
  color: #000099;
}

#example_html {
 background-color: #FFFFFF;
}
"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='dtables').examples.add(example1)
