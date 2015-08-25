"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples_common import *



# =============================
# Example 1
# =============================

order = 1
eg_carousel = ExampleGroup.objects.get(slug="carousels")

example_info                = example_object()
example_info.order          = order
example_info.example_groups = [eg_carousel]
example_info.title          = 'Carousel of Automatically Rotating Images'
example_info.permanent_slug = 'carousel1'

example_info.description = """ 
Many organizational home pages often like to use a set of rotating images to provide an
overview of the organizations activities or information on recent news. 
"""
example_info.keyboard    = """
* Focus on menu stops image rotation
* Focus on slider allows user to use cursor keys to manually move through the slides
"""

example_info.aria_labelledby = True

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')


m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute="role", value='navigation')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute="aria-label")
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute="role", value='slider')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute="aria-valuemin")
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute="aria-valuenow")
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute="aria-valuemax")

example_info.markup = [m1,m2,m3,m4,m5,m6]

rr1 = rule_reference_object("KEYBOARD_1", "pass", "pass", "KEYBOARD_1_T1", "", "")

example_info.rule_references = [rr1]

example_info.html        = """


<div role="navigation" aria-label="Links in the slide show" style="position: absolute; left: -300em; top: -30em;">
  <ul>
    <li><a href="javascript:alert('Image Link 1')">Dummy link 1"</a></li>
    <li><a href="javascript:alert('Image Link 2')">Dummy link 2"</a></li>
    <li><a href="javascript:alert('Image Link 3')">Dummy link 3"</a></li>
    <li><a href="javascript:alert('Image Link 4')">Dummy link 4"</a></li>
    <li><a href="javascript:alert('Image Link 5')">Dummy link 5"</a></li>
    <li><a href="javascript:alert('Image Link 6')">Dummy link 6"</a></li>
  <ul>
</div>

<div id="id_slideshow" 
     role="region" 
     aria-label="Rotating slide show"
     class="cycle-slideshow" 
     data-cycle-slides="a" 
     data-cycle-caption="#id-caption"
     data-cycle-caption-template="Slide {{slideNum}}: {{cycleTitle}}"
     data-cycle-pause-on-hover="true" 
     >
  <a href="javascript:alert('Image Link 1')" data-cycle-title="A"><img src="{{EXAMPLE_MEDIA}}images/world1.jpg" alt="Dummy link 1"/></a>
  <a href="javascript:alert('Image Link 2')" data-cycle-title="B"><img src="{{EXAMPLE_MEDIA}}images/world2.jpg" alt="Dummy link 2"/></a>
  <a href="javascript:alert('Image Link 3')" data-cycle-title="C"><img src="{{EXAMPLE_MEDIA}}images/world3.jpg" alt="Dummy link 3"/></a>
  <a href="javascript:alert('Image Link 4')" data-cycle-title="D"><img src="{{EXAMPLE_MEDIA}}images/lab.jpg" alt="Dummy link 4"/></a>
  <a href="javascript:alert('Image Link 5')" data-cycle-title="E"><img src="{{EXAMPLE_MEDIA}}images/keyboard.jpg" alt="Dummy link 5"/></a>
  <a href="javascript:alert('Image Link 6')" data-cycle-title="F"><img src="{{EXAMPLE_MEDIA}}images/disk.jpg" alt="Dummy link 6"/></a>
  <div id="id-caption">-----</div>
</div>

<input id="id_slider" type="range" min="1" max="6" value="1" aria-label="slide show option" aria-controls="id_slideshow"/>

<div>Slide: <span id="id_slide"></span></div>
<div>Paused: <span id="id_paused"></span></div>
<div>Last Event: <span id="id_event"></span></div>

"""

																							
example_info.script      = """

$(document).ready(function() {

  var $slideshow = $('#id_slideshow');
  var $slideshow_links = $('#id_slideshow a');
  var $slider = $('#id_slider');

  var $event_info = $('#id_event');
  var $slide_info = $('#id_slide');
  var $paused_info = $('#id_paused');

  var $paused = false;
  
  $slideshow_links.focusin(function() {
    $paused = true;
    $slideshow.cycle('pause');
    $event_info.text('focus in');
    $paused_info.text('True');
  });  
    
  $slideshow_links.focusout(function() {
    $paused = false;
    $slideshow.cycle('resume');
    $event_info.text('focus out');
    $paused_info.text('False');
  });  

  $slideshow.on('cycle-after', function(event, opts) {
    if (!opts.paused && !$paused) {
      $slider.val(opts.slideNum);
      $slider.attr('max',  opts.slideCount.toString());
      $slide_info.text("Auto cycling: " + opts.slideNum + " out of " + opts.slideCount);

      $paused_info.text('False');
    }  

  });  
      
  $slider.focusin(function() {
    $paused = true;
    $slideshow.cycle('pause');

    $event_info.text('focus in');
    $paused_info.text('True');
  });  
    
  $slider.focusout(function() {
    $paused = false;
    $slideshow.cycle('resume');

    $event_info.text('focus out');
    $paused_info.text('False');
  });  
      
  $slider.change(function() {
    $slideshow.cycle('goto', $slider.val()-1);
    $event_info.text('changed event');
    $slide_info.text('Go to slide: ' + $slider.val());
  });  

  $slider.keyup(function() {
    $slideshow.cycle('goto', $slider.val());
    $event_info.text('keyup event');
    $slide_info.text('Go to slide: ' + $slider.val());
  });  
  
});

"""

example_info.style       = """"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script2      = ExampleScript.objects.get(script='examples/js/jquery-2.0.2.min.js')
script_cycle = ExampleScript.objects.get(script='examples/js/jquery.cycle2.all.js')
add_script_reference( example1, script2 )
add_script_reference( example1, script_cycle )

