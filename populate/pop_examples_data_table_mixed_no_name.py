"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples_common import *


# =============================
# Example 1
# =============================

order = 1

eg_mtables = ExampleGroup.objects.get(slug="mtables")

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_mtables]
example_info.title       = 'Nested tables without accessible names'
example_info.permanent_slug = 'mtable4'

example_info.description = """

"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')

example_info.markup = [m1]

rr1 = rule_reference_object("TABLE_1", "pass", "pass", "TABLE_1_T1", "", "")
rr2 = rule_reference_object("TABLE_4", "fail", "fail", "", "", "")
rr3 = rule_reference_object("TABLE_5", "pass", "pass", "TABLE_5_T1", "", "")
rr4 = rule_reference_object("TABLE_6", "pass", "pass", "TABLE_6_T1", "", "")
rr5 = rule_reference_object("TABLE_2", "fail", "fail", "", "", "")
rr6 = rule_reference_object("LAYOUT_3", "pass","pass", "LAYOUT_3_T1", "", "")

example_info.rule_references = [rr1,rr2,rr3,rr4,rr5,rr6]

example_info.html     = """

<table role="presentation">
  <tr role="presentation"><h1 id="id_rankings">NCAA Basketball Rankings by Conference</h1></tr>
  </tr>
  <tr role="presentation">
    <td role="presentation">
    <h2 id="id_big10">Big 10</h2>
      <table>
        <tr>
          <th>Team</th>
          <th>Conf</th>
          <th>Overall</th>   
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

    </td>
    <td role="presentation">
    <h2 id="id_big12">Big 12</h2>
      <table>
        <tr>
          <th>Team</th>
          <th>Conf</th>
          <th>Overall</th>   
        </tr>

        <tr class='odd'>
          <th>Kansas</th>
          <td>3-0</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <th>Oklahoma State</th>
          <td>3-1</td>
          <td>15-2</td>   
        </tr>

        <tr class='odd'>
          <th>Kansas State</th>
          <td>3-1</td>
          <td>13-4</td>   
        </tr>

        <tr>
          <th>Iowa State</th>
          <td>2-2</td>
          <td>14-2</td>   
        </tr>

        <tr class='odd'>
          <th>Oklahoma</th>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr>
          <th>Texas</th>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr class='odd'>
          <th>West Virginia</th>
          <td>2-2</td>
          <td>10-7</td>   
        </tr>

        <tr>
          <th>Baylor</th>
          <td>1-2</td>
          <td>1-3</td>   
        </tr>

        <tr class='odd'>
          <th>Texas Tech</th>
          <td>1-3</td>
          <td>9-8</td>   
        </tr>

        <tr>
          <th>TCU</th>
          <td>0-4</td>
          <td>9-7</td>   
        </tr>
      </table>
    </td>
    <td role="presentation">
    <h2 id="id_sec">SEC</h2>
      <table>
        <tr>
          <th>Team</th>
          <th>Conf</th>
          <th>Overall</th>   
        </tr>

        <tr class='odd'>
          <th>Florida</th>
          <td>3-0</td>
          <td>14-2</td>   
        </tr>

        <tr>
          <th>Texas A&M</th>
          <td>3-0</td>
          <td>12-4</td>   
        </tr>

        <tr class='odd'>
          <th>Kentucky</th>
          <td>2-1</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <th>Ole Miss</th>
          <td>2-1</td>
          <td>11-5</td>   
        </tr>

        <tr class='odd'>
          <th>Tennessee</th>
          <td>2-1</td>
          <td>11-5</td>   
        </tr>

        <tr>
          <th>Georgia</th>
          <td>2-1</td>
          <td>8-7</td>   
        </tr>

        <tr class='odd'>
          <th>Alabama</th>
          <td>2-1</td>
          <td>8-8</td>   
        </tr>

        <tr>
          <th>Missouri</th>
          <td>1-1</td>
          <td>13-2</td>   
        </tr>

        <tr class='odd'>
          <th>Arkansas</th>
          <td>1-2</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <th>Mississippi State</th>
          <td>1-2</td>
          <td>11-5</td>   
        </tr>

        <tr class='odd'>
          <th>LSU</th>
          <td>1-2</td>
          <td>10-5</td>   
        </tr>

        <tr>
          <th>Vanderbilt</th>
          <td>0-2</td>
          <td>8-6</td>   
        </tr>

        <tr class='odd'>
          <th>Auburn</th>
          <td>0-3</td>
          <td>8-6</td>   
        </tr>

        <tr>
          <th>South Carolina</th>
          <td>0-3</td>
          <td>7-9</td>   
        </tr>

      </table>
    </td>
  </tr>
  <tr role="presentation">
    <td role="presentation">
    <h2 id="id_pac12">PAC 12</h2>
      <table>
        <tr>
          <th>Team</th>
          <th>Conf</th>
          <th>Overall</th>   
        </tr>

        <tr class='odd'>
          <th>Arizona</th>
          <td>4-0</td>
          <td>17-0</td>   
        </tr>

        <tr>
          <th>California</th>
          <td>4-0</td>
          <td>13-4</td>   
        </tr>

        <tr class='odd'>
          <th>Colorado</th>
          <td>3-1</td>
          <td>14-3</td>   
        </tr>

        <tr>
          <th>UCLA</th>
          <td>2-1</td>
          <td>13-3</td>   
        </tr>

        <tr class='odd'>
          <th>Washington</th>
          <td>3-2</td>
          <td>11-7</td>   
        </tr>

        <tr>
          <th>Arizona State</th>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr class='odd'>
          <th>Stanford</th>
          <td>2-2</td>
          <td>11-5</td>   
        </tr>

        <tr>
          <th>Oregon</th>
          <td>1-3</td>
          <td>13-3</td>   
        </tr>

        <tr class='odd'>
          <th>Utah</th>
          <td>1-3</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <th>Oregon State</th>
          <td>1-3</td>
          <td>9-7</td>   
        </tr>

        <tr class='odd'>
          <th>Washington State</th>
          <td>1-4</td>
          <td>8-9</td>   
        </tr>

        <tr>
          <th>USC</th>
          <td>0-3</td>
          <td>9-7</td>   
        </tr>
      </table>
    </td>

    <td role="presentation">
    <h2 id="id_acc">ACC</h2>
      <table>
        <tr>
          <th>Team</th>
          <th>Conf</th>
          <th>Overall</th>   
        </tr>

        <tr class='odd'>
          <th>Syracuse</th>
          <td>4-0</td>
          <td>17-0</td>   
        </tr>

        <tr>
          <th>Pittsburgh</th>
          <td>4-0</td>
          <td>16-1</td>   
        </tr>

        <tr class='odd'>
          <th>Clemson</th>
          <td>3-1</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <th>Florida State</th>
          <td>3-1</td>
          <td>12-4</td>   
        </tr>

        <tr class='odd'>
          <th>Virginia</th>
          <td>3-1</td>
          <td>12-5</td>   
        </tr>

        <tr>
          <th>Maryland</th>
          <td>3-2</td>
          <td>11-7</td>   
        </tr>

        <tr class='odd'>
          <th>Duke</th>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr>
          <th>Wake Forest</th>
          <td>2-2</td>
          <td>12-5</td>   
        </tr>

        <tr class='odd'>
          <th>NC State</th>
          <td>1-3</td>
          <td>11-6</td>   
        </tr>

        <tr>
          <th>Georgia Tech</th>
          <td>1-3</td>
          <td>10-7</td>   
        </tr>

        <tr class='odd'>
          <th>Notre Dame</th>
          <td>1-3</td>
          <td>10-7</td>   
        </tr>

        <tr>
          <th>Miami (FL)</th>
          <td>1-3</td>
          <td>9-7</td>   
        </tr>

        <tr class='odd'>
          <th>Virginia Tech</th>
          <td>1-3</td>
          <td>8-8</td>   
        </tr>

        <tr>
          <th>Boston College</th>
          <td>1-3</td>
          <td>5-12</td>   
        </tr>

        <tr class='odd'>
          <th>North Carolina</th>
          <td>0-3</td>
          <td>10-6</td>   
        </tr>
      </table>
    </td>
    <td role="presentation">
    <h2 id="id_bigeast">Big East</h2>
      <table>
        <tr>
          <th>Team</th>
          <th>Conf</th>
          <th>Overall</th>   
        </tr>

        <tr class='odd'>
          <th>Creighton</th>
          <td>5-0</td>
          <td>15-2</td>   
        </tr>

        <tr>
          <th>Villanova</th>
          <td>4-0</td>
          <td>15-1</td>   
        </tr>

        <tr class='odd'>
          <th>Xavier</th>
          <td>4-1</td>
          <td>14-4</td>   
        </tr>

        <tr>
          <th>Georgetown</th>
          <td>3-2</td>
          <td>11-5</td>   
        </tr>

        <tr class='odd'>
          <th>Marquette</th>
          <td>2-2</td>
          <td>10-7</td>   
        </tr>

        <tr>
          <th>DePaul</th>
          <td>2-3</td>
          <td>10-8</td>   
        </tr>

        <tr class='odd'>
          <th>Providence</th>
          <td>1-2</td>
          <td>11-5</td>   
        </tr>

        <tr>
          <th>Seton Hall</th>
          <td>1-3</td>
          <td>10-7</td>   
        </tr>

        <tr class='odd'>
          <th>St. John's</th>
          <td>0-4</td>
          <td>9-7</td>   
        </tr>

        <tr>
          <th>Butler</th>
          <td>0-5</td>
          <td>10-7</td>   
        </tr>

      </table>
    </td>
  </tr>
</table>
"""

example_info.script   = """

"""

example_info.style    = """
#example_html table table{
  background-color: #FFFFFF;
}

#example_html table table tr:nth-child(1){
  border-bottom:5px solid #000000;
}

#example_html table table th, table table td{
  padding:5px 5px 5px 5px;
}

#example_html table td {
  vertical-align: text-top;
}

#example_html tr.odd, tr.title {
  background-color: #E0E0E0;
}
"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='mtables').examples.add(example1)
