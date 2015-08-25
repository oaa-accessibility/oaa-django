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
example_info.title       = 'Data Table 3'
example_info.permanent_slug = 'dtable3'

example_info.description = """
Example of a data table with links.
"""

example_info.keyboard = """
No keyboard controls.
"""
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

example_info.aria_labelledby = True
example_info.aria_styling = True

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='presentation')

example_info.markup = [m1]

rr1 = rule_reference_object("TABLE_1", "pass", "pass", "TABLE_1_T1", "", "")
rr2 = rule_reference_object("TABLE_4", "pass", "pass", "TABLE_4_T2", "", "")
rr3 = rule_reference_object("TABLE_5", "pass", "pass", "TABLE_5_T1", "", "")
rr4 = rule_reference_object("TABLE_6", "pass", "pass", "TABLE_6_T2", "", "")
rr5 = rule_reference_object("TABLE_3", "pass", "pass", "TABLE_3_T1", "", "")
rr6 = rule_reference_object("TABLE_2", "pass", "pass", "TABLE_2_T1", "", "")

example_info.rule_references = [rr1,rr2,rr3,rr4,rr5,rr6]
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
      <h3>Midwestern University Union</h3>
      <h4>Location and Contact Info</h4>
        <p>Main Level, 123 Complex
        <p>456 Main Street, Cornland, Illinois 60123
        <p>Phone: 217-123-4567
        <p>Fax: 217-987-6543
        <p>Email: union@midwestern.edu
      <h4>Business Hours</h4>
        <p>Monday-Friday 8am - 5pm
        </p>
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
}

"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='dtables').examples.add(example1)
