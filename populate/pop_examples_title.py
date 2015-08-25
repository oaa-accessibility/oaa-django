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
example_info1.title       = 'Page unique title matches @H1@ element'
example_info1.permanent_slug = ''

example_info1.description = """
* The one and only title element has content.
* The one h1 element has content.
* The words in the h1 element are also in the title element.
"""
example_info1.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='title')
m2 = ElementDefinition.objects.get(spec=spec_html4, element='h1')

example_info1.markup = [m1,m2]

rr1 = rule_reference_object("TITLE_1", "na", "pass", "TITLE_1_T1", "", "")
rr2 = rule_reference_object("TITLE_2", "pass", "pass", "TITLE_2_T1", "", "")

example_info1.rule_references = [rr1,rr2]

example_info1.html        = """
 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head>
  <HL1><title>University of Illinois at Urbana-Champaign</title></HL1>
  </head>
  
<body>
  <HL1><h1>University of Illinois at Urbana-Champaign</h1></HL1>
  
  <div id="container">
    <div id="navigation">
    <h2><a name="un_navbar" />Main Menu</h2>
    <ul>
      <li><a href="/tt/www.uiuc.edu/overview/info/directories.html">Campus Units (a-z)</a></li>
        <li><a href="https://transcoder.usablenet.com/tt/login.express.cites.uiuc.edu/">Express Email</a></li>
      <li><a href="/tt/www.uiuc.edu/ricker/PH">Find People</a></li>
      <li><a href="/tt/www.library.uiuc.edu/">Library</a></li>
      <li><a href="/tt/www.uiuc.edu/ricker/CampusMap">Maps</a></li>
      <li><a href="/tt/www.uiuc.edu/cms/0.navigation">UI Now</a>&nbsp;&nbsp;RSS index</li>
    </ul>
      </div>
    
    <div id="content">
    <h3>Colleges &amp; Schools</h3>
      <ul>
      <li><a href="/tt/www.aces.uiuc.edu/">College of Agricultural, Consumer and Environmental Sciences</a></li>
      <li><a href="/tt/www.ahs.uiuc.edu/">College of Applied Health Sciences</a></li>
      <li><a href="/tt/www.aviation.uiuc.edu/">Institute of Aviation</a></li>
      <li><a href="/tt/www.business.uiuc.edu/">College of Business</a></li>
      <li><a href="/tt/www.comm.uiuc.edu/">College of Media</a></li>
      <li><a href="/tt/www.ed.uiuc.edu/">College of Education</a></li>
      <li><a href="/tt/www.engr.uiuc.edu/">College of Engineering</a></li>
      <li><a href="/tt/www.faa.uiuc.edu/">College of Fine and Applied Arts</a></li>
      <li><a href="/tt/www.dgs.uiuc.edu/">Division of General Studies</a></li>
      <li><a href="/tt/www.grad.uiuc.edu/">Graduate College</a></li>
      <li><a href="/tt/www.ilir.uiuc.edu/">Institute of Labor and Industrial Relations</a></li>
      <li><a href="/tt/www.law.uiuc.edu/">College of Law</a></li>
      <li><a href="/tt/www.las.uiuc.edu/">College of Liberal Arts and Sciences</a></li>
      <li><a href="/tt/www.lis.uiuc.edu/">Graduate School of Library and Information Science</a></li>
      <li><a href="/tt/www.med.uiuc.edu/">College of Medicine at Urbana-Champaign</a></li>
      <li><a href="/tt/www.social.uiuc.edu/">School of Social Work</a></li>
      <li><a href="/tt/www.cvm.uiuc.edu/">College of Veterinary Medicine</a></li>
        </ul>
    </div>  

    <p>
      <ul>
      <li><a href="/tt/www.uiuc.edu/resources/aboutsite.html">About this Site</a></li>
      <li><a href="/tt/www.uiuc.edu/resources/sitemap.html">Site Map</a></li>
      <li><a href="/tt/www.uiuc.edu/overview/info/contactus.html">Contact Us</a></li>
      <li>Text Only</li>
      <li><a href="/tt/www.vpaa.uillinois.edu/policies/web_privacy.asp?bch=1onClick=">Privacy Policy</a></li>
    </ul>
      <p><a href="/tt/www.uillinois.edu/">University Administration</a>, <a href="/tt/www.uis.edu">Springfield</a>, <a href="/tt/www.uic.edu/index.html/">Chicago</a>, <a href="/tt/global.uillinois.edu">Global Campus</a> | &copy; 2007 The Board of Trustees at the University of Illinois <a href="/tt/www.uiuc.edu/overview/moreResources.html">more resources</a></p>
    </p>
  </div>
  
  <p><a href="#" rel="nofollow">Top of page</a></p>
      
</body>
</html> 
"""

example_info1.style       = """"""

example1 = create_example(example_info1)
