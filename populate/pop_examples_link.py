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

eg_links = ExampleGroup.objects.get(slug="links")

example_info1             = example_object()
example_info1.example_groups = [eg_links]
example_info1.title       = 'Making the same link text unique using @hidden span@ elements'
example_info1.permanent_slug = 'link1'

example_info1.description = """
* The possible problem of links as in this example is that there are multiple "Edit" and "Delete" links that have same text but carry out different functions when clicked.
* To solve this problem, parts of link texts are @hidden@ using span element with edited CSS position property to differentiate link texts that are identical otherwise and to clarify the function of the link.
"""
example_info1.keyboard    = """
"""

spec_html4 = LanguageSpec.objects.get(url_slug='html4')

m1 = ElementDefinition.objects.get(spec=spec_html4, element='a', attribute='href')
m2 = ElementDefinition.objects.get(spec=spec_html4, element='table', attribute='summary')
m3 = ElementDefinition.objects.get(spec=spec_html4, element='td', attribute='headers')
m4 = ElementDefinition.objects.get(spec=spec_html4, element='th', attribute='id')

example_info1.markup = [m1, m2, m3, m4]

rr1 = rule_reference_object("LINK_2", "fail", "fail", "", "", "")
rr2 = rule_reference_object("LINK_4", "pass", "pass", "LINK_4_T3","","")
rr3 = rule_reference_object("LINK_1", "pass", "pass", "LINK_1_T2","","")
rr4 = rule_reference_object("LINK_3", "pass", "pass", "LINK_3_T1","","")

example_info1.rule_references = [rr1,rr2,rr3,rr4]

example_info1.html        = """
<h3>Course Information</h3>
<table id="schedule" summary="List of Courses and Times">
  <tr>
    <th id="number">No.</th>
  <th id="time">Time</th>
  <th id="coursetitle">Course Title</th>
  <th id="instructor">Instructor</th>
  <th id="edit"></th>
  <th id="delete"></th>
  </tr>
  
  <tr>
    <th id="1" headers="number">1</th>
  <td headers="time 1">9:00-9:50</td>
  <td headers="coursetitle 1"><a href="#german">Intermediate German I</a></d>
  <td headers="instructor 1"><a href="#bkneer">Boris Kneer</a></td>
  <td headers="edit 1"><HL1> <a href="#edit_1"><HL2>Edit</HL2><span class="hidden"><HL2>course 1</HL2></span></a></HL1></td>
  <td headers="delete 1"><HL1><a href="#delete_1"><HL2>Delete</HL2><span class="hidden"><HL2> course 1</HL2></span></a></HL1></td>
  </tr>

  <tr>
    <th id="2" headers="number">2</th>
  <td headers="time 2">10:00-11:20</td>
  <td headers="coursetitle 2"><a href="#entomology">Intro to Entomology</a></d>
  <td headers="instructor 2"><a href="#rlobe">Rose Lobe</a></td>
  <td headers="edit 2"><HL1><a href="#edit_2"><HL2>Edit</HL2><span class="hidden">  <HL2>course 2</HL2></span></a></HL1></td>
  <td headers="delete 2"><HL1><a href="#delete_2"><HL2>Delete</HL2><span class="hidden">  <HL2>course 2</HL2></span></a></HL1></td>
  </tr>

  <tr>
    <th id="3" headers="number">3</th>
  <td headers="time 3">13:00-14:50</td>
  <td headers="coursetitle 3"><a href="#toxicology">Environmental Toxicology</a></d>
  <td headers="instructor 3"><a href="#mgoodman">Michael Goodman</a></td>
  <td headers="edit 3"><a href="#edit_3">Edit<span class="hidden"> course 3</span></a></td>
  <td headers="delete 3"><a href="#delete_3">Delete<span class="hidden"> course 3</span></a></td>
  </tr>

  <tr>
    <th id="4" headers="number">4</th>
  <td headers="time 4">15:00-15:50</td>
  <td headers="coursetitle 4"><a href="#psycholinguistics">Psycholinguistics</a></d>
  <td headers="instructor 4"><a href="#landerson">Lisa Anderson</a></td>
  <td headers="edit 4"><a href="#edit_4">Edit<span class="hidden"> course 4</span></a></td>
  <td headers="delete 4"><a href="#delete_4">Delete<span class="hidden"> course 4</span></a></td>
  </tr>
</table> 
"""

example_info1.script      = """"""

example_info1.style       = """

#example_html {
  background-color: #FFFFFF;
}

span.hidden {
  position: absolute;
  top: -20em;
  left: -200em;
}

table#schedule td {
  padding-right: 1em;
  padding-left: .3em;
  padding-top: .2em;
  padding-bottom: .2em;
  border-bottom: 1px solid #88ccaa;
}

table#schedule th {
  background-color: #88ccaa;
}

table#schedule th#number {
  background-color: #88ccaa;
  padding-right: .3em;
  padding-left: .3em;
}

table#schedule {
  border-right: 1px solid #99ddbb;
  border-spacing: 0;
} 
"""

example1 = create_example(example_info1)
ExampleGroup.objects.get(slug='links').examples.add(example1)
# =============================
# Example 2
# =============================

example_info2             = example_object()
example_info2.example_groups = [eg_links]
example_info2.title       = 'Link text does not accurately describe link @href@ attribute'
example_info2.permanent_slug = ''

example_info2.description = """
* To solve this problem, parts of link texts are @hidden@ using @span@ element with edited CSS @position@ property to differentiate link texts that are identical otherwise and to clarify the function of the link.
* Taken by itself, link text "Full Story" does not provide sufficient information about the destination.
* The @alt@ attribute of an @img@ element that is used as a link should not describe the image, but describe the destination. However, in this example, since @img@ element links have same destinations as text links, the @alt@ attributes should be empty.
* This example is based on "Inside llinois" page of the News Bureau of UIUC.
"""
example_info2.keyboard    = """
"""

example_info2.markup = [m1]

rr1 = rule_reference_object("LINK_2", "fail", "fail", "", "", "")
rr2 = rule_reference_object("LINK_4", "fail", "fail", "","","")
rr3 = rule_reference_object("LINK_1", "fail", "fail", "","","")
rr4 = rule_reference_object("LINK_3", "pass", "pass", "LINK_3_T1","","")

example_info2.rule_references = [rr1,rr2,rr3,rr4]

example_info2.html        = """
 <div class="inil">
  <div class="inil_pic">
    <HL1><a href="http://www.news.uiuc.edu/news/08/0701email.html"><img src="{{EXAMPLE_MEDIA}}images/white_tiffany_b.jpg" alt="<HL2>Tiffany Barnett White</HL2>" id="newsphoto" width="70" height="70"/></a></HL1>
  </div>
  <h3 id="newshead">Personal Information in e-mail marketing can backfire, study indicates</h3>
  <p id="inil_text">Businesses rick chasing away prospective customers when they send chummy e-mails that bandy around people's names, hobbies and other personal information to pitch sales, according to a new study of the popular marketing tool. <a href="http://www.news.uiuc.edu/news/08/0701email.html">Full Story</a></p>
</div>  
  
<div class="inil">
  <div class="inil_pic">
    <HL1><a href="http://www.news.uiuc.edu/news/08/0715athapaskans.html"><img src="{{EXAMPLE_MEDIA}}images/geronimo_b.jpg" alt="<HL2>Geronimo</HL2>" id="newsphoto" width="70" height="70"/></a></HL1>
  </div>
  <h3 id="newshead">Y chromosome study sheds light on Athapaskan migration to southwest U.S.</h3>
  <p id="inil_text">A large-scale genetic study of native North Americans offers new insights into the migration of a small group of Athapaskan natives from their subarctic home in northwest North America to the southwestern United States. The migration, which left no known archaeological trace, is believed to have occurred about 500 years ago. <HL1><a href="http://www.news.uiuc.edu/news/08/0715athapaskans.html"><HL2>Full Story</HL2></a></HL1></p>
</div>  
  
<div class="inil">
  <div class="inil_pic">
    <a href="http://www.news.uiuc.edu/news/08/0711infants.html"><img src="{{EXAMPLE_MEDIA}}images/JKim_b.jpg" alt="Juhee Kim" id="newsphoto" width="70" height="70"/></a>
  </div>
  <h3 id="newshead">Non-parental care of infants tied to unfavorable feeding practices</h3>
  <p id="inil_text">With more new mothers in the workplace than ever before, there has been a corresponding increase in the number of child-care facilities in the United States. At the same time, data from a variety of sources point to a growing prevalence of overweight infants and toddlers. Is there a connection? <a href="http://www.news.uiuc.edu/news/08/0711infants.html">Full Story</a></p>
</div>  
  
<div class="inil">
  <div class="inil_pic">
    <a href="http://www.news.uiuc.edu/news/08/0707hiring.html"><img src="{{EXAMPLE_MEDIA}}images/Lawler,John_w.jpg" alt="John Lawler" id="newsphoto" width="70" height="70"/></a>
  </div>
  <h3 id="newshead">U.S. firms a role model for fair hiring standards, study says</h3>
  <p id="inil_text">U.S. companies are helping spread fair hiring practices across the world as they set up shop in developing nations, according to a new study of gender and age discrimination co-written by a University of Illinois labor expert. <a href="http://www.news.uiuc.edu/news/08/0707hiring.html">Full Story</a></p>
</div>
"""

example_info2.script      = """"""

example_info2.style       = """

#example_html {
  background-color: #FFFFFF;
}

.inil {
  margin-top: .5em;
}

.inil_pic {
  float: left;
  margin-right: .7em;
}

h3#newshead {
  font-weight: bolder;
  color: #ff5555;
  font-family: Times New Roman, Times, serif;
  font-size: large;
}

h3#newshead a:link{
  font-weight: bolder;
  color: #ff5555;
  font-family: Times New Roman, Times, serif;
  font-size: large;
  text-decoration: none;
}

h3#newshead a:hover{
  font-weight: bolder;
  color: #5555dd;
  font-family: Times New Roman, Times, serif;
  font-size: large;
  text-decoration: underline;
}

h3#newshead a:visited{
  font-weight: bolder;
  color: #ff5555;
  font-family: Times New Roman, Times, serif;
  font-size: large;
  text-decoration: none;
}

h3#newshead a:active{
  font-weight: bolder;
  color: #ff5555;
  font-family: Times New Roman, Times, serif;
  font-size: large;
  text-decoration: none;
}

p#inil_text a:link {
  color: #5555dd;
}

img#newsphoto {
  padding-right: 0;
}

"""

example2 = create_example(example_info2)
ExampleGroup.objects.get(slug='links').examples.add(example2)
# =============================
# Example 3
# =============================

example_info3             = example_object()
example_info3.example_groups = [eg_links]
example_info3.title       = 'Unambiguous Text Link'
example_info3.permanent_slug = ''

example_info3.description = """
* The @h3@ elements, that are the titles of news articles in this example, are the text contents of the links, instead of text "Full Story", so that the text content is unique and indicative of the destinations of links. 
* The @img@ elements that have the same destinations as text links have emtpy alt attributes (""). 
"""
example_info3.keyboard    = """
"""
example_info3.markup = [m1]

rr1 = rule_reference_object("LINK_2", "pass", "pass", "LINK_2_T1", "", "")
rr2 = rule_reference_object("LINK_4", "pass", "pass", "LINK_4_T3","","")
rr3 = rule_reference_object("LINK_1", "pass", "pass", "LINK_1_T2","","")
rr4 = rule_reference_object("LINK_3", "pass", "pass", "LINK_3_T1","","")

example_info3.rule_references = [rr1,rr2,rr3,rr4]

example_info3.html        = """
<div class="example"> 

<div class="inil">
  <div class="inil_pic">
    <HL1><a href="http://www.news.uiuc.edu/news/08/0701email.html"><img src="{{EXAMPLE_MEDIA}}images/white_tiffany_b.jpg" <HL1>alt=""</HL1> id="newsphoto" width="70" height="70"/></a></HL1>
  </div>
  <HL1><h3 id="newshead"><a href="http://www.news.uiuc.edu/news/08/0701email.html"><HL2>Personal Information in e-mail marketing can backfire, study indicates</HL2></a></h3></HL1>
  <p id="inil_text">Businesses rick chasing away prospective customers when they send chummy e-mails that bandy around people's names, hobbies and other personal information to pitch sales, according to a new study of the popular marketing tool.</p>
</div>  
  
<div class="inil">
  <div class="inil_pic">
    <a href="http://www.news.uiuc.edu/news/08/0715athapaskans.html"><img src="{{EXAMPLE_MEDIA}}images/geronimo_b.jpg" alt="" id="newsphoto" width="70" height="70"/></a>
  </div>
  <h3 id="newshead"><a href="http://www.news.uiuc.edu/news/08/0715athapaskans.html">Y chromosome study sheds light on Athapaskan migration to southwest U.S.</a></h3>
  <p id="inil_text">A large-scale genetic study of native North Americans offers new insights into the migration of a small group of Athapaskan natives from their subarctic home in northwest North America to the southwestern United States. The migration, which left no known archaeological trace, is believed to have occurred about 500 years ago.</p>
</div>  
  
<div class="inil">
  <div class="inil_pic">
    <a href="http://www.news.uiuc.edu/news/08/0711infants.html"><img src="{{EXAMPLE_MEDIA}}images/JKim_b.jpg" alt="" id="newsphoto" width="70" height="70"/></a>
  </div>
  <h3 id="newshead"><a href="http://www.news.uiuc.edu/news/08/0711infants.html">Non-parental care of infants tied to unfavorable feeding practices</a></h3>
  <p id="inil_text">With more new mothers in the workplace than ever before, there has been a corresponding increase in the number of child-care facilities in the United States. At the same time, data from a variety of sources point to a growing prevalence of overweight infants and toddlers. Is there a connection?</p>
</div>  
  
<div class="inil">
  <div class="inil_pic">
    <a href="http://www.news.uiuc.edu/news/08/0707hiring.html"><img src="{{EXAMPLE_MEDIA}}images/Lawler,John_w.jpg" alt="" id="newsphoto" width="70" height="70"/></a>
  </div>
  <h3 id="newshead"><a href="http://www.news.uiuc.edu/news/08/0707hiring.html">U.S. firms a role model for fair hiring standards, study says</a></h3>
  <p id="inil_text">U.S. companies are helping spread fair hiring practices across the world as they set up shop in developing nations, according to a new study of gender and age discrimination co-written by a University of Illinois labor expert.</p>
</div>  

</div>
"""

example_info3.script      = """"""

example_info3.style       = """

#example_html {
  background-color: #FFFFFF;
}

.inil {
  margin-top: .5em;
}

.inil_pic {
  float: left;
  margin-right: .7em;
}

h3#newshead {
  font-weight: bolder;
  color: #ff5555;
  font-family: Times New Roman, Times, serif;
  font-size: large;
}

h3#newshead a:link{
  font-weight: bolder;
  color: #ff5555;
  font-family: Times New Roman, Times, serif;
  font-size: large;
  text-decoration: none;
}

h3#newshead a:hover{
  font-weight: bolder;
  color: #5555dd;
  font-family: Times New Roman, Times, serif;
  font-size: large;
  text-decoration: underline;
}

h3#newshead a:visited{
  font-weight: bolder;
  color: #ff5555;
  font-family: Times New Roman, Times, serif;
  font-size: large;
  text-decoration: none;
}

h3#newshead a:active{
  font-weight: bolder;
  color: #ff5555;
  font-family: Times New Roman, Times, serif;
  font-size: large;
  text-decoration: none;
}

p#inil_text a:link {
  color: #5555dd;
}

img#newsphoto {
  padding-right: 0;
}

"""

example3 = create_example(example_info3)
ExampleGroup.objects.get(slug='links').examples.add(example3)
# =============================
# Example 4
# =============================

example_info4             = example_object()
example_info4.example_groups = [eg_links]
example_info4.title       = 'Ambigous unnaccessible @img@ element link'
example_info4.permanent_slug = ''

example_info4.description = """
* The @alt@ attributes of the @img@ elements are not indicative enough as an alternative for a link text.
* One image (ex6_bluearrow.gif) is used repeatedly for links that point to different URIs with insufficient @alt@ attribute content.
* This example is based on the homepage of University of Illinois Alumni Association of Urbana.
"""

example_info4.keyboard    = """
"""

example_info4.markup = [m1]

rr1 = rule_reference_object("LINK_1", "fail", "fail", "LINK_1_T1", "", "")
rr2 = rule_reference_object("LINK_3", "pass", "pass", "LINK_3_T1", "", "")
rr3 = rule_reference_object("LINK_4", "fail", "fail", "", "", "")
rr4 = rule_reference_object("LINK_2", "fail", "fail", "", "", "")

example_info4.rule_references = [rr1, rr2, rr3,rr4]

example_info4.html        = """
 <div class="news_item">
  <div class="news_image_left"><HL1><a href="http://www.uiaa.org/urbana/statefarm.html"><img src="{{EXAMPLE_MEDIA}}images/ex6_statefarm.jpg" alt="<HL2>State Farm Arch Rivalry Tailgate</HL2>"></a></HL1></div>
  <p>
  <span id="news_title">State Farm Arch Rivalry Tailgate</span><br>
    Join us for a humdinger of a tailgate prior to the Illinois vs. Missouri matchup! There will be great food, lots of fun activities and the camaraderie of fellow Illini fans.
  <HL1><a href="http://www.uiaa.org/urbana/statefarm.html"><img src="{{EXAMPLE_MEDIA}}images/ex6_bluearrow.gif" alt="More ..." width="16" height="13"></a></HL1>
  </p>
</div>

<div class="news_item">
  <div class="news_image_right"><a href="http://www.uofi.onlinecommunity.com/cgi-any/postcards.dll/genfill?sitename=UOFI"><img src="{{EXAMPLE_MEDIA}}images/ex6_postcards.jpg" alt="Illinois Postcards" width="180" height="86"></a></div>
  <p>
    <span id="news_title">Surprise someone with an Illinois e-postcard</span><br>
    Want to wish someone happy birthday, razz your best friend about his favorite baseball team or simply say hello to your old Illinois roommate? Use our simple-to-send e-postcards to keep in touch with companions, loved ones and acquaintances. We offer vibrant postcard images from each U of I campus, with space for your personalized message and multiple coloring options - including orange and blue! It's free, fun and a great way to stay in touch.
  <a href="http://www.uofi.onlinecommunity.com/cgi-any/postcards.dll/genfill?sitename=UOFI"><img src="{{EXAMPLE_MEDIA}}images/ex6_bluearrow.gif" alt="More ..." width="16" height="13"></a>
  </p>
</div>
  
"""

example_info4.script      = """"""

example_info4.style      = """
#example_html {
  background-color: #FFFFFF;
}

.news_item {
  margin-top: 2em;
}

.news_item img {
  border: 0;
}

.news_image_left {
  float: left;
  margin-top: -1em;
}

.news_image_left img {
  border: 0;
}

.news_image_right {
  float: right;
}

.news_image_right img {
  border: 0;
}

#news_title {
  color: #FF6600;
  font-weight: bold;
}

#news_title a:link {
  color: #FF6600;
  font-weight: bold;
  text-decoration: none;
}

#news_title a:active {
  color: #FF6600;
  font-weight: bold;
  text-decoration: none;
}

#news_title a:visited {
  color: #FF6600;
  font-weight: bold;
  text-decoration: none;
}

#news_title a:hover {
  color: #FF6600;
  font-weight: bold;
  text-decoration: underline;
}
"""

example4 = create_example(example_info4)
ExampleGroup.objects.get(slug='links').examples.add(example4)
# =============================
# Example 5
# =============================

example_info5             = example_object()
example_info5.example_groups = [eg_links]
example_info5.title       = 'Internal links that move accessible focus'
example_info5.permanent_slug = ''

example_info5.description = """
The current WCAG 2.0 Techniques for links in context requirement 2.4.4 do not provide a progammatic means to determine the authors intended context.
The following examples use the <code>aria-describedby</code> attribute to provide a means for authors to define the context to users and to support assistive technologies to identify the correct context.
This technique it supported by the JAWS screen reader for both Internet Explorer 9.0 and Firefox 4.0.
"""
example_info5.keyboard    = """
"""

example_info5.markup = [m1]

rr1 = rule_reference_object("LINK_1", "pass", "pass", "LINK_1_T1", "", "")
rr2 = rule_reference_object("LINK_3", "pass", "pass", "LINK_3_T1", "", "")
rr3 = rule_reference_object("LINK_4", "fail", "fail", "", "", "")
rr4 = rule_reference_object("LINK_2", "pass", "pass", "LINK_2_T3", "", "")

example_info5.rule_references = [rr1, rr2, rr3,rr4]

example_info5.html        = """
<p><a href="#maintopic">Go to the main topic</a></p>

<h3>Navigation Links</h3>
<ul>
    <li><a href=".">Navigation link #1</a></li>
    <li><a href=".">Navigation link #2</a></li>
    <li><a href=".">Navigation link #3</a></li>
    <li><a href=".">Navigation link #4</a></li>
    <li><a href=".">Navigation link #5</a></li>
</ul>

<h3><a id="maintopic" name="maintopic" tabindex="-1"></a>The Main Topic</h3>
<p>The text of the main topic of the web page would be here.  
    This is an <a href=",">example link</a> to show the keyboard focus is moved past the navigation bar links when the "Go to the main topic" link was selected.  
    For Internet Explorer the <code>tabindex</code> value is needed to make sure following the link actually moves keyboard focus.
</p>     
"""

example_info5.script      = """"""

example_info5.style      = """

#example_html {
  background-color: #FFFFFF;
}

#example_html h3 {
  color: #FF6600;
}

#example_html a {

}



"""

example5 = create_example(example_info5)
ExampleGroup.objects.get(slug='links').examples.add(example5)
