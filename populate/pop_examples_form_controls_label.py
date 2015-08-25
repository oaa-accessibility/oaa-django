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

order = 1

eg_label = ExampleGroup.objects.get(slug="labeling")
eg_focus    = ExampleGroup.objects.get(slug="focus")

example_info             = example_object()
example_info.order       = order
example_info.example_groups = [eg_label, eg_focus]
example_info.title       = 'Complex Survey - No @label@ elements'
example_info.permanent_slug = 'label1'

example_info.description = """
* Form controls without labels are inaccessible!
* Information about the format of the date is after the form control and not easily discoverable by people using speech.
* Headers are used to mark sections of the survey
"""
example_info.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='label')

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "fail", "na", "", "", "")

example_info.rule_references = [rr1]

example_info.html        = """
<form method="post" action="form-example-survey-label.php">

  <!--
      Using hidden LABELs to provide effective labels for form controls densely packed in layout tables.
   -->

  <h3>Survey Instructions</h3>

  <p>Please rate the following statements (1 is lowest, 9 is highest) by indicating:</p>

  <ul class="survey">
     <li><div>Minimum --</div> the number that represents the minimum level of service that you would find acceptable</li>
     <li><div>Desired --</div> the number that represents the level of service that you personally want</li>
     <li><div>Perceived --</div> the number that represents the level of service that you believe our library currently provides</li>
  </ul>

  <p>For each item, you must EITHER rate the item in all three columns OR identify the item as "N/A" (not applicable). Selecting "N/A" will override all other answers for that item.</p>

  <h3>Survey Questions</h3>

  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s1" colspan="2">When it comes to..</th>
        <th class="column">&nbsp;</th>
        <th id="min_s1" colspan="9" class="column">My Minimum<br/>Service Level Is</th>
        <th id="des_s1" colspan="9" class="column">My Desired<br/>Service Level Is</th>
        <th id="per_s1" colspan="9" class="column">Perceived Service<br/>Performance Is</th>
      </tr>
      <tr>
        <th colspan="2">&nbsp;</th>
        <th id="na_s1" class="na"><abbr title="Not Applicable">N/A</abbr></th>
        <th class="low"  colspan="4">Low</th>
        <th class="high" colspan="5">High</th>
        <th class="low"  colspan="4">Low</th>
        <th class="high" colspan="5">High</th>
        <th class="low"  colspan="4">Low</th>
        <th class="high" colspan="5">High</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           1)
        </td>
        <td class="question" align="left" valign="middle">
            Employees who instill confidence in users
        </td>
        <td class="low" align="center" valign="middle">
           <input class="low" type="checkbox" name="s1_q1_na" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" />
        </td>
        <td class="" align="center" valign="middle">Bryant made it clear from the first day of training camp this past season that the Lakers were his team, and he saw it as his responsibility to prepare Howard for that responsibility one day. Howard stated that he was anxious to learn from Bryant, Nash and Gasol. Both Howard and Bryant were amenable to that arrangement early, but as the season wore on, it became clear to Howard that there wouldn't be a clean transfer of power, sources said.
           <input type="radio" name="s1_q1_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" />
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>Bryant made it clear from the first day of training camp this past season that the Lakers were his team, and he saw it as his responsibility to prepare Howard for that responsibility one day. Howard stated that he was anxious to learn from Bryant, Nash and Gasol. Both Howard and Bryant were amenable to that arrangement early, but as the season wore on, it became clear to Howard that there wouldn't be a clean transfer of power, sources said.
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
        <td class="low rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>Bryant made it clear from the first day of training camp this past season that the Lakers were his team, and he saw it as his responsibility to prepare Howard for that responsibility one day. Howard stated that he was anxious to learn from Bryant, Nash and Gasol. Both Howard and Bryant were amenable to that arrangement early, but as the season wore on, it became clear to Howard that there wouldn't be a clean transfer of power, sources said.
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="low rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>Bryant made it clear from the first day of training camp this past season that the Lakers were his team, and he saw it as his responsibility to prepare Howard for that responsibility one day. Howard stated that he was anxious to learn from Bryant, Nash and Gasol. Both Howard and Bryant were amenable to that arrangement early, but as the season wore on, it became clear to Howard that there wouldn't be a clean transfer of power, sources said.
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
            Making electronic resources accessible from my home or office
        </td>
        <td class="low" align="center" valign="middle">Bryant made it clear from the first day of training camp this past season that the Lakers were his team, and he saw it as his responsibility to prepare Howard for that responsibility one day. Howard stated that he was anxious to learn from Bryant, Nash and Gasol. Both Howard and Bryant were amenable to that arrangement early, but as the season wore on, it became clear to Howard that there wouldn't be a clean transfer of power, sources said.
           <input class="low" type="checkbox" name="s1_q2_na" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" />Bryant made it clear from the first day of training camp this past season that the Lakers were his team, and he saw it as his responsibility to prepare Howard for that responsibility one day. Howard stated that he was anxious to learn from Bryant, Nash and Gasol. Both Howard and Bryant were amenable to that arrangement early, but as the season wore on, it became clear to Howard that there wouldn't be a clean transfer of power, sources said.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" />
        </td>
        <td class="" align="center" valign="middle">Bryant made it clear from the first day of training camp this past season that the Lakers were his team, and he saw it as his responsibility to prepare Howard for that responsibility one day. Howard stated that he was anxious to learn from Bryant, Nash and Gasol. Both Howard and Bryant were amenable to that arrangement early, but as the season wore on, it became clear to Howard that there wouldn't be a clean transfer of power, sources said.
           <input type="radio" name="s1_q2_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" />
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
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
        <td class="low rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
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
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           3)
        </td>
        <td class="question" align="left" valign="middle">
            Library space that inspires study and learning
        </td>
        <td class="low" align="center" valign="middle">
           <input class="low" type="checkbox" name="s1_q3_na" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" />
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
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
        <td class="low rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
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
           4)
        </td>
        <td class="question" align="left" valign="middle">
            Giving users individual attention
        </td>
        <td class="low" align="center" valign="middle">
           <input class="low" type="checkbox" name="s1_q4_na" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" />
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
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
        <td class="low rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
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
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           5)
        </td>
        <td class="question" align="left" valign="middle">
            A library Web site enabling me to locate information on my own
        </td>
        <td class="low" align="center" valign="middle">
           <input class="low" type="checkbox" name="s1_q5_na" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" />
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
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
        <td class="low rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
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
  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s2" colspan="2">Please indicate your library usage patterns:</th>
        <th id="min_s2" colspan="9" class="column">&nbsp;</th>
      </tr>
    </thead>
    <tbody>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           6)
        </td>
        <td class="question" align="left" valign="middle">
            The library helps me stay abreast of developments in my field(s) of interest.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" />
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
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
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           7)
        </td>
        <td class="question" align="left" valign="middle">
            The library aids my advancement in my academic discipline or work.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" />
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
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
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           8)
        </td>
        <td class="question" align="left" valign="middle">
            The library enables me to be more efficient in my academic pursuits or work.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" />
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
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
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           9)
        </td>
        <td class="question" align="left" valign="middle">
            The library helps me distinguish between trustworthy and untrustworthy information.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" />
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
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
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           10)
        </td>
        <td class="question" align="left" valign="middle">
            The library provides me with the information skills I need in my work or study.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" />
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
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
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
    </tbody>
  </table>
  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s3" colspan="2">Please answer a few questions about yourself:</th>
        <th id="min_s3" colspan="9" class="column">&nbsp;</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           11)
        </td>
        <td class="question" align="left" valign="middle">
             The library that you use the most often:
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q11_select" id="s3_q11_select">
             <option value="1++">Downtown Branch</option>
             <option value="1++">Southwest Branch</option>
             <option value="1++">Northeast Branch</option>
             <option value="1++">Bookmobile</option>
           </select>
        </td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           12)
        </td>
        <td class="question" align="left" valign="middle">
            Age:
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q12_select" id="s3_q12_select">
             <option value="1++">Under 18</option>
             <option value="1++">18-22</option>
             <option value="1++">23- 30</option>
             <option value="1++">31-45</option>
             <option value="1++">over 45</option>
           </select>
        </td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           13)
        </td>
        <td class="question" align="left" valign="middle">
            Sex:
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q13_select" id="s3_q13_select">
             <option value="1++">Male</option>
             <option value="1++">Female</option>
           </select>
        </td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           14)
        </td>
        <td class="question" align="left" valign="middle">
            Discipline:
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q14_select" id="s3_q14_select">
             <option value="1++">Agriculture / Environmental Studies</option>
             <option value="1++">Business</option>
             <option value="1++">Communications / Journalism</option>
             <option value="1++">Education</option>
             <option value="1++">Engineering / Computer Science</option>
             <option value="1++">General Studies</option>
             <option value="1++">Health Sciences</option>
             <option value="1++">Humanities</option>
             <option value="1++">Law</option>
             <option value="1++">Military / Naval Science</option>
             <option value="1++">Other</option>
             <option value="1++">Performing &amp; Fine Arts</option>
             <option value="1++">Science / Math</option>
             <option value="1++">Psychology/Sociology</option>
             <option value="1++">Undecided</option>
             <option value="1++">Miscellaneous</option>
             <option value="1++">Architecture</option>
           </select>
        </td>
      </tr>
    </tbody>
  </table>
  <p class="submit"><input type="submit" value="Submit Survey Responses"/></p>
</form> 
"""

example_info.script      = """"""

example_info.style       = """
   <style type="text/css">
/* CSS Document */


table.survey {
  margin-bottom: 2em;
}

table.survey th {
  padding: .5em;
  text-align: center;
}

table.survey th.prefix {
  border-bottom: solid white 2px;
}

table.survey th.column {
  border-left: solid white 2px;
  border-bottom: solid white 2px;
}

table.survey th.low,
table.survey td.low,
table.survey th.na {
  border-left: solid white 2px;
}

table.survey th.low,
table.survey th.high,
table.survey th.na {
  font-weight: normal;
  font-size: 90%;
}  

table.survey th.low {
  font-size: 90%;
}

table.survey th.high {
  text-align: right;
}

table.survey thead {
  background-color:#CCCCFF;
}

table.survey tr.odd td {
  background-color: #EEEEEE;
}

table.survey tr.even {
  background-color: #FFFFCC;
}

table.survey tr.top td {
  border-top: solid white 2px;
  padding-top: .125em;
}

table.survey td,
table.survey td {
  padding: 0;
  margin: 0;
}

table.survey td input,
table.survey td input {
  padding: 0;
  margin: 0;
}


table.survey td.rating {
  padding: 0;
  margin: 0;
  font-size: 70%;
  color: #606060;
}

table.survey td.question {
  font-size: 100%;
  font-weight: normal;
  padding-right: 1.25em;
}

table.survey td.number {
  font-size: 100%;
  font-weight: bold;
  width: 2em;
  padding-left: .125em;
}

table.survey td.select {
  width: 30em;
}

table.survey td.select select{
  margin: .5em;
}

ul.survey li {
  list-style: none;
}

ul.survey li div {
  width: 10em;
  padding-right: .5em;
  text-align: right;
  font-weight: bold;
  float: left;
}

table.survey h3 {
  margin: 0;
  padding: 0;
  font-size: 100%;
  font-weight: normal;
}

  </style>
"""

example1 = create_example(example_info)
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
ExampleScriptReference.objects.filter(example=example1).delete()
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='labeling').examples.add(example1)
# =============================
# Example 2
# =============================
order += 1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_label]
example_info.title       = 'Complex Survey - Non-unique @label@ elements'
example_info.permanent_slug = 'label2'

example_info.description = """
* Form controls do have @label@ markup.
* The problem with this @form@ is the @label@ markup is not unique.
* Headers are used to mark sections of the survey
"""

example_info.keyboard    = """
"""

rr1 = rule_reference_object("CONTROL_1", "fail", "na", "", "", "")
rr2 = rule_reference_object("CONTROL_12", "fail", "na", "", "", "")

example_info.rule_references = [rr1, rr2]

example_info.markup = [m1]

example_info.html        = """
<form method="post" action="form-example-survey-label.php">

  <!--
      Using hidden LABELs to provide effective labels for form controls densely packed in layout tables.
   -->

  <h3>Survey Instructions</h3>

  <p>Please rate the following statements (1 is lowest, 9 is highest) by indicating:</p>

  <ul class="survey">
     <li><div>Minimum --</div> the number that represents the minimum level of service that you would find acceptable</li>
     <li><div>Desired --</div> the number that represents the level of service that you personally want</li>
     <li><div>Perceived --</div> the number that represents the level of service that you believe our library currently provides</li>
  </ul>

  <p>For each item, you must EITHER rate the item in all three columns OR identify the item as "N/A" (not applicable). Selecting "N/A" will override all other answers for that item.</p>

  <h3>Survey Questions</h3>

  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s1" colspan="2">When it comes to..</th>
        <th class="column">&nbsp;</th>
        <th id="min_s1" colspan="9" class="column">My Minimum<br/>Service Level Is</th>
        <th id="des_s1" colspan="9" class="column">My Desired<br/>Service Level Is</th>
        <th id="per_s1" colspan="9" class="column">Perceived Service<br/>Performance Is</th>
      </tr>
      <tr>
        <th colspan="2">&nbsp;</th>
        <th id="na_s1" class="na"><abbr title="Not Applicable">N/A</abbr></th>
        <th class="low"  colspan="4">Low</th>
        <th class="high" colspan="5">High</th>
        <th class="low"  colspan="4">Low</th>
        <th class="high" colspan="5">High</th>
        <th class="low"  colspan="4">Low</th>
        <th class="high" colspan="5">High</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           1)
        </td>
        <td class="question" align="left" valign="middle">
            Employees who instill confidence in users
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="hidden" for="s1_q1_na">Not applicable</label>
           <input class="low" type="checkbox" name="s1_q1_na" id="s1_q1_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_9"/>
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_min_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_des_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_des_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_des_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_des_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_des_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_des_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_des_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_des_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_des_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_per_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_per_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_per_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_per_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_per_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_per_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_per_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_per_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q1_per_9">9</label></td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           2)
        </td>
        <td class="question" align="left" valign="middle">
            Making electronic resources accessible from my home or office
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="hidden" for="s1_q2_na">Not applicable</label>
           <input class="low" type="checkbox" name="s1_q2_na" id="s1_q2_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_9"/>
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_min_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_des_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_des_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_des_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_des_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_des_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_des_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_des_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_des_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_des_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_per_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_per_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_per_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_per_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_per_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_per_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_per_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_per_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q2_per_9">9</label></td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           3)
        </td>
        <td class="question" align="left" valign="middle">
            Library space that inspires study and learning
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="hidden" for="s1_q3_na">Not applicable</label>
           <input class="low" type="checkbox" name="s1_q3_na" id="s1_q3_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_9"/>
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_min_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_des_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_des_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_des_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_des_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_des_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_des_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_des_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_des_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_des_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_per_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_per_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_per_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_per_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_per_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_per_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_per_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_per_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q3_per_9">9</label></td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           4)
        </td>
        <td class="question" align="left" valign="middle">
            Giving users individual attention
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="hidden" for="s1_q4_na">Not applicable</label>
           <input class="low" type="checkbox" name="s1_q4_na" id="s1_q4_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_9"/>
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_min_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_des_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_des_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_des_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_des_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_des_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_des_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_des_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_des_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_des_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_per_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_per_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_per_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_per_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_per_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_per_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_per_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_per_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q4_per_9">9</label></td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           5)
        </td>
        <td class="question" align="left" valign="middle">
            A library Web site enabling me to locate information on my own
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="hidden" for="s1_q5_na">Not applicable</label>
           <input class="low" type="checkbox" name="s1_q5_na" id="s1_q5_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_9"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_1"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_2"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_3"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_4"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_5"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_6"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_7"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_8"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_9"/>
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_min_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_des_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_des_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_des_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_des_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_des_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_des_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_des_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_des_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_des_9">9</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_per_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_per_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_per_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_per_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_per_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_per_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_per_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_per_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s1_q5_per_9">9</label></td>
      </tr>
    </tbody>
  </table>
  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s2" colspan="2">Please indicate your library usage patterns:</th>
        <th id="min_s2" colspan="9" class="column">&nbsp;</th>
      </tr>
    </thead>
    <tbody>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           6)
        </td>
        <td class="question" align="left" valign="middle">
            The library helps me stay abreast of developments in my field(s) of interest.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_1" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_2" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_3" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_4" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_5" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_6" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_7" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_8" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_9" />
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle"><label for="s2_q6_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q6_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q6_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q6_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q6_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q6_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q6_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q6_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q6_min_9">9</label></td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           7)
        </td>
        <td class="question" align="left" valign="middle">
            The library aids my advancement in my academic discipline or work.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_1" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_2" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_3" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_4" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_5" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_6" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_7" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_8" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_9" />
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle"><label for="s2_q7_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q7_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q7_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q7_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q7_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q7_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q7_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q7_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q7_min_9">9</label></td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           8)
        </td>
        <td class="question" align="left" valign="middle">
            The library enables me to be more efficient in my academic pursuits or work.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_1" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_2" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_3" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_4" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_5" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_6" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_7" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_8" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_9" />
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle"><label for="s2_q8_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q8_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q8_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q8_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q8_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q8_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q8_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q8_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q8_min_9">9</label></td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           9)
        </td>
        <td class="question" align="left" valign="middle">
            The library helps me distinguish between trustworthy and untrustworthy information.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_1" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_2" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_3" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_4" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_5" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_6" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_7" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_8" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_9" />
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle"><label for="s2_q9_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q9_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q9_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q9_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q9_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q9_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q9_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q9_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q9_min_9">9</label></td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           10)
        </td>
        <td class="question" align="left" valign="middle">
            The library provides me with the information skills I need in my work or study.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_1" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_2" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_3" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_4" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_5" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_6" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_7" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_8" />
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_9" />
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle"><label for="s2_q10_min_1">1</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q10_min_2">2</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q10_min_3">3</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q10_min_4">4</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q10_min_5">5</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q10_min_6">6</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q10_min_7">7</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q10_min_8">8</label></td>
        <td class="rating" align="center" valign="middle"><label for="s2_q10_min_9">9</label></td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
    </tbody>
  </table>
  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s3" colspan="2">Please answer a few questions about yourself:</th>
        <th id="min_s3" colspan="9" class="column">&nbsp;</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           11)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q11_select"> The library that you use the most often:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q11_select" id="s3_q11_select">
             <option value="1++">Downtown Branch</option>
             <option value="1++">Southwest Branch</option>
             <option value="1++">Northeast Branch</option>
             <option value="1++">Bookmobile</option>
           </select>
        </td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           12)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q12_select">Age:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q12_select" id="s3_q12_select">
             <option value="1++">Under 18</option>
             <option value="1++">18-22</option>
             <option value="1++">23- 30</option>
             <option value="1++">31-45</option>
             <option value="1++">over 45</option>
           </select>
        </td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           13)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q13_select">Sex:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q13_select" id="s3_q13_select">
             <option value="1++">Male</option>
             <option value="1++">Female</option>
           </select>
        </td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           14)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q14_select">Discipline:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q14_select" id="s3_q14_select">
             <option value="1++">Agriculture / Environmental Studies</option>
             <option value="1++">Business</option>
             <option value="1++">Communications / Journalism</option>
             <option value="1++">Education</option>
             <option value="1++">Engineering / Computer Science</option>
             <option value="1++">General Studies</option>
             <option value="1++">Health Sciences</option>
             <option value="1++">Humanities</option>
             <option value="1++">Law</option>
             <option value="1++">Military / Naval Science</option>
             <option value="1++">Other</option>
             <option value="1++">Performing &amp; Fine Arts</option>
             <option value="1++">Science / Math</option>
             <option value="1++">Psychology/Sociology</option>
             <option value="1++">Undecided</option>
             <option value="1++">Miscellaneous</option>
             <option value="1++">Architecture</option>
           </select>
        </td>
      </tr>
    </tbody>
  </table>
  <p class="submit"><input type="submit" value="Submit Survey Responses"/></p>
</form> 
"""

example_info.script      = """"""

example_info.style       = """
  <style type="text/css">
/* CSS Document */

.hidden {
  position: absolute;
  left: -200em;
  top: -20em;
}

table.survey {
  margin-bottom: 2em;
}

table.survey th {
  padding: .5em;
  text-align: center;
}

table.survey th.prefix {
  border-bottom: solid white 2px;
}

table.survey th.column {
  border-left: solid white 2px;
  border-bottom: solid white 2px;
}

table.survey th.low,
table.survey td.low,
table.survey th.na {
  border-left: solid white 2px;
}

table.survey th.low,
table.survey th.high,
table.survey th.na {
  font-weight: normal;
  font-size: 90%;
}  

table.survey th.low {
  font-size: 90%;
}

table.survey th.high {
  text-align: right;
}

table.survey thead {
  background-color:#CCCCFF;
}

table.survey tr.odd td {
  background-color: #EEEEEE;
}

table.survey tr.even {
  background-color: #FFFFCC;
}

table.survey tr.top td {
  border-top: solid white 2px;
  padding-top: .125em;
}

table.survey td,
table.survey td {
  padding: 0;
  margin: 0;
}

table.survey td input,
table.survey td input {script      = """"""
  padding: 0;
  margin: 0;
}


table.survey td.rating {
  padding: 0;
  margin: 0;
  font-size: 70%;
  color: #606060;
}

table.survey td.question {
  font-size: 100%;
  font-weight: normal;
  padding-right: 1.25em;
}

table.survey td.number {
  font-size: 100%;
  font-weight: bold;
  width: 2em;
  padding-left: .125em;
}

table.survey td.select {
  width: 30em;
}

table.survey td.select select{
  margin: .5em;
}

ul.survey li {
  list-style: none;
}

ul.survey li div {
  width: 10em;
  padding-right: .5em;
  text-align: right;
  font-weight: bold;
  float: left;
}


#content table.survey h3 {
  margin: 0;
  padding: 0;
  font-size: 100%;
  font-weight: normal;
}

  </style>
"""

example2 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
add_script_reference( example2, script1 )

ExampleGroup.objects.get(slug='labeling').examples.add(example2)
# =============================
# Example 3
# =============================

order += 1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_label]
example_info.title       = 'Complex Survey - @Input[type=radio] elements positioned off screen @label@ elements'
example_info.permanent_slug = 'label3'

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "", "", "")
rr2 = rule_reference_object("CONTROL_12", "pass", "na", "", "", "")

example_info.rule_references = [rr1,rr2]

example_info.description = """
* Form controls do have unique @label@ markup.
* It is considered a poor practice because the labels are long and have alot of redudant information that is difficult to listen to with speech.
* It is also a poor practice from a coding perspective since there is lot of redudant text on the page making the page much larger than necessary.
* The labels for the most complex radio buttons include: 
*# The rating number is first, since it is the most unique information, and is the first piece of information read.
*# Total number of operations is second
*# The column question is third
*# The question number and question text are fourth
* Headers are used to mark sections of the survey.
"""
example_info.keyboard    = """
"""
example_info.markup = [m1]

example_info.html        = """
<form method="post" action="form-example-survey-label.php">

  <!--
      Using hidden LABELs to provide effective labels for form controls densely packed in layout tables.
   -->

  <h3>Survey Instructions</h3>

  <p>Please rate the following statements (1 is lowest, 9 is highest) by indicating:</p>

  <ul class="survey">
     <li><div>Minimum --</div> the number that represents the minimum level of service that you would find acceptable</li>
     <li><div>Desired --</div> the number that represents the level of service that you personally want</li>
     <li><div>Perceived --</div> the number that represents the level of service that you believe our library currently provides</li>
  </ul>

  <p>For each item, you must EITHER rate the item in all three columns OR identify the item as "N/A" (not applicable). Selecting "N/A" will override all other answers for that item.</p>

  <h3>Survey Questions</h3>

  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s1" colspan="2">When it comes to..</th>
        <th class="column">&nbsp;</th>
        <th id="min_s1" colspan="9" class="column">My Minimum<br/>Service Level Is</th>
        <th id="des_s1" colspan="9" class="column">My Desired<br/>Service Level Is</th>
        <th id="per_s1" colspan="9" class="column">Perceived Service<br/>Performance Is</th>
      </tr>
      <tr>
        <th colspan="2">&nbsp;</th>
        <th id="na_s1" class="na"><abbr title="Not Applicable">N/A</abbr></th>
        <th class="low"  colspan="4">Low</th>
        <th class="high" colspan="5">High</th>
        <th class="low"  colspan="4">Low</th>
        <th class="high" colspan="5">High</th>
        <th class="low"  colspan="4">Low</th>
        <th class="high" colspan="5">High</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           1)
        </td>
        <td class="question" align="left" valign="middle">
            Employees who instill confidence in users
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q1_na">Question 1, Employees who instill confidence in users, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q1_na" id="s1_q1_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_1"/>
           <label class="offscreen" for="s1_q1_min_1">1 of 9, lowest rating, rating of my minimum service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_2"/>
           <label class="offscreen" for="s1_q1_min_2">2 of 9, rating of my minimum service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_3"/>
           <label class="offscreen" for="s1_q1_min_3">3 of 9, rating of my minimum service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_4"/>
           <label class="offscreen" for="s1_q1_min_4">4 of 9, rating of my minimum service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_5"/>
           <label class="offscreen" for="s1_q1_min_5">5 of 9, rating of my minimum service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_6"/>
           <label class="offscreen" for="s1_q1_min_6">6 of 9, rating of my minimum service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_7"/>
           <label class="offscreen" for="s1_q1_min_7">7 of 9, rating of my minimum service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_8"/>
           <label class="offscreen" for="s1_q1_min_8">8 of 9, rating of my minimum service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_min" id="s1_q1_min_9"/>
           <label class="offscreen" for="s1_q1_min_9">9 of 9, highest rating, rating of my minimum service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_1"/>
           <label class="offscreen" for="s1_q1_des_1">1 of 9, lowest rating, rating of my desired service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_2"/>
           <label class="offscreen" for="s1_q1_des_2">2 of 9, rating of my desired service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_3"/>
           <label class="offscreen" for="s1_q1_des_3">3 of 9, rating of my desired service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_4"/>
           <label class="offscreen" for="s1_q1_des_4">4 of 9, rating of my desired service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_5"/>
           <label class="offscreen" for="s1_q1_des_5">5 of 9, rating of my desired service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_6"/>
           <label class="offscreen" for="s1_q1_des_6">6 of 9, rating of my desired service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_7"/>
           <label class="offscreen" for="s1_q1_des_7">7 of 9, rating of my desired service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_8"/>
           <label class="offscreen" for="s1_q1_des_8">8 of 9, rating of my desired service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_des" id="s1_q1_des_9"/>
           <label class="offscreen" for="s1_q1_des_9">9 of 9, highest rating, rating of my desired service level for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_1"/>
           <label class="offscreen" for="s1_q1_per_1">1 of 9, lowest rating, rating of my perceived service performance  for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_2"/>
           <label class="offscreen" for="s1_q1_per_2">2 of 9, rating of my perceived service performance  for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_3"/>
           <label class="offscreen" for="s1_q1_per_3">3 of 9, rating of my perceived service performance  for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_4"/>
           <label class="offscreen" for="s1_q1_per_4">4 of 9, rating of my perceived service performance  for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_5"/>
           <label class="offscreen" for="s1_q1_per_5">5 of 9, rating of my perceived service performance  for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_6"/>
           <label class="offscreen" for="s1_q1_per_6">6 of 9, rating of my perceived service performance  for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_7"/>
           <label class="offscreen" for="s1_q1_per_7">7 of 9, rating of my perceived service performance  for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_8"/>
           <label class="offscreen" for="s1_q1_per_8">8 of 9, rating of my perceived service performance  for question 1 Employees who instill confidence in users</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q1_per" id="s1_q1_per_9"/>
           <label class="offscreen" for="s1_q1_per_9">9 of 9, highest rating, rating of my perceived service performance  for question 1 Employees who instill confidence in users</label>
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
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
            Making electronic resources accessible from my home or office
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q2_na">Question 2, Making electronic resources accessible from my home or office, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q2_na" id="s1_q2_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_1"/>
           <label class="offscreen" for="s1_q2_min_1">1 of 9, lowest rating, rating of my minimum service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_2"/>
           <label class="offscreen" for="s1_q2_min_2">2 of 9, rating of my minimum service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_3"/>
           <label class="offscreen" for="s1_q2_min_3">3 of 9, rating of my minimum service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_4"/>
           <label class="offscreen" for="s1_q2_min_4">4 of 9, rating of my minimum service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_5"/>
           <label class="offscreen" for="s1_q2_min_5">5 of 9, rating of my minimum service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_6"/>
           <label class="offscreen" for="s1_q2_min_6">6 of 9, rating of my minimum service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_7"/>
           <label class="offscreen" for="s1_q2_min_7">7 of 9, rating of my minimum service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_8"/>
           <label class="offscreen" for="s1_q2_min_8">8 of 9, rating of my minimum service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_min" id="s1_q2_min_9"/>
           <label class="offscreen" for="s1_q2_min_9">9 of 9, highest rating, rating of my minimum service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_1"/>
           <label class="offscreen" for="s1_q2_des_1">1 of 9, lowest rating, rating of my desired service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_2"/>
           <label class="offscreen" for="s1_q2_des_2">2 of 9, rating of my desired service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_3"/>
           <label class="offscreen" for="s1_q2_des_3">3 of 9, rating of my desired service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_4"/>
           <label class="offscreen" for="s1_q2_des_4">4 of 9, rating of my desired service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_5"/>
           <label class="offscreen" for="s1_q2_des_5">5 of 9, rating of my desired service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_6"/>
           <label class="offscreen" for="s1_q2_des_6">6 of 9, rating of my desired service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_7"/>
           <label class="offscreen" for="s1_q2_des_7">7 of 9, rating of my desired service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_8"/>
           <label class="offscreen" for="s1_q2_des_8">8 of 9, rating of my desired service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_des" id="s1_q2_des_9"/>
           <label class="offscreen" for="s1_q2_des_9">9 of 9, highest rating, rating of my desired service level for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_1"/>
           <label class="offscreen" for="s1_q2_per_1">1 of 9, lowest rating, rating of my perceived service performance  for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_2"/>
           <label class="offscreen" for="s1_q2_per_2">2 of 9, rating of my perceived service performance  for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_3"/>
           <label class="offscreen" for="s1_q2_per_3">3 of 9, rating of my perceived service performance  for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_4"/>
           <label class="offscreen" for="s1_q2_per_4">4 of 9, rating of my perceived service performance  for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_5"/>
           <label class="offscreen" for="s1_q2_per_5">5 of 9, rating of my perceived service performance  for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_6"/>
           <label class="offscreen" for="s1_q2_per_6">6 of 9, rating of my perceived service performance  for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_7"/>
           <label class="offscreen" for="s1_q2_per_7">7 of 9, rating of my perceived service performance  for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_8"/>
           <label class="offscreen" for="s1_q2_per_8">8 of 9, rating of my perceived service performance  for question 2 Making electronic resources accessible from my home or office</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q2_per" id="s1_q2_per_9"/>
           <label class="offscreen" for="s1_q2_per_9">9 of 9, highest rating, rating of my perceived service performance  for question 2 Making electronic resources accessible from my home or office</label>
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           3)
        </td>
        <td class="question" align="left" valign="middle">
            Library space that inspires study and learning
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q3_na">Question 3, Library space that inspires study and learning, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q3_na" id="s1_q3_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_1"/>
           <label class="offscreen" for="s1_q3_min_1">1 of 9, lowest rating, rating of my minimum service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_2"/>
           <label class="offscreen" for="s1_q3_min_2">2 of 9, rating of my minimum service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_3"/>
           <label class="offscreen" for="s1_q3_min_3">3 of 9, rating of my minimum service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_4"/>
           <label class="offscreen" for="s1_q3_min_4">4 of 9, rating of my minimum service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_5"/>
           <label class="offscreen" for="s1_q3_min_5">5 of 9, rating of my minimum service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_6"/>
           <label class="offscreen" for="s1_q3_min_6">6 of 9, rating of my minimum service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_7"/>
           <label class="offscreen" for="s1_q3_min_7">7 of 9, rating of my minimum service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_8"/>
           <label class="offscreen" for="s1_q3_min_8">8 of 9, rating of my minimum service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_min" id="s1_q3_min_9"/>
           <label class="offscreen" for="s1_q3_min_9">9 of 9, highest rating, rating of my minimum service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_1"/>
           <label class="offscreen" for="s1_q3_des_1">1 of 9, lowest rating, rating of my desired service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_2"/>
           <label class="offscreen" for="s1_q3_des_2">2 of 9, rating of my desired service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_3"/>
           <label class="offscreen" for="s1_q3_des_3">3 of 9, rating of my desired service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_4"/>
           <label class="offscreen" for="s1_q3_des_4">4 of 9, rating of my desired service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_5"/>
           <label class="offscreen" for="s1_q3_des_5">5 of 9, rating of my desired service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_6"/>
           <label class="offscreen" for="s1_q3_des_6">6 of 9, rating of my desired service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_7"/>
           <label class="offscreen" for="s1_q3_des_7">7 of 9, rating of my desired service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_8"/>
           <label class="offscreen" for="s1_q3_des_8">8 of 9, rating of my desired service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_des" id="s1_q3_des_9"/>
           <label class="offscreen" for="s1_q3_des_9">9 of 9, highest rating, rating of my desired service level for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_1"/>
           <label class="offscreen" for="s1_q3_per_1">1 of 9, lowest rating, rating of my perceived service performance  for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_2"/>
           <label class="offscreen" for="s1_q3_per_2">2 of 9, rating of my perceived service performance  for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_3"/>
           <label class="offscreen" for="s1_q3_per_3">3 of 9, rating of my perceived service performance  for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_4"/>
           <label class="offscreen" for="s1_q3_per_4">4 of 9, rating of my perceived service performance  for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_5"/>
           <label class="offscreen" for="s1_q3_per_5">5 of 9, rating of my perceived service performance  for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_6"/>
           <label class="offscreen" for="s1_q3_per_6">6 of 9, rating of my perceived service performance  for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_7"/>
           <label class="offscreen" for="s1_q3_per_7">7 of 9, rating of my perceived service performance  for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_8"/>
           <label class="offscreen" for="s1_q3_per_8">8 of 9, rating of my perceived service performance  for question 3 Library space that inspires study and learning</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q3_per" id="s1_q3_per_9"/>
           <label class="offscreen" for="s1_q3_per_9">9 of 9, highest rating, rating of my perceived service performance  for question 3 Library space that inspires study and learning</label>
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
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
           4)
        </td>
        <td class="question" align="left" valign="middle">
            Giving users individual attention
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q4_na">Question 4, Giving users individual attention, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q4_na" id="s1_q4_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_1"/>
           <label class="offscreen" for="s1_q4_min_1">1 of 9, lowest rating, rating of my minimum service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_2"/>
           <label class="offscreen" for="s1_q4_min_2">2 of 9, rating of my minimum service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_3"/>
           <label class="offscreen" for="s1_q4_min_3">3 of 9, rating of my minimum service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_4"/>
           <label class="offscreen" for="s1_q4_min_4">4 of 9, rating of my minimum service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_5"/>
           <label class="offscreen" for="s1_q4_min_5">5 of 9, rating of my minimum service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_6"/>
           <label class="offscreen" for="s1_q4_min_6">6 of 9, rating of my minimum service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_7"/>
           <label class="offscreen" for="s1_q4_min_7">7 of 9, rating of my minimum service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_8"/>
           <label class="offscreen" for="s1_q4_min_8">8 of 9, rating of my minimum service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_min" id="s1_q4_min_9"/>
           <label class="offscreen" for="s1_q4_min_9">9 of 9, highest rating, rating of my minimum service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_1"/>
           <label class="offscreen" for="s1_q4_des_1">1 of 9, lowest rating, rating of my desired service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_2"/>
           <label class="offscreen" for="s1_q4_des_2">2 of 9, rating of my desired service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_3"/>
           <label class="offscreen" for="s1_q4_des_3">3 of 9, rating of my desired service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_4"/>
           <label class="offscreen" for="s1_q4_des_4">4 of 9, rating of my desired service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_5"/>
           <label class="offscreen" for="s1_q4_des_5">5 of 9, rating of my desired service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_6"/>
           <label class="offscreen" for="s1_q4_des_6">6 of 9, rating of my desired service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_7"/>
           <label class="offscreen" for="s1_q4_des_7">7 of 9, rating of my desired service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_8"/>
           <label class="offscreen" for="s1_q4_des_8">8 of 9, rating of my desired service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_des" id="s1_q4_des_9"/>
           <label class="offscreen" for="s1_q4_des_9">9 of 9, highest rating, rating of my desired service level for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_1"/>
           <label class="offscreen" for="s1_q4_per_1">1 of 9, lowest rating, rating of my perceived service performance  for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_2"/>
           <label class="offscreen" for="s1_q4_per_2">2 of 9, rating of my perceived service performance  for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_3"/>
           <label class="offscreen" for="s1_q4_per_3">3 of 9, rating of my perceived service performance  for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_4"/>
           <label class="offscreen" for="s1_q4_per_4">4 of 9, rating of my perceived service performance  for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_5"/>
           <label class="offscreen" for="s1_q4_per_5">5 of 9, rating of my perceived service performance  for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_6"/>
           <label class="offscreen" for="s1_q4_per_6">6 of 9, rating of my perceived service performance  for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_7"/>
           <label class="offscreen" for="s1_q4_per_7">7 of 9, rating of my perceived service performance  for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_8"/>
           <label class="offscreen" for="s1_q4_per_8">8 of 9, rating of my perceived service performance  for question 4 Giving users individual attention</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q4_per" id="s1_q4_per_9"/>
           <label class="offscreen" for="s1_q4_per_9">9 of 9, highest rating, rating of my perceived service performance  for question 4 Giving users individual attention</label>
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           5)
        </td>
        <td class="question" align="left" valign="middle">
            A library Web site enabling me to locate information on my own
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q5_na">Question 5, A library Web site enabling me to locate information on my own, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q5_na" id="s1_q5_na"/>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_1"/>
           <label class="offscreen" for="s1_q5_min_1">1 of 9, lowest rating, rating of my minimum service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_2"/>
           <label class="offscreen" for="s1_q5_min_2">2 of 9, rating of my minimum service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_3"/>
           <label class="offscreen" for="s1_q5_min_3">3 of 9, rating of my minimum service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_4"/>
           <label class="offscreen" for="s1_q5_min_4">4 of 9, rating of my minimum service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_5"/>
           <label class="offscreen" for="s1_q5_min_5">5 of 9, rating of my minimum service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_6"/>
           <label class="offscreen" for="s1_q5_min_6">6 of 9, rating of my minimum service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_7"/>
           <label class="offscreen" for="s1_q5_min_7">7 of 9, rating of my minimum service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_8"/>
           <label class="offscreen" for="s1_q5_min_8">8 of 9, rating of my minimum service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_min" id="s1_q5_min_9"/>
           <label class="offscreen" for="s1_q5_min_9">9 of 9, highest rating, rating of my minimum service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_1"/>
           <label class="offscreen" for="s1_q5_des_1">1 of 9, lowest rating, rating of my desired service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_2"/>
           <label class="offscreen" for="s1_q5_des_2">2 of 9, rating of my desired service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_3"/>
           <label class="offscreen" for="s1_q5_des_3">3 of 9, rating of my desired service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_4"/>
           <label class="offscreen" for="s1_q5_des_4">4 of 9, rating of my desired service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_5"/>
           <label class="offscreen" for="s1_q5_des_5">5 of 9, rating of my desired service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_6"/>
           <label class="offscreen" for="s1_q5_des_6">6 of 9, rating of my desired service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_7"/>
           <label class="offscreen" for="s1_q5_des_7">7 of 9, rating of my desired service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_8"/>
           <label class="offscreen" for="s1_q5_des_8">8 of 9, rating of my desired service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_des" id="s1_q5_des_9"/>
           <label class="offscreen" for="s1_q5_des_9">9 of 9, highest rating, rating of my desired service level for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_1"/>
           <label class="offscreen" for="s1_q5_per_1">1 of 9, lowest rating, rating of my perceived service performance  for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_2"/>
           <label class="offscreen" for="s1_q5_per_2">2 of 9, rating of my perceived service performance  for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_3"/>
           <label class="offscreen" for="s1_q5_per_3">3 of 9, rating of my perceived service performance  for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_4"/>
           <label class="offscreen" for="s1_q5_per_4">4 of 9, rating of my perceived service performance  for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_5"/>
           <label class="offscreen" for="s1_q5_per_5">5 of 9, rating of my perceived service performance  for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_6"/>
           <label class="offscreen" for="s1_q5_per_6">6 of 9, rating of my perceived service performance  for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_7"/>
           <label class="offscreen" for="s1_q5_per_7">7 of 9, rating of my perceived service performance  for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_8"/>
           <label class="offscreen" for="s1_q5_per_8">8 of 9, rating of my perceived service performance  for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s1_q5_per" id="s1_q5_per_9"/>
           <label class="offscreen" for="s1_q5_per_9">9 of 9, highest rating, rating of my perceived service performance  for question 5 A library Web site enabling me to locate information on my own</label>
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="low rating" align="center" valign="middle"><abbr title="not applicable">n/a</abbr></td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
        <td class="rating" align="center" valign="middle">1</td>
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
  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s2" colspan="2">Please indicate your library usage patterns:</th>
        <th id="min_s2" colspan="9" class="column">&nbsp;</th>
      </tr>
    </thead>
    <tbody>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           6)
        </td>
        <td class="question" align="left" valign="middle">
            The library helps me stay abreast of developments in my field(s) of interest.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_1" />
           <label class="offscreen" for="s2_q6_min_1">Rating 1 of 9, strong disagreement, for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_2" />
           <label class="offscreen" for="s2_q6_min_2">Rating 2 of 9, for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_3" />
           <label class="offscreen" for="s2_q6_min_3">Rating 3 of 9, for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_4" />
           <label class="offscreen" for="s2_q6_min_4">Rating 4 of 9, for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_5" />
           <label class="offscreen" for="s2_q6_min_5">Rating 5 of 9, for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_6" />
           <label class="offscreen" for="s2_q6_min_6">Rating 6 of 9, for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_7" />
           <label class="offscreen" for="s2_q6_min_7">Rating 7 of 9, for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_8" />
           <label class="offscreen" for="s2_q6_min_8">Rating 8 of 9, for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q6_min" id="s2_q6_min_9" />
           <label class="offscreen" for="s2_q6_min_9">Rating 9 of 9, strong agreement, for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           7)
        </td>
        <td class="question" align="left" valign="middle">
            The library aids my advancement in my academic discipline or work.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_1" />
           <label class="offscreen" for="s2_q7_min_1">Rating 1 of 9, strong disagreement, for question 7 The library aids my advancement in my academic discipline or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_2" />
           <label class="offscreen" for="s2_q7_min_2">Rating 2 of 9, for question 7 The library aids my advancement in my academic discipline or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_3" />
           <label class="offscreen" for="s2_q7_min_3">Rating 3 of 9, for question 7 The library aids my advancement in my academic discipline or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_4" />
           <label class="offscreen" for="s2_q7_min_4">Rating 4 of 9, for question 7 The library aids my advancement in my academic discipline or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_5" />
           <label class="offscreen" for="s2_q7_min_5">Rating 5 of 9, for question 7 The library aids my advancement in my academic discipline or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_6" />
           <label class="offscreen" for="s2_q7_min_6">Rating 6 of 9, for question 7 The library aids my advancement in my academic discipline or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_7" />
           <label class="offscreen" for="s2_q7_min_7">Rating 7 of 9, for question 7 The library aids my advancement in my academic discipline or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_8" />
           <label class="offscreen" for="s2_q7_min_8">Rating 8 of 9, for question 7 The library aids my advancement in my academic discipline or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q7_min" id="s2_q7_min_9" />
           <label class="offscreen" for="s2_q7_min_9">Rating 9 of 9, strong agreement, for question 7 The library aids my advancement in my academic discipline or work.</label>
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           8)
        </td>
        <td class="question" align="left" valign="middle">
            The library enables me to be more efficient in my academic pursuits or work.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_1" />
           <label class="offscreen" for="s2_q8_min_1">Rating 1 of 9, strong disagreement, for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_2" />
           <label class="offscreen" for="s2_q8_min_2">Rating 2 of 9, for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_3" />
           <label class="offscreen" for="s2_q8_min_3">Rating 3 of 9, for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_4" />
           <label class="offscreen" for="s2_q8_min_4">Rating 4 of 9, for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_5" />
           <label class="offscreen" for="s2_q8_min_5">Rating 5 of 9, for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_6" />
           <label class="offscreen" for="s2_q8_min_6">Rating 6 of 9, for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_7" />
           <label class="offscreen" for="s2_q8_min_7">Rating 7 of 9, for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_8" />
           <label class="offscreen" for="s2_q8_min_8">Rating 8 of 9, for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q8_min" id="s2_q8_min_9" />
           <label class="offscreen" for="s2_q8_min_9">Rating 9 of 9, strong agreement, for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           9)
        </td>
        <td class="question" align="left" valign="middle">
            The library helps me distinguish between trustworthy and untrustworthy information.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_1" />
           <label class="offscreen" for="s2_q9_min_1">Rating 1 of 9, strong disagreement, for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_2" />
           <label class="offscreen" for="s2_q9_min_2">Rating 2 of 9, for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_3" />
           <label class="offscreen" for="s2_q9_min_3">Rating 3 of 9, for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_4" />
           <label class="offscreen" for="s2_q9_min_4">Rating 4 of 9, for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_5" />
           <label class="offscreen" for="s2_q9_min_5">Rating 5 of 9, for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_6" />
           <label class="offscreen" for="s2_q9_min_6">Rating 6 of 9, for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_7" />
           <label class="offscreen" for="s2_q9_min_7">Rating 7 of 9, for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_8" />
           <label class="offscreen" for="s2_q9_min_8">Rating 8 of 9, for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q9_min" id="s2_q9_min_9" />
           <label class="offscreen" for="s2_q9_min_9">Rating 9 of 9, strong agreement, for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
        </td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
      </tr>
      <tr class="odd">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           10)
        </td>
        <td class="question" align="left" valign="middle">
            The library provides me with the information skills I need in my work or study.
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_1" />
           <label class="offscreen" for="s2_q10_min_1">Rating 1 of 9, strong disagreement, for question 10 The library provides me with the information skills I need in my work or study.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_2" />
           <label class="offscreen" for="s2_q10_min_2">Rating 2 of 9, for question 10 The library provides me with the information skills I need in my work or study.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_3" />
           <label class="offscreen" for="s2_q10_min_3">Rating 3 of 9, for question 10 The library provides me with the information skills I need in my work or study.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_4" />
           <label class="offscreen" for="s2_q10_min_4">Rating 4 of 9, for question 10 The library provides me with the information skills I need in my work or study.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_5" />
           <label class="offscreen" for="s2_q10_min_5">Rating 5 of 9, for question 10 The library provides me with the information skills I need in my work or study.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_6" />
           <label class="offscreen" for="s2_q10_min_6">Rating 6 of 9, for question 10 The library provides me with the information skills I need in my work or study.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_7" />
           <label class="offscreen" for="s2_q10_min_7">Rating 7 of 9, for question 10 The library provides me with the information skills I need in my work or study.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_8" />
           <label class="offscreen" for="s2_q10_min_8">Rating 8 of 9, for question 10 The library provides me with the information skills I need in my work or study.</label>
        </td>
        <td class="" align="center" valign="middle">
           <input type="radio" name="s2_q10_min" id="s2_q10_min_9" />
           <label class="offscreen" for="s2_q10_min_9">Rating 9 of 9, strong agreement, for question 10 The library provides me with the information skills I need in my work or study.</label>
        </td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" align="center" valign="middle">1</td>
        <td class="rating" align="center" valign="middle">2</td>
        <td class="rating" align="center" valign="middle">3</td>
        <td class="rating" align="center" valign="middle">4</td>
        <td class="rating" align="center" valign="middle">5</td>
        <td class="rating" align="center" valign="middle">6</td>
        <td class="rating" align="center" valign="middle">7</td>
        <td class="rating" align="center" valign="middle">8</td>
        <td class="rating" align="center" valign="middle">9</td>
      </tr>
      <tr class="even">
        <td colspan="2">&nbsp;</td>
        <td class="rating" colspan="5" align="left" valign="middle">Strongly Disagree&nbsp;&nbsp;</td>
        <td class="rating" colspan="4" align="right" valign="middle">&nbsp;&nbsp;Strongly Agree</td>
      </tr>
    </tbody>
  </table>
  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s3" colspan="2">Please answer a few questions about yourself:</th>
        <th id="min_s3" colspan="9" class="column">&nbsp;</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           11)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q11_select"> The library that you use the most often:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q11_select" id="s3_q11_select">
             <option value="1++">Downtown Branch</option>
             <option value="1++">Southwest Branch</option>
             <option value="1++">Northeast Branch</option>
             <option value="1++">Bookmobile</option>
           </select>
        </td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           12)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q12_select">Age:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q12_select" id="s3_q12_select">
             <option value="1++">Under 18</option>
             <option value="1++">18-22</option>
             <option value="1++">23- 30</option>
             <option value="1++">31-45</option>
             <option value="1++">over 45</option>
           </select>
        </td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           13)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q13_select">Sex:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q13_select" id="s3_q13_select">
             <option value="1++">Male</option>
             <option value="1++">Female</option>
           </select>
        </td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           14)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q14_select">Discipline:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q14_select" id="s3_q14_select">
             <option value="1++">Agriculture / Environmental Studies</option>
             <option value="1++">Business</option>
             <option value="1++">Communications / Journalism</option>
             <option value="1++">Education</option>
             <option value="1++">Engineering / Computer Science</option>
             <option value="1++">General Studies</option>
             <option value="1++">Health Sciences</option>
             <option value="1++">Humanities</option>
             <option value="1++">Law</option>
             <option value="1++">Military / Naval Science</option>
             <option value="1++">Other</option>
             <option value="1++">Performing &amp; Fine Arts</option>
             <option value="1++">Science / Math</option>
             <option value="1++">Psychology/Sociology</option>
             <option value="1++">Undecided</option>
             <option value="1++">Miscellaneous</option>
             <option value="1++">Architecture</option>
           </select>
        </td>
      </tr>
    </tbody>
  </table>
  <p class="submit"><input type="submit" value="Submit Survey Responses"/></p>
</form> 
"""

example_info.script      = """"""

example_info.style       = """
  <style type="text/css">
/* CSS Document */


.offscreen {
  position: absolute;
  left: -200em;
  top: -20em;
}

table.survey {
  margin-bottom: 2em;
}

table.survey th {
  padding: .5em;
  text-align: center;
}

table.survey th.prefix {
  border-bottom: solid white 2px;
}

table.survey th.column {
  border-left: solid white 2px;
  border-bottom: solid white 2px;
}

table.survey th.low,
table.survey td.low,
table.survey th.na {
  border-left: solid white 2px;
}

table.survey th.low,
table.survey th.high,
table.survey th.na {
  font-weight: normal;
  font-size: 90%;
}  

table.survey th.low {
  font-size: 90%;
}

table.survey th.high {
  text-align: right;
}

table.survey thead {
  background-color:#CCCCFF;
}

table.survey tr.odd td {
  background-color: #EEEEEE;
}

table.survey tr.even {
  background-color: #FFFFCC;
}

table.survey tr.top td {
  border-top: solid white 2px;
  padding-top: .125em;
}

table.survey td,
table.survey td {
  padding: 0;
  margin: 0;
}

table.survey td input,
table.survey td input {
  padding: 0;
  margin: 0;
}


table.survey td.rating {
  padding: 0;
  margin: 0;
  font-size: 70%;
  color: #606060;
}

table.survey td.question {
  font-size: 100%;
  font-weight: normal;
  padding-right: 1.25em;
}

table.survey td.number {
  font-size: 100%;
  font-weight: bold;
  width: 2em;
  padding-left: .125em;
}

table.survey td.select {
  width: 30em;
}

table.survey td.select select{
  margin: .5em;
}

ul.survey li {
  list-style: none;
}

ul.survey li div {
  width: 10em;
  padding-right: .5em;
  text-align: right;
  font-weight: bold;
  float: left;
}

table.survey h3 {
  margin: 0;
  padding: 0;
  font-size: 100%;
  font-weight: normal;
}

  </style>
"""

example3 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
add_script_reference( example3, script1 )

ExampleGroup.objects.get(slug='labeling').examples.add(example3)

# =============================
# Example 4
# =============================
order += 1

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_label]
example_info.title       = 'Complex Survey - @select@ elements replaced @input[type=radio]@ buttons for selecting options'
example_info.permanent_slug = 'label4'

example_info.description = """
* Form controls do have @label@ markup.
* Labels are long and are therefore are positioned off screen.
* Radio button groups are replaced with select elements, this greatly simplifies labels.
* Headers are used to mark sections of the survey.
"""

example_info.keyboard    = """
"""

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "CONTROL_1_T1", "", "")
rr2 = rule_reference_object("CONTROL_12", "pass", "na", "", "", "")

example_info.rule_references = [rr1,rr2]


example_info.html        = """
<form method="post" action="form-example-survey-label.php">

  <!--
      Using hidden LABELs to provide effective labels for form controls densely packed in layout tables.
   -->

  <h3>Survey Instructions</h3>

  <p>Please rate the following statements (1 is lowest, 9 is highest) by indicating:</p>

  <ul class="survey">
     <li><div>Minimum --</div> the number that represents the minimum level of service that you would find acceptable</li>
     <li><div>Desired --</div> the number that represents the level of service that you personally want</li>
     <li><div>Perceived --</div> the number that represents the level of service that you believe our library currently provides</li>
  </ul>

  <p>For each item, you must EITHER rate the item in all three columns OR identify the item as "N/A" (not applicable). Selecting "N/A" will override all other answers for that item.</p>

  <h3>Survey Questions</h3>

  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s1" colspan="2">When it comes to..</th>
        <th id="na_s1"   class="column"><abbr title="Not Applicable">N/A</abbr></th>
        <th id="min_s1" class="column">My Minimum<br/>Service Level Is</th>
        <th id="des_s1" class="column">My Desired<br/>Service Level Is</th>
        <th id="per_s1" class="column">Perceived Service<br/>Performance Is</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           1)
        </td>
        <td class="question" align="left" valign="middle">
            Employees who instill confidence in users
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q1_na">Question 1, Employees who instill confidence in users, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q1_na" id="s1_q1_na"/>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q1_min">Rate my minimum service level, for question 1 Employees who instill confidence in users</label>
           <select name="s1_q1_min" id="s1_q1_min">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q1_desc">Rate my desired service level, for question 1 Employees who instill confidence in users</label>
           <select name="s1_q1_desc" id="s1_q1_desc">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q1_pre">Rate my perceived service performance, for question 1 Employees who instill confidence in users</label>
           <select name="s1_q1_pre" id="s1_q1_pre">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           2)
        </td>
        <td class="question" align="left" valign="middle">
            Making electronic resources accessible from my home or office
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q2_na">Question 2, Making electronic resources accessible from my home or office, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q2_na" id="s1_q2_na"/>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q2_min">Rate my minimum service level, for question 2 Making electronic resources accessible from my home or office</label>
           <select name="s1_q2_min" id="s1_q2_min">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q2_desc">Rate my desired service level, for question 2 Making electronic resources accessible from my home or office</label>
           <select name="s1_q2_desc" id="s1_q2_desc">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q2_pre">Rate my perceived service performance, for question 2 Making electronic resources accessible from my home or office</label>
           <select name="s1_q2_pre" id="s1_q2_pre">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           3)
        </td>
        <td class="question" align="left" valign="middle">
            Library space that inspires study and learning
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q3_na">Question 3, Library space that inspires study and learning, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q3_na" id="s1_q3_na"/>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q3_min">Rate my minimum service level, for question 3 Library space that inspires study and learning</label>
           <select name="s1_q3_min" id="s1_q3_min">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q3_desc">Rate my desired service level, for question 3 Library space that inspires study and learning</label>
           <select name="s1_q3_desc" id="s1_q3_desc">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q3_pre">Rate my perceived service performance, for question 3 Library space that inspires study and learning</label>
           <select name="s1_q3_pre" id="s1_q3_pre">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           4)
        </td>
        <td class="question" align="left" valign="middle">
            Giving users individual attention
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q4_na">Question 4, Giving users individual attention, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q4_na" id="s1_q4_na"/>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q4_min">Rate my minimum service level, for question 4 Giving users individual attention</label>
           <select name="s1_q4_min" id="s1_q4_min">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q4_desc">Rate my desired service level, for question 4 Giving users individual attention</label>
           <select name="s1_q4_desc" id="s1_q4_desc">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q4_pre">Rate my perceived service performance, for question 4 Giving users individual attention</label>
           <select name="s1_q4_pre" id="s1_q4_pre">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           5)
        </td>
        <td class="question" align="left" valign="middle">
            A library Web site enabling me to locate information on my own
        </td>
        <td class="low" align="center" valign="middle" >
           <label class="offscreen" for="s1_q5_na">Question 5, A library Web site enabling me to locate information on my own, is not applicable to me</label>
           <input class="low" type="checkbox" name="s1_q5_na" id="s1_q5_na"/>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q5_min">Rate my minimum service level, for question 5 A library Web site enabling me to locate information on my own</label>
           <select name="s1_q5_min" id="s1_q5_min">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q5_desc">Rate my desired service level, for question 5 A library Web site enabling me to locate information on my own</label>
           <select name="s1_q5_desc" id="s1_q5_desc">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

        <td align="center">
           <label class="offscreen" for="s1_q5_pre">Rate my perceived service performance, for question 5 A library Web site enabling me to locate information on my own</label>
           <select name="s1_q5_pre" id="s1_q5_pre">
             <option>select rating</option>
             <option>1, lowest</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, highest</option>
          </select>
        </td>

      </tr>
    </tbody>
  </table>
  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s2" colspan="2">Please indicate your library usage patterns:</th>
        <th id="min_s2" colspan="9" class="column">Rating</th>
      </tr>
    </thead>
    <tbody>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           6)
        </td>
        <td class="question" align="left" valign="middle">
            The library helps me stay abreast of developments in my field(s) of interest.
        </td>
        <td>
           <label class="offscreen" for="s2_q6_desc">Rating for question 6 The library helps me stay abreast of developments in my field(s) of interest.</label>
           <select name="s2_q6_desc" id="s2_q6_desc">
             <option>select rating</option>
             <option>1, strongest disagreement</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, strongest agreement</option>
          </select>
        </td>

      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           7)
        </td>
        <td class="question" align="left" valign="middle">
            The library aids my advancement in my academic discipline or work.
        </td>
        <td>
           <label class="offscreen" for="s2_q7_desc">Rating for question 7 The library aids my advancement in my academic discipline or work.</label>
           <select name="s2_q7_desc" id="s2_q7_desc">
             <option>select rating</option>
             <option>1, strongest disagreement</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, strongest agreement</option>
          </select>
        </td>

      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           8)
        </td>
        <td class="question" align="left" valign="middle">
            The library enables me to be more efficient in my academic pursuits or work.
        </td>
        <td>
           <label class="offscreen" for="s2_q8_desc">Rating for question 8 The library enables me to be more efficient in my academic pursuits or work.</label>
           <select name="s2_q8_desc" id="s2_q8_desc">
             <option>select rating</option>
             <option>1, strongest disagreement</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, strongest agreement</option>
          </select>
        </td>

      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           9)
        </td>
        <td class="question" align="left" valign="middle">
            The library helps me distinguish between trustworthy and untrustworthy information.
        </td>
        <td>
           <label class="offscreen" for="s2_q9_desc">Rating for question 9 The library helps me distinguish between trustworthy and untrustworthy information.</label>
           <select name="s2_q9_desc" id="s2_q9_desc">
             <option>select rating</option>
             <option>1, strongest disagreement</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, strongest agreement</option>
          </select>
        </td>

      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           10)
        </td>
        <td class="question" align="left" valign="middle">
            The library provides me with the information skills I need in my work or study.
        </td>
        <td>
           <label class="offscreen" for="s2_q10_desc">Rating for question 10 The library provides me with the information skills I need in my work or study.</label>
           <select name="s2_q10_desc" id="s2_q10_desc">
             <option>select rating</option>
             <option>1, strongest disagreement</option>
             <option>2</option>
             <option>3</option>
             <option>4</option>
             <option>5</option>
             <option>6</option>
             <option>7</option>
             <option>8</option>
             <option>9, strongest agreement</option>
          </select>
        </td>

      </tr>
    </tbody>
  </table>
  <table class="survey" cellspacing="0" cellpadding="0">
    <thead>
      <tr>
        <th class="prefix" id="pre_s3" colspan="2">Please answer a few questions about yourself:</th>
        <th id="min_s3" colspan="9" class="column">Rating</th>
      </tr>
    </thead>
    <tbody>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           11)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q11_select"> The library that you use the most often:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q11_select" id="s3_q11_select">
             <option value="1++">Downtown Branch</option>
             <option value="1++">Southwest Branch</option>
             <option value="1++">Northeast Branch</option>
             <option value="1++">Bookmobile</option>
           </select>
        </td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           12)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q12_select">Age:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q12_select" id="s3_q12_select">
             <option value="1++">Under 18</option>
             <option value="1++">18-22</option>
             <option value="1++">23- 30</option>
             <option value="1++">31-45</option>
             <option value="1++">over 45</option>
           </select>
        </td>
      </tr>
      <tr class="odd top">
        <td class="number" align="left" valign="middle">
           13)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q13_select">Sex:</label>
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q13_select" id="s3_q13_select">
             <option value="1++">Male</option>
             <option value="1++">Female</option>
           </select>
        </td>
      </tr>
      <tr class="even top">
        <td class="number" align="left" valign="middle">
           14)
        </td>
        <td class="question" align="left" valign="middle">
            <label for="s3_q14_select">Discipline:</label>el class="offscreen" for="s1_q1_min_3">3 of 9, 
        </td>
        <td class="low select" align="left" valign="middle">
           <select name="s3_q14_select" id="s3_q14_select">
             <option value="1++">Agriculture / Environmental Studies</option>
             <option value="1++">Business</option>
             <option value="1++">Communications / Journalism</option>
             <option value="1++">Education</option>
             <option value="1++">Engineering / Computer Science</option>
             <option value="1++">General Studies</option>
             <option value="1++">Health Sciences</option>
             <option value="1++">Humanities</option>
             <option value="1++">Law</option>
             <option value="1++">Military / Naval Science</option>
             <option value="1++">Other</option>
             <option value="1++">Performing &amp; Fine Arts</option>
             <option value="1++">Science / Math</option>
             <option value="1++">Psychology/Sociology</option>
             <option value="1++">Undecided</option>
             <option value="1++">Miscellaneous</option>
             <option value="1++">Architecture</option>
           </select>
        </td>
      </tr>
    </tbody>
  </table>
  <p class="submit"><input type="submit" value="Submit Survey Responses"/></p>
</form>   
"""

example_info.script      = """"""

example_info.style       = """
  <style type="text/css">
/* CSS Document */


.offscreen {
  position: absolute;
  left: -200em;
  top: -20em;
}

table.survey {
  margin-bottom: 2em;
}

table.survey th {
  padding: .5em;
  text-align: center;
}

table.survey th.prefix {
  border-bottom: solid white 2px;
}

table.survey th.column {
  border-left: solid white 2px;
  border-bottom: solid white 2px;
}

table.survey th.low,
table.survey td.low,
table.survey th.na {
  border-left: solid white 2px;
}

table.survey th.low,
table.survey th.high,
table.survey th.na {
  font-weight: normal;
  font-size: 90%;
}  

table.survey th.low {
  font-size: 90%;
}

table.survey th.high {
  text-align: right;
}

table.survey thead {
  background-color:#CCCCFF;
}

table.survey tr.odd td {
  background-color: #EEEEEE;
}

table.survey tr.even {
  background-color: #FFFFCC;
}

table.survey tr.top td {
  border-top: solid white 2px;
  padding-top: .125em;
}

table.survey td,
table.survey td {
  padding: 0;
  margin: 0;
}

table.survey td input,
table.survey td input {
  padding: 0;
  margin: 0;
}


table.survey td.rating {
  padding: 0;
  margin: 0;
  font-size: 70%;
  color: #606060;
}

table.survey td.question {
  font-size: 100%;
  font-weight: normal;
  padding-right: 1.25em;
}

table.survey td.number {
  font-size: 100%;
  font-weight: bold;
  width: 2em;
  padding-left: .125em;
}

table.survey td.select {
  width: 30em;
}

table.survey td.select select{
  margin: .5em;
}

ul.survey li {
  list-style: none;
}

ul.survey li div {
  width: 10em;
  padding-right: .5em;
  text-align: right;
  font-weight: bold;
  float: left;
}

table.survey h3 {
  margin: 0;
  padding: 0;
  font-size: 100%;
  font-weight: normal;
}

  </style>
"""

example4 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
add_script_reference( example4, script1 )

ExampleGroup.objects.get(slug='labeling').examples.add(example1)

# =============================
# Example 5
# =============================
order += 1
example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_label]
example_info.title       = '@label@ element - Survey with @label@ elements'
example_info.permanent_slug = 'label5'

example_info.description = """
* The @label@ element content provides effective labels to form controls of following types: 
** input element of @type="text"@, @type="radio"@, and @type="password"@
** @select@ element
** @textarea@ element
* The effective labels of the @input@ elements of @type="radio"@ in this example include the content of the @legend@ element associated with the @fieldset@ element containing them.
* The tabindex attribute is defined for the p element that contains an instruction. This ensures that screen reader users will access the instruction text, which normally is a non-focusable text content, as they TAB through the form controls.
"""

example_info.keyboard    = """
"""

example_info.markup = [m1]

rr1 = rule_reference_object("CONTROL_1", "pass", "na", "", "", "")

example_info.rule_references = [rr1]

example_info.html        = """
<form method="post" action="form-example-sub-label.php">

  <!--
      Text box input form controls with LABEL markup using the FOR and ID attributes
   -->
  <p class="text" ><label for="first">First Name</label><input type="text" name="first" id="first" size="20" value=""/></p>
  <p class="text" ><label for="last">Last Name</label><input type="text" name="last" id="last" size="30" value=""/></p>

  <!--
      Checkbox input form control with LABEL markup using the FOR and ID attributes
   -->
  <p class="check" ><input type="checkbox" name="check1" id="check1"/><label for="check1">Remove from E-mail list</label></p>

  <!--
      More text box input form controls with LABEL markup using the FOR and ID attributes
   -->
  <p class="text" ><label for="email1">E-mail Address</label><input type="text" name="email1" id="email1" size="40" value=""/></p>
  <p class="text" ><label for="email2">Confirm E-mail</label><input type="text" name="email2" id="email2" size="40" value=""/></p>

  <!--
      Select form control with LABEL markup using the FOR and ID attributes
   -->
  <p class="select">
     <label for="select1">Subscription Type</label>
     <select name="select1" id="select1">
      <option value="0" selected="selected">Regular</option>
      <option value="1">Digest (Traditional) </option>
      <option value="2">Digest (MIME format)</option>
      <option value="3">Digest (HTML format)</option>
      <option value="4">Index (traditional)</option>
      <option value="5">Index (HTML format)</option>
    </select>
  </p>

  <!--
      Radio button form controls with LABEL markup using the FOR and ID attributes.  The FIELDSET and LEGEND elements are used to give the group of form controls a label.
   -->
  <fieldset class="radio">
    <legend>Acknowledgement of posting</legend>
    <ul class="radio">
      <li><input type="radio" name="radio1" id="radio10" value="0" checked="checked"/><label for="radio10">No acknowledgements</label></li>
      <li><input type="radio" name="radio1" id="radio11" value="1"/><label for="radio11">Short message confirming receipt</label></li>
      <li><input type="radio" name="radio1" id="radio12" value="2"/><label for="radio12">Receive copy of own postings</label></li>
    </ul>
  </fieldset>

  <!--
      Setting the TABINDEX attribute to "0" is used to make sure screen reader users can easily find the instructions for filling out the next part of the form.  NOTE: The tabindex technique results in invalid HTML, so the tabindex attribute should be added through scripting.
   -->
<p class="instruction" tabindex="0">If you would like to have access to the private archive you will need to create a password.  Your e-mail address will be used as your login id.</p>
  <!--
      Password form controls with LABEL markup using the FOR and ID attributes
   -->
  <p class="text" ><label for="pass1">Password</label><input type="password" name="pass1" id="pass1" size="20" value=""/></p>
  <p class="text" ><label for="pass2">Confirm Password</label><input type="password" name="pass2" id="pass2" size="20" value=""/></p>

  <!--
      Textarea form control with LABEL markup using the FOR and ID attributes
   -->
  <p class="text" ><label for="textarea1">Note to list administrator</label><textarea name="textarea1" id="textarea1" rows="10" cols="80"></textarea></p>
  <p class="submit"><input type="submit" value="Submit Request"/></p>
</form>
"""

example_info.script      = """"""

example_info.style       = """
 /* html test pages styles */


table.examples thead {
   background-color: #F8F8F8;
}

table.examples th.desc {
   font-weight: normal;
   text-align: left;
}

table.examples td {
   text-align: center;
}


table.examples th.res {
   font-weight: normal;
   text-align: center;
}

table.examples tr.b {
  background-color: #DDFFDD;
}

table.examples tr.b th.res{
  color: #228B22;
}

table.examples tr.f {
  background-color: #FFDDDD;
}

table.examples tr.f th.res {
  color: #FF0000;
}

table.examples tr.p {
  background-color: #F0E68C;
}

table.examples tr.p th.res {
  color: #904000;
}

table.htmlbp tr.e {
  background-image: url('../images/exp.png');
}

table.htmlbp tr.e th.res{
  color: black;
}
"""

example5 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
add_script_reference( example5, script1 )

ExampleGroup.objects.get(slug='labeling').examples.add(example5)
