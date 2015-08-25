"""tdis file is for populating tde database witd projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples_common import *


# =============================
# Example 1
# =============================


eg_dtables = ExampleGroup.objects.get(slug="dtables")

example_info             = example_object()
example_info.order          = 3
example_info.example_groups = [eg_dtables]
example_info.title       = 'Simple Data Table without column header th'
example_info.permanent_slug = 'dtable'

example_info.description = """
Simple example of a Data Table that is inaccessible due to a lack of column headers.
"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

example_info.aria_labelledby = True
example_info.aria_styling = True

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-describedby')

example_info.markup = [m1]

rr1 = rule_reference_object("TABLE_1", "fail", "fail", "", "", "")
rr2 = rule_reference_object("TABLE_4", "pass", "pass", "TABLE_4_T1", "", "")
rr3 = rule_reference_object("TABLE_5", "fail", "fail", "", "", "")
rr4 = rule_reference_object("TABLE_6", "fail", "fail", "", "", "")
rr5 = rule_reference_object("TABLE_2", "pass", "pass", "TABLE_2_T1", "", "")

example_info.rule_references = [rr1,rr2,rr3,rr4,rr5]



example_info.rule_references = [rr1,rr2,rr3,rr4,rr5]

example_info.html     = """
  <table>
    <caption>Big 10 Basketball Rankings</caption>
    <tr class='even'>
      <td>TEAM</td>
      <td>CONF</td>
      <td>OVERALL</td>   
    </tr>
   
    <tr class='odd'>
      <td>Michigan State</td>
      <td>5-0</td>
      <td>16-1</td>
    </tr>

    <tr class='even'>
      <td>Michigan</td>
      <td>4-0</td>
      <td>12-4</td>
    </tr>

    <tr class='odd'>
      <td>Wisconsin</td>
      <td>3-1</td>
      <td>16-1</td>
    </tr>

    <tr class='even'>
      <td>Iowa</td>
      <td>3-1</td>
      <td>14-3</td>
    </tr>

    <tr class='odd'>
      <td>Ohio State</td>
      <td>2-2</td>
      <td>15-2</td>
    </tr>

    <tr class='even'>
      <td>Minnesota</td>
      <td>2-2</td>
      <td>13-4</td>
    </tr>

    <tr class='odd'>
      <td>Indiana</td>
      <td>2-2</td>
      <td>12-5</td>
    </tr>

    <tr class='even'>
      <td>Purdue</td>
      <td>2-2</td>
      <td>12-5</td>
    </tr>

    <tr class='odd'>
      <td>Illinois</td>
      <td>2-3</td>
      <td>13-5</td>
    </tr>

    <tr class='even'>
      <td>Northwestern</td>
      <td>1-4</td>
      <td>8-10</td>
    </tr>

    <tr class='odd'>
      <td>Nebraska</td>
      <td>0-4</td>
      <td>8-8</td>
    </tr>

    <tr class='even'>
      <td>Penn State</td>
      <td>0-5</td>
      <td>9-9</td>
    </tr>

 </table> 
"""

example_info.script   = """






"""

example_info.style    = """
#example_html table{
  border-left: 1px solid #808080;
  border-right: 1px solid #808080;
  border-bottom: 1px solid #808080;
}

#example_html table td {
  padding: .125em;
  margin: 0;
  widtd: 10%;
  background-color: #FFFFFF;
  border-right: 1px solid #C0C0C0;
  border-top: 1px solid #C0C0C0;
  border-bottom: 1px solid #C0C0C0;
}

#example_html table.odd {
  background-color: #C0C0C0;
}

"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='dtables').examples.add(example1)
