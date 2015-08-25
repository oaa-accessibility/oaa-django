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
example_info.title       = 'Unidentifiable Data Table'
example_info.permanent_slug = 'dtable6'

example_info.description = """
An example of a data table that does not define its markup.
"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')

example_info.markup = [m1]

rr1 = rule_reference_object("TABLE_5", "fail", "fail", "", "", "")

example_info.rule_references = [rr1]

example_info.html     = """

<table aria-labelledby="id_rankings" >
  <tr><h1 id="id_rankings">NCAA Basketball Rankings by Conference</h1></tr>
  </tr>
  <tr>
    <td>
    <h2 id="id_big10">Big 10</h2>
      <table aria-labelledby="id_big10">
        <tr>
          <td>Team</th>
          <td>Conf</th>
          <td>Overall</th>   
        </tr>
   
        <tr class='odd'>
          <td>Michigan State</th>
          <td>5-0</td>
          <td>16-1</td>
        </tr>

        <tr>
          <td>Michigan</th>
          <td>4-0</td>
          <td>12-4</td>
        </tr>
  
        <tr class='odd'>
          <td>Wisconsin</th>
          <td>3-1</td>
          <td>16-1</td>
        </tr>

        <tr>
          <td>Iowa</th>
          <td>3-1</td>
          <td>14-3</td>
        </tr>

        <tr class='odd'>
          <td>Ohio State</th>
          <td>2-2</td>
          <td>15-2</td>
        </tr>

        <tr>
          <td>Minnesota</th>
          <td>2-2</td>
          <td>13-4</td>
        </tr>

        <tr class='odd'>
          <td>Indiana</th>
          <td>2-2</td>
          <td>12-5</td>
        </tr>

        <tr>
          <td>Purdue</th>
          <td>2-2</td>
          <td>12-5</td>
        </tr>

        <tr class='odd'>
          <td>Illinois</th>
          <td>2-3</td>
          <td>13-5</td>
        </tr>

        <tr>
          <td>Northwestern</th>
          <td>1-4</td>
          <td>8-10</td>
        </tr>
 
        <tr class='odd'>
          <td>Nebraska</th>
          <td>0-4</td>
          <td>8-8</td>
        </tr>

        <tr>
          <td>Penn State</th>
          <td>0-5</td>
          <td>9-9</td>
        </tr>
      </table> 

    </td>
    <td>
    <h2 id="id_big12">Big 12</h2>
      <table aria-labelledby="id_big12">
        <tr>
          <td>Team</th>
          <td>Conf</th>
          <td>Overall</th>   
        </tr>

        <tr class='odd'>
          <td>Kansas</th>
          <td>3-0</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Oklahoma State</th>
          <td>3-1</td>
          <td>15-2</td>   
        </tr>

        <tr class='odd'>
          <td>Kansas State</th>
          <td>3-1</td>
          <td>13-4</td>   
        </tr>

        <tr>
          <td>Iowa State</th>
          <td>2-2</td>
          <td>14-2</td>   
        </tr>

        <tr class='odd'>
          <td>Oklahoma</th>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr>
          <td>Texas</th>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr class='odd'>
          <td>West Virginia</th>
          <td>2-2</td>
          <td>10-7</td>   
        </tr>

        <tr>
          <td>Baylor</th>
          <td>1-2</td>
          <td>1-3</td>   
        </tr>

        <tr class='odd'>
          <td>Texas Tech</th>
          <td>1-3</td>
          <td>9-8</td>   
        </tr>

        <tr>
          <td>TCU</th>
          <td>0-4</td>
          <td>9-7</td>   
        </tr>
      </table>
    </td>
    <td>
    <h2 id="id_sec">SEC</h2>
      <table aria-labelledby="id_sec">
        <tr>
          <td>Team</th>
          <td>Conf</th>
          <td>Overall</th>   
        </tr>

        <tr class='odd'>
          <td>Florida</th>
          <td>3-0</td>
          <td>14-2</td>   
        </tr>

        <tr>
          <td>Texas A&M</th>
          <td>3-0</td>
          <td>12-4</td>   
        </tr>

        <tr class='odd'>
          <td>Kentucky</th>
          <td>2-1</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Ole Miss</th>
          <td>2-1</td>
          <td>11-5</td>   
        </tr>

        <tr class='odd'>
          <td>Tennessee</th>
          <td>2-1</td>
          <td>11-5</td>   
        </tr>

        <tr>
          <td>Georgia</th>
          <td>2-1</td>
          <td>8-7</td>   
        </tr>

        <tr class='odd'>
          <td>Alabama</th>
          <td>2-1</td>
          <td>8-8</td>   
        </tr>

        <tr>
          <td>Missouri</th>
          <td>1-1</td>
          <td>13-2</td>   
        </tr>

        <tr class='odd'>
          <td>Arkansas</th>
          <td>1-2</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Mississippi State</th>
          <td>1-2</td>
          <td>11-5</td>   
        </tr>

        <tr class='odd'>
          <td>LSU</th>
          <td>1-2</td>
          <td>10-5</td>   
        </tr>

        <tr>
          <td>Vanderbilt</th>
          <td>0-2</td>
          <td>8-6</td>   
        </tr>

        <tr class='odd'>
          <td>Auburn</th>
          <td>0-3</td>
          <td>8-6</td>   
        </tr>

        <tr>
          <td>South Carolina</th>
          <td>0-3</td>
          <td>7-9</td>   
        </tr>

      </table>
    </td>
  </tr>
  <tr>
    <td>
    <h2 id="id_pac12">PAC 12</h2>
      <table aria-labelledby="id_pac12">
        <tr>
          <td>Team</th>
          <td>Conf</th>
          <td>Overall</th>   
        </tr>

        <tr class='odd'>
          <td>Arizona</th>
          <td>4-0</td>
          <td>17-0</td>   
        </tr>

        <tr>
          <td>California</th>
          <td>4-0</td>
          <td>13-4</td>   
        </tr>

        <tr class='odd'>
          <td>Colorado</th>
          <td>3-1</td>
          <td>14-3</td>   
        </tr>

        <tr>
          <td>UCLA</th>
          <td>2-1</td>
          <td>13-3</td>   
        </tr>

        <tr class='odd'>
          <td>Washington</th>
          <td>3-2</td>
          <td>11-7</td>   
        </tr>

        <tr>
          <td>Arizona State</th>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr class='odd'>
          <td>Stanford</th>
          <td>2-2</td>
          <td>11-5</td>   
        </tr>

        <tr>
          <td>Oregon</th>
          <td>1-3</td>
          <td>13-3</td>   
        </tr>

        <tr class='odd'>
          <td>Utah</th>
          <td>1-3</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Oregon State</th>
          <td>1-3</td>
          <td>9-7</td>   
        </tr>

        <tr class='odd'>
          <td>Washington State</th>
          <td>1-4</td>
          <td>8-9</td>   
        </tr>

        <tr>
          <td>USC</th>
          <td>0-3</td>
          <td>9-7</td>   
        </tr>
      </table>
    </td>

    <td>
    <h2 id="id_acc">ACC</h2>
      <table aria-labelledby="id_acc">
        <tr>
          <td>Team</th>
          <td>Conf</th>
          <td>Overall</th>   
        </tr>

        <tr class='odd'>
          <td>Syracuse</th>
          <td>4-0</td>
          <td>17-0</td>   
        </tr>

        <tr>
          <td>Pittsburgh</th>
          <td>4-0</td>
          <td>16-1</td>   
        </tr>

        <tr class='odd'>
          <td>Clemson</th>
          <td>3-1</td>
          <td>12-4</td>   
        </tr>

        <tr>
          <td>Florida State</th>
          <td>3-1</td>
          <td>12-4</td>   
        </tr>

        <tr class='odd'>
          <td>Virginia</th>
          <td>3-1</td>
          <td>12-5</td>   
        </tr>

        <tr>
          <td>Maryland</th>
          <td>3-2</td>
          <td>11-7</td>   
        </tr>

        <tr class='odd'>
          <td>Duke</th>
          <td>2-2</td>
          <td>13-4</td>   
        </tr>

        <tr>
          <td>Wake Forest</th>
          <td>2-2</td>
          <td>12-5</td>   
        </tr>

        <tr class='odd'>
          <td>NC State</th>
          <td>1-3</td>
          <td>11-6</td>   
        </tr>

        <tr>
          <td>Georgia Tech</th>
          <td>1-3</td>
          <td>10-7</td>   
        </tr>

        <tr class='odd'>
          <td>Notre Dame</th>
          <td>1-3</td>
          <td>10-7</td>   
        </tr>

        <tr>
          <td>Miami (FL)</th>
          <td>1-3</td>
          <td>9-7</td>   
        </tr>

        <tr class='odd'>
          <td>Virginia Tech</th>
          <td>1-3</td>
          <td>8-8</td>   
        </tr>

        <tr>
          <td>Boston College</th>
          <td>1-3</td>
          <td>5-12</td>   
        </tr>

        <tr class='odd'>
          <td>North Carolina</th>
          <td>0-3</td>
          <td>10-6</td>   
        </tr>
      </table>
    </td>
    <td>
    <h2 id="id_bigeast">Big East</h2>
      <table aria-labelledby="id_bigeast">
        <tr>
          <td>Team</th>
          <td>Conf</th>
          <td>Overall</th>   
        </tr>

        <tr class='odd'>
          <td>Creighton</th>
          <td>5-0</td>
          <td>15-2</td>   
        </tr>

        <tr>
          <td>Villanova</th>
          <td>4-0</td>
          <td>15-1</td>   
        </tr>

        <tr class='odd'>
          <td>Xavier</th>
          <td>4-1</td>
          <td>14-4</td>   
        </tr>

        <tr>
          <td>Georgetown</th>
          <td>3-2</td>
          <td>11-5</td>   
        </tr>

        <tr class='odd'>
          <td>Marquette</th>
          <td>2-2</td>
          <td>10-7</td>   
        </tr>

        <tr>
          <td>DePaul</th>
          <td>2-3</td>
          <td>10-8</td>   
        </tr>

        <tr class='odd'>
          <td>Providence</th>
          <td>1-2</td>
          <td>11-5</td>   
        </tr>

        <tr>
          <td>Seton Hall</th>
          <td>1-3</td>
          <td>10-7</td>   
        </tr>

        <tr class='odd'>
          <td>St. John's</th>
          <td>0-4</td>
          <td>9-7</td>   
        </tr>

        <tr>
          <td>Butler</th>
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

#example_html table table td, table table td{
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

ExampleGroup.objects.get(slug='dtables').examples.add(example1)
