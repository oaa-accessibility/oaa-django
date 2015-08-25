"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

import sys,os
sys.path.append(os.path.abspath('..'))

from django.core.management import setup_environ 
import coding.settings as settings
setup_environ(settings)

from django.core.exceptions import ObjectDoesNotExist
from markup.models import LanguageSpec, ElementDefinition
from pop_examples_common import *


# =============================
# Example 1
# =============================


example_info1             = example_object()
example_info1.title       = 'heading - Complex table with properly nested heading elements'
example_info1.permanent_slug = ''

example_info1.description = """
* All heading elements (@h1@, @h2@, @h3@, and @h4@) must contain content.
* The words in the one and only @h1@ element are also in the @title@ element.
* The @h2@, @h3@, and @h4@ elements are properly nested.
* Contents of heading elements of the same level are unique.
* Contents of heading elements are concise, i.e. less than 65 characters. 
"""
example_info1.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='h1')
m2 = ElementDefinition.objects.get(spec=spec_html4, element='h2')
m3 = ElementDefinition.objects.get(spec=spec_html4, element='h3')
m4 = ElementDefinition.objects.get(spec=spec_html4, element='h4')

example_info1.markup = [m1,m2,m3,m4]

rr1 = rule_reference_object("HEADING_1", "pass", "na", "HEADING_1_T3", "", "")
rr2 = rule_reference_object("HEADING_3", "pass", "na", "HEADING_3_T1", "", "")
rr3 = rule_reference_object("HEADING_4", "na", "pass", "HEADING_4_T2", "HEADING_4_T3", "")
rr4 = rule_reference_object("HEADING_5", "na", "pass", "HEADING_5_T1", "", "")

example_info1.rule_references = [rr1, rr2, rr3, rr4]

example_info1.html        = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>iCITA: Web Survey with Form Controls Labelled by Hidden LABEL</title>
</head>

<body>
<HL1><h1>Web Survey with Form Controls Labelled by Hidden LABEL</h1></HL1>
  <HL1><h2><a name="description"></a>Accessibility Features of Example</h2></HL1>
  <ul>
    <li>The <code>label</code> element content provides effective labels to form controls of following types: <code>input</code> element of <code>type="radio"</code> and <code>type="checkbox"</code>, and <code>select</code> element.</li>
    <li>Since the form controls of this survey form are densely packed, the <code>label</code> element contents are hidden entirely or partially from the visual rendering using CSS technique of absolute positioning (i.e. use <code>position: absolute; top: -20em; left: -200em</code>).</li>
  </ul>

  <HL1><h2><a name="example"></a>Example</h2></HL1>
  <form method="post" action="form-example-survey-label.php">
  <div tabindex="0">
    <HL1><h3>Survey Instructions</h3></HL1>
    <p>Please rate the following statements (1 is lowest, 9 is highest) by indicating Minimum -- the number that represents the minimum level of service that you would find acceptable.</p>
  </div>
  <div tabindex="0">
    <HL1><h3>Survey Questions</h3></HL1>
  </div>
  <table class="survey" cellpadding="0" cellspacing="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s1" colspan="2">When it comes to..</th>
        <th class="column">&nbsp;</th>
        <th id="min_s1" colspan="9" class="column">My Minimum<br>Service Level Is</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           1)
        </td>
        <td class="question" align="left" valign="middle">
          <HL1><h4>Employees who instill confidence in users</h4></HL1>
        </td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="low rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           2)
        </td>
        <td class="question" align="left" valign="middle">
          <div tabindex="0">
            <HL1><h4>Making electronic resources accessible from my home</h4></HL1>
          </div>
        </td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="low rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
      </tr>
    </tbody>
  </table>

</body>
</html> 
"""

example_info1.script       = """"""

example_info1.style       = """"""

example1 = create_example(example_info1)
