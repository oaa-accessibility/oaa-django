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
example_info.title       = 'Unidentifiable Layout Table'
example_info.permanent_slug = 'ltable6'

example_info.description = """
Example of an unidentifiable layout table.
"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

example_info.aria_labelledby = True
example_info.aria_styling = True

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')

example_info.markup = [m1]


rr1 = rule_reference_object("TABLE_5", "fail", "fail", "", "", "")

example_info.rule_references = [rr1]

example_info.html     = """
 <table>
 <tr>
    <td colspan="2">
      <h1 align="center">Midwestern University</h1>
    </td>
 </tr>

  <tr>
    <td>
      <h2>Navigation Menu</h2>
      <ul>
        <li><a href="">LINK 1</a>
        <li><a href="">LINK 2</a>
      </ul>
    </td>

    <td>
      <h3>Midwestern University Union</h3>
      <h3>Location and Contact Info</h3>
        <p>Main Level, 123 Complex
        <p>456 Main Street, Cornland, Illinois 60123
        <p>Phone: 217-123-4567
        <p>Fax: 217-987-6543
        <p>Email: union@midwestern.edu
      <h3>Business Hours</h3>
        <p>Monday-Friday 8am - 5pm
        </p>
    </td>   
  </tr>

  <tr>
    <td colspan="2">
      <p><h4>2014 Midwestern University Union <br>456 Main Street Cornland, Illinois 60123</h6>
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

#example_html table caption {
  padding: .25em;
  border-top: 1px solid #808080;
  border-left: 1px solid #808080;
  border-right: 1px solid #808080;
  background-color: #FFFFFF;
}


#example_html table td, table.complex th {
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
