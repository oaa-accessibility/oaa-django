"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples_common import *


# =============================
# Example 1
# =============================

order = 7

eg_dtables = ExampleGroup.objects.get(slug="dtables")

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_dtables]
example_info.title       = 'Naming Data Tables using caption'
example_info.permanent_slug = 'dtable1'

example_info.description = """
Simple example of a data table named with a caption
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
  <caption>Big 10 Basketball Standings</caption>
    <tr>
      <th>TEAM</th>
      <th>CONF</th>
      <th>OVERALL</th>   
    </tr>
   
    <tr class='odd'>
      <th>Michigan State</th>
      <td>5-0</td>
      <td>16-1</td>
    </tr>

    <tr>
      <th>Michigan</th>
      <td>4-0</td>
      <td>12-4</td>
    </tr>

    <tr class='odd'>
      <th>Wisconsin</th>
      <td>3-1</td>
      <td>16-1</td>
    </tr>

    <tr>
      <th>Iowa</th>
      <td>3-1</td>
      <td>14-3</td>
    </tr>

    <tr class='odd'>
      <th>Ohio State</th>
      <td>2-2</td>
      <td>15-2</td>
    </tr>

    <tr>
      <th>Minnesota</th>
      <td>2-2</td>
      <td>13-4</td>
    </tr>

    <tr class='odd'>
      <th>Indiana</th>
      <td>2-2</td>
      <td>12-5</td>
    </tr>

    <tr>
      <th>Purdue</th>
      <td>2-2</td>
      <td>12-5</td>
    </tr>

    <tr class='odd'>
      <th>Illinois</th>
      <td>2-3</td>
      <td>13-5</td>
    </tr>

    <tr>
      <th>Northwestern</th>
      <td>1-4</td>
      <td>8-10</td>
    </tr>

    <tr class='odd'>
      <th>Nebraska</th>
      <td>0-4</td>
      <td>8-8</td>
    </tr>

    <tr>
      <th>Penn State</th>
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

#example_html table td, table th {
  padding: .125em;
  margin: 0;
  width: 10%;
  border-right: 1px solid #C0C0C0;
  border-top: 1px solid #C0C0C0;
  border-bottom: 1px solid #C0C0C0;
  padding: 5px 5px 5px 5px;
}

#example_html table tr{
  background: #FFFFFF;
}

#example_html table tr.odd {
  background: #E0E0E0;
}

"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='dtables').examples.add(example1)

# =============================
# Example 2
# =============================

order = 6

eg_dtables = ExampleGroup.objects.get(slug="dtables")

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_dtables]
example_info.title       = 'Naming Data Tables using aria-labelledby'
example_info.permanent_slug = 'dtable2'

example_info.description = """
Simple example of a data table named with aria-labelledby.
"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

example_info.aria_labelledby = True
example_info.aria_styling = True

rr1 = rule_reference_object("TABLE_1", "pass", "pass", "TABLE_1_T1", "", "")
rr3 = rule_reference_object("TABLE_5", "pass", "pass", "TABLE_5_T1", "", "")
rr4 = rule_reference_object("TABLE_6", "pass", "pass", "TABLE_6_T1", "", "")
rr5 = rule_reference_object("TABLE_2", "pass", "pass", "TABLE_2_T3", "", "")

example_info.rule_references = [rr1,rr3,rr4,rr5]

example_info.html     = """
<h2 id="id_big10">Big 10 Basketball Standings</h2> 
 
  <table aria-labelledby="id_big10">
    <tr>
      <th>TEAM</th>
      <th>CONF</th>
      <th>OVERALL</th>   
    </tr>
   
    <tr class='odd'>
      <th>Michigan State</th>
      <td>5-0</td>
      <td>16-1</td>
    </tr>

    <tr>
      <th>Michigan</th>
      <td>4-0</td>
      <td>12-4</td>
    </tr>

    <tr class='odd'>
      <th>Wisconsin</th>
      <td>3-1</td>
      <td>16-1</td>
    </tr>

    <tr>
      <th>Iowa</th>
      <td>3-1</td>
      <td>14-3</td>
    </tr>

    <tr class='odd'>
      <th>Ohio State</th>
      <td>2-2</td>
      <td>15-2</td>
    </tr>

    <tr>
      <th>Minnesota</th>
      <td>2-2</td>
      <td>13-4</td>
    </tr>

    <tr class='odd'>
      <th>Indiana</th>
      <td>2-2</td>
      <td>12-5</td>
    </tr>

    <tr>
      <th>Purdue</th>
      <td>2-2</td>
      <td>12-5</td>
    </tr>

    <tr class='odd'>
      <th>Illinois</th>
      <td>2-3</td>
      <td>13-5</td>
    </tr>

    <tr>
      <th>Northwestern</th>
      <td>1-4</td>
      <td>8-10</td>
    </tr>

    <tr class='odd'>
      <th>Nebraska</th>
      <td>0-4</td>
      <td>8-8</td>
    </tr>

    <tr>
      <th>Penn State</th>
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

#example_html table td, table th {
  padding: .125em;
  margin: 0;
  width: 10%;
  border-right: 1px solid #C0C0C0;
  border-top: 1px solid #C0C0C0;
  border-bottom: 1px solid #C0C0C0;
  padding: 5px 5px 5px 5px;
}

#example_html table tr{
  background: #FFFFFF;
}

#example_html table tr.odd {
  background: #E0E0E0;
}

"""

example2 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example2, script1 )

ExampleGroup.objects.get(slug='dtables').examples.add(example1)


# =============================
# Example 3
# =============================

order = 5

eg_dtables = ExampleGroup.objects.get(slug="dtables")

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_dtables]
example_info.title       = 'Naming Data Tables using aria-label'
example_info.permanent_slug = 'dtable3'

example_info.description = """
Simple example of a data table named with aria-label.
"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

example_info.aria_labelledby = True
example_info.aria_styling = True

rr1 = rule_reference_object("TABLE_1", "pass", "pass", "TABLE_1_T1", "", "")
rr3 = rule_reference_object("TABLE_5", "pass", "pass", "TABLE_5_T1", "", "")
rr4 = rule_reference_object("TABLE_6", "pass", "pass", "TABLE_6_T1", "", "")
rr5 = rule_reference_object("TABLE_2", "pass", "pass", "TABLE_2_T2", "", "")



example_info.rule_references = [rr1,rr3,rr4,rr5]

example_info.html     = """
  <h2>Big 10 Basketball Standings</h2>
   <table aria-label="big 10 standings">
    <tr>
      <th>TEAM</th>
      <th>CONF</th>
      <th>OVERALL</th>   
    </tr>
   
    <tr class='odd'>
      <th>Michigan State</th>
      <td>5-0</td>
      <td>16-1</td>
    </tr>

    <tr>
      <th>Michigan</th>
      <td>4-0</td>
      <td>12-4</td>
    </tr>

    <tr class='odd'>
      <th>Wisconsin</th>
      <td>3-1</td>
      <td>16-1</td>
    </tr>

    <tr>
      <th>Iowa</th>
      <td>3-1</td>
      <td>14-3</td>
    </tr>

    <tr class='odd'>
      <th>Ohio State</th>
      <td>2-2</td>
      <td>15-2</td>
    </tr>

    <tr>
      <th>Minnesota</th>
      <td>2-2</td>
      <td>13-4</td>
    </tr>

    <tr class='odd'>
      <th>Indiana</th>
      <td>2-2</td>
      <td>12-5</td>
    </tr>

    <tr>
      <th>Purdue</th>
      <td>2-2</td>
      <td>12-5</td>
    </tr>

    <tr class='odd'>
      <th>Illinois</th>
      <td>2-3</td>
      <td>13-5</td>
    </tr>

    <tr>
      <th>Northwestern</th>
      <td>1-4</td>
      <td>8-10</td>
    </tr>

    <tr class='odd'>
      <th>Nebraska</th>
      <td>0-4</td>
      <td>8-8</td>
    </tr>

    <tr>
      <th>Penn State</th>
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

#example_html table td, table th {
  padding: .125em;
  margin: 0;
  width: 10%;
  border-right: 1px solid #C0C0C0;
  border-top: 1px solid #C0C0C0;
  border-bottom: 1px solid #C0C0C0;
  padding: 5px 5px 5px 5px;
}

#example_html table tr{
  background: #FFFFFF;
}

#example_html table tr.odd {
  background: #E0E0E0;
}
"""

example3 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='dtables').examples.add(example1)
