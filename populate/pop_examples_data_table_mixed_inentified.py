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
example_info.title       = 'Unidentified Nested Table'
example_info.permanent_slug = 'mtable2'

example_info.description = """
An example of an identified nested data table.
"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')

example_info.markup = [m1]

rr1 = rule_reference_object("TABLE_1", "fail", "fail", "", "", "")
rr2 = rule_reference_object("TABLE_4", "fail", "fail", "", "", "")
rr3 = rule_reference_object("TABLE_5", "fail", "fail", "", "", "")
rr4 = rule_reference_object("TABLE_6", "fail", "fail", "", "", "")
rr5 = rule_reference_object("TABLE_2", "fail", "fail", "", "", "")
rr6 = rule_reference_object("LAYOUT_3", "fail","fail", "", "", "")

example_info.rule_references = [rr1,rr2,rr3,rr4,rr5,rr6]
example_info.html     = """

<table>
  <tr><h1 id="id_rankings">NCAA Basketball Rankings by Conference</h1></tr>
  </tr>
  <tr>
    <td>
    <h2 id="id_big10">Big 10</h2>
      <table>
        <tr>
          <td>Team</td>
          <td>Conf</td>
          <td>Overall</td>   
        </tr>
   
        <tr class='odd'>
          <td>Michigan State</td>
          <td>5-0</td>
          <td>16-1</td>
        </tr>

        <tr>
          <td>Michigan</td>
          <td>4-0</td>
          <td>12-4</td>
        </tr>
  
        <tr class='odd'>
          <td>Wisconsin</td>
          <td>3-1</td>
          <td>16-1</td>
        </tr>

        <tr>
          <td>Iowa</td>
          <td>3-1</td>
          <td>14-3</td>
        </tr>

        <tr class='odd'>
          <td>Ohio State</td>
          <td>2-2</td>
          <td>15-2</td>
        </tr>

        <tr>
          <td>Minnesota</td>
          <td>2-2</td>
          <td>13-4</td>
        </tr>

        <tr class='odd'>
          <td>Indiana</td>
          <td>2-2</td>
          <td>12-5</td>
        </tr>

        <tr>
          <td>Purdue</td>
          <td>2-2</td>
          <td>12-5</td>
        </tr>

        <tr class='odd'>
          <td>Illinois</td>
          <td>2-3</td>
          <td>13-5</td>
        </tr>

        <tr>
          <td>Northwestern</td>
          <td>1-4</td>
          <td>8-10</td>
        </tr>
 
        <tr class='odd'>
          <td>Nebraska</td>
          <td>0-4</td>
          <td>8-8</td>
        </tr>

        <tr>
          <td>Penn State</td>
          <td>0-5</td>
          <td>9-9</td>
        </tr>
      </table> 

    </td>
    <td>
    <h2 id="id_big12">Big 12</h2>
      <table>
        <tr>
          <td>Team</td>
          <td>Conf</td>
          <td>Overall</td>   
        </tr>

        <tr class='odd'>
          <td>Kansas</td>
          <td>3-0</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Oklahoma State</td>
          <td>3-1</td>
          <td>15-2</td>   
        </tr>

        <tr class='odd'>
          <td>Kansas State</td>
          <td>3-1</td>
          <td>13-4</td>   
        </tr>

        <tr>
          <td>Iowa State</td>
          <td>2-2</td>
          <td>14-2</td>   
        </tr>

        <tr class='odd'>
          <td>Oklahoma</td>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr>
          <td>Texas</td>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr class='odd'>
          <td>West Virginia</td>
          <td>2-2</td>
          <td>10-7</td>   
        </tr>

        <tr>
          <td>Baylor</td>
          <td>1-2</td>
          <td>1-3</td>   
        </tr>

        <tr class='odd'>
          <td>Texas Tech</td>
          <td>1-3</td>
          <td>9-8</td>   
        </tr>

        <tr>
          <td>TCU</td>
          <td>0-4</td>
          <td>9-7</td>   
        </tr>
      </table>
    </td>
    <td>
    <h2 id="id_sec">SEC</h2>
      <table>
        <tr>
          <td>Team</td>
          <td>Conf</td>
          <td>Overall</td>   
        </tr>

        <tr class='odd'>
          <td>Florida</td>
          <td>3-0</td>
          <td>14-2</td>   
        </tr>

        <tr>
          <td>Texas A&M</td>
          <td>3-0</td>
          <td>12-4</td>   
        </tr>

        <tr class='odd'>
          <td>Kentucky</td>
          <td>2-1</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Ole Miss</td>
          <td>2-1</td>
          <td>11-5</td>   
        </tr>

        <tr class='odd'>
          <td>Tennessee</td>
          <td>2-1</td>
          <td>11-5</td>   
        </tr>

        <tr>
          <td>Georgia</td>
          <td>2-1</td>
          <td>8-7</td>   
        </tr>

        <tr class='odd'>
          <td>Alabama</td>
          <td>2-1</td>
          <td>8-8</td>   
        </tr>

        <tr>
          <td>Missouri</td>
          <td>1-1</td>
          <td>13-2</td>   
        </tr>

        <tr class='odd'>
          <td>Arkansas</td>
          <td>1-2</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Mississippi State</td>
          <td>1-2</td>
          <td>11-5</td>   
        </tr>

        <tr class='odd'>
          <td>LSU</td>
          <td>1-2</td>
          <td>10-5</td>   
        </tr>

        <tr>
          <td>Vanderbilt</td>
          <td>0-2</td>
          <td>8-6</td>   
        </tr>

        <tr class='odd'>
          <td>Auburn</td>
          <td>0-3</td>
          <td>8-6</td>   
        </tr>

        <tr>
          <td>South Carolina</td>
          <td>0-3</td>
          <td>7-9</td>   
        </tr>

      </table>
    </td>
  </tr>
  <tr>
    <td>
    <h2 id="id_pac12">PAC 12</h2>
      <table>
        <tr>
          <td>Team</td>
          <td>Conf</td>
          <td>Overall</td>   
        </tr>

        <tr class='odd'>
          <td>Arizona</td>
          <td>4-0</td>
          <td>17-0</td>   
        </tr>

        <tr>
          <td>California</td>
          <td>4-0</td>
          <td>13-4</td>   
        </tr>

        <tr class='odd'>
          <td>Colorado</td>
          <td>3-1</td>
          <td>14-3</td>   
        </tr>

        <tr>
          <td>UCLA</td>
          <td>2-1</td>
          <td>13-3</td>   
        </tr>

        <tr class='odd'>
          <td>Washington</td>
          <td>3-2</td>
          <td>11-7</td>   
        </tr>

        <tr>
          <td>Arizona State</td>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr class='odd'>
          <td>Stanford</td>
          <td>2-2</td>
          <td>11-5</td>   
        </tr>

        <tr>
          <td>Oregon</td>
          <td>1-3</td>
          <td>13-3</td>   
        </tr>

        <tr class='odd'>
          <td>Utah</td>
          <td>1-3</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Oregon State</td>
          <td>1-3</td>
          <td>9-7</td>   
        </tr>

        <tr class='odd'>
          <td>Washington State</td>
          <td>1-4</td>
          <td>8-9</td>   
        </tr>

        <tr>
          <td>USC</td>
          <td>0-3</td>
          <td>9-7</td>   
        </tr>
      </table>
    </td>

    <td>
    <h2 id="id_acc">ACC</h2>
      <table>
        <tr>
          <td>Team</td>
          <td>Conf</td>
          <td>Overall</td>   
        </tr>

        <tr class='odd'>
          <td>Syracuse</td>
          <td>4-0</td>
          <td>17-0</td>   
        </tr>

        <tr>
          <td>Pittsburgh</td>
          <td>4-0</td>
          <td>16-1</td>   
        </tr>

        <tr class='odd'>
          <td>Clemson</td>
          <td>3-1</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Florida State</td>
          <td>3-1</td>
          <td>12-4</td>   
        </tr>

        <tr class='odd'>
          <td>Virginia</td>
          <td>3-1</td>
          <td>12-5</td>   
        </tr>

        <tr>
          <td>Maryland</td>
          <td>3-2</td>
          <td>11-7</td>   
        </tr>

        <tr class='odd'>
          <td>Duke</td>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr>
          <td>Wake Forest</td>
          <td>2-2</td>
          <td>12-5</td>   
        </tr>

        <tr class='odd'>
          <td>NC State</td>
          <td>1-3</td>
          <td>11-6</td>   
        </tr>

        <tr>
          <td>Georgia Tech</td>
          <td>1-3</td>
          <td>10-7</td>   
        </tr>

        <tr class='odd'>
          <td>Notre Dame</td>
          <td>1-3</td>
          <td>10-7</td>   
        </tr>

        <tr>
          <td>Miami (FL)</td>
          <td>1-3</td>
          <td>9-7</td>   
        </tr>

        <tr class='odd'>
          <td>Virginia Tech</td>
          <td>1-3</td>
          <td>8-8</td>   
        </tr>

        <tr>
          <td>Boston College</td>
          <td>1-3</td>
          <td>5-12</td>   
        </tr>

        <tr class='odd'>
          <td>North Carolina</td>
          <td>0-3</td>
          <td>10-6</td>   
        </tr>
      </table>
    </td>
    <td>
    <h2 id="id_bigeast">Big East</h2>
      <table>
        <tr>
          <td>Team</td>
          <td>Conf</td>
          <td>Overall</td>   
        </tr>

        <tr class='odd'>
          <td>Creighton</td>
          <td>5-0</td>
          <td>15-2</td>   
        </tr>

        <tr>
          <td>Villanova</td>
          <td>4-0</td>
          <td>15-1</td>   
        </tr>

        <tr class='odd'>
          <td>Xavier</td>
          <td>4-1</td>
          <td>14-4</td>   
        </tr>

        <tr>
          <td>Georgetown</td>
          <td>3-2</td>
          <td>11-5</td>   
        </tr>

        <tr class='odd'>
          <td>Marquette</td>
          <td>2-2</td>
          <td>10-7</td>   
        </tr>

        <tr>
          <td>DePaul</td>
          <td>2-3</td>
          <td>10-8</td>   
        </tr>

        <tr class='odd'>
          <td>Providence</td>
          <td>1-2</td>
          <td>11-5</td>   
        </tr>

        <tr>
          <td>Seton Hall</td>
          <td>1-3</td>
          <td>10-7</td>   
        </tr>

        <tr class='odd'>
          <td>St. John's</td>
          <td>0-4</td>
          <td>9-7</td>   
        </tr>

        <tr>
          <td>Butler</td>
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
