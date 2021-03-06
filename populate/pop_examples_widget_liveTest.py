"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples_common import *
from pop_examples_common_resources import script1
from pop_examples_common_resources import script2

# =============================
# Example 1
# =============================


example_info             = example_object()
example_info.title       = 'Live Region'
example_info.permanent_slug = 'live1'

example_info.description = """
Simple example of a live region widget with two timers.
"""
example_info.keyboard    = """
"""

example_info.aria_labelledby = True
example_info.html_label = True
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='log')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='option')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='timer')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-activedescendant')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-atomic')
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-live')
m7 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-relevant')
m8 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-selected')

example_info.markup = [m1,m2,m3,m4,m5,m6,m7,m8]

rr1 = rule_reference_object("KEYBOARD_1", "pass", "pass", "KEYBOARD_1_T1", "", "")
rr2 = rule_reference_object("KEYBOARD_2", "pass", "pass", "KEYBOARD_2_T1", "", "")
rr3 = rule_reference_object("WIDGET_1","pass", "pass", "WIDGET_1_T3","","")
rr4 = rule_reference_object("WIDGET_2","pass", "na", "WIDGET_2_T2","WIDGET_2_T3","")
rr5 = rule_reference_object("WIDGET_3","pass", "na", "WIDGET_3_T1","","")
rr6 = rule_reference_object("WIDGET_6","pass", "na", "WIDGET_6_T1","","")

example_info.rule_references = [rr1,rr2,rr3,rr4,rr5,rr6]

example_info.html        = """
<div class="controls">
<h2>RSS Feed Controls</h2>
<p><label for="rssFeedSelect">Select an RSS Feed</label>:
<select id="rssFeedSelect">
  <option id="feed1"
    value="http://en-us.fxfeeds.mozilla.com/en-US/firefox/headlines.xml" selected>Mozilla Latest Headlines
  </option>
  <option id="feed2"
    value="http://news.google.com/?output=rss">Google News
  </option>
  <option id="feed3"
    value="http://feeds.bbci.co.uk/news/rss.xml">BBC News
  </option>
  <option id="feed4"
    value="http://hosted.ap.org/lineups/TOPHEADS.rss?SITE=AP&SECTION=HOME">Associated Press News
  </option>
  <option id="feed5"
    value="http://rss.slashdot.org/Slashdot/slashdot">Slashdot
  </option>
</select></p>
<p><label for="intervalSelect">Select an Update Interval</label>:
<select id="intervalSelect">
  <option value="1">1 minute</option>
<option value="5" selected >5 minutes</option>
  <option value="10">10 minutes</option>
</select></p>
<hr />
<p><label for="rssPolitenessSelect">Politeness Level (aria-live value)</label>:
<select id="rssPolitenessSelect">
  <option 
    id="rssPolite1" value="off">off
  </option>
  <option 
    id="rssPolite2" value="polite">polite
  </option>
  <option
    id="rssPolite3" value="assertive" selected>assertive
  </option>
</select></p>
<p><label for="rssAtomicSelect">Atomic Updates</label>:
<select id="rssAtomicSelect">
  <option id="atomicSelect1"
    value="false" selected>false
  </option>
  <option id="atomicSelect2"
    value="true">true
  </option>
</select></p>
<p><label for="rssRelevantSelect">Change Relevance</label>:
<select id="rssRelevantSelect">
  <option selected
    value="additions" selected>additions
  </option>
  <option
    value="removals">removals
  </option>
  <option
    value="text">text
  </option>
  <option
    value="all">all
  </option>
</select></p>
</div>
<div class="controls">
<h2>Timer Controls</h2>
<p><label for="timerPolitenessSelect">Politeness Level (aria-live value)</label>:
<select id="timerPolitenessSelect">
  <option id="timerPolite1"
    value="off">off
  </option>
  <option id="timerPolite2"
    value="polite" selected>polite
  </option>
  <option id="timerPolite3"
    value="assertive">assertive
  </option>
</select></p>
<p><label for="timerAtomicSelect">Atomic Updates</label>:
<select id="timerAtomicSelect" role="listbox">
  <option
    id="timerAtomic1"
    value="false">false
  </option>
  <option id="timerAtomic2"
    value="true" selected>true
  </option>
</select></p>
<p><label for="timerRelevantSelect">Change Relevance</label>:
<select id="timerRelevantSelect">
  <option id="timerRelevant1"
    value="additions" selected>additions
  </option>
  <option id="timerRelevant2"
    value="removals">removals
  </option>
  <option id="timerRelevant3"
    value="text">text
  </option>
  <option
    id="timerRelevant4"
    value="all" selected>all
  </option>
</select></p>
<hr/>
  <div id="countdown">
    <label for="timer">Time until next update</label>:
    <div id="timer"></div>
  </div>
</div>

<div id="rssFeedContent">
  &nbsp;
</div> 
"""
example_info.script = """
(function($){$.extend({jGFeed:function(url,fnk,num,key){if(url==null){return false;}var gurl="http://ajax.googleapis.com/ajax/services/feed/load?v=1.0&callback=?&q="+url;if(num!=null){gurl+="&num="+num;}if(key!=null){gurl+="&key="+key;}$.getJSON(gurl,function(data){if(typeof fnk=="function"){fnk.call(this,data.responseData.feed);}else{return false;}});}});})(jQuery);

var g_seconds =  0;
var OAA_EXAMPLES = OAA_EXAMPLES ||{};

$(document).ready(function() {

  // set the globabal second countdown variable before we create the associated
  // live region
  g_seconds =  $('#intervalSelect').val() * 60 - 1;

  var timerRegion = new OAA_EXAMPLES.liveRegion('timer', 'OAA_EXAMPLES.countdown()', 1000);
  var rssRegion = new OAA_EXAMPLES.liveRegion('rssFeedContent', 'getRssFeed()', $('#intervalSelect').val() * 60000);

  // do initial rss grab
  getRssFeed();

  //////////////////// bind event handlers for rssRegion controls /////////////////////////////

  // bind a change event handler for the RSS feed select
  $('#rssFeedSelect').change(function(e) {

    if ($(this).val() != null) {
      // get the new feed
      getRssFeed();
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the interval select
  $('#intervalSelect').change(function(e) {

    if ($(this).val() != null) {
      // set the new timer interval
      rssRegion.setInterval($(this).val() * 60000);

      // update the countdown interval
      g_seconds = $(this).val() * 60 - 1;
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the politeness select
  $('#rssPolitenessSelect').change(function(e) {

    if ($(this).val() != null) {
      // set the politeness level
      rssRegion.setPoliteness($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic updates select
  $('#rssAtomicSelect').change(function(e) {

    if ($(this).val() != null) {
      // set the atomic update setting
      rssRegion.setAtomic($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#rssRelevantSelect').change(function(e) {

    if ($(this).val() != null) {
      // set the update relevance setting
      rssRegion.setRelevant($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  //////////////////// bind event handlers for timer controls /////////////////////////////

  // bind a change event handler for the politeness select
  $('#timerPolitenessSelect').change(function(e) {

    if ($(this).val() != null) {
      // set the politeness level
      timerRegion.setPoliteness($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic updates select
  $('#timerAtomicSelect').change(function(e) {

    if ($(this).val() != null) {
      // set the atomic update setting
      timerRegion.setAtomic($(this).val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#timerRelevantSelect').change(function(e) {

    if ($(this).val() != null) {
      // set the update relevance setting
      timerRegion.setRelevant($(this).val());
    }

    e.stopPropagation();
    return false;
  });
}); // end ready


/**
* @method countdown
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback to update the countdown live region. This callback is passed to rssRegion.
*
* @return {N/A}
*/

OAA_EXAMPLES.countdown = function() {
  var minutes = Math.floor(g_seconds / 60);
  var seconds = g_seconds % 60;

  if (seconds < 10) {
    seconds = '0' + seconds;
  }

  if (g_seconds == 0) {
    // do nothing - countdown will be reset by the
    // rssRegion interval timer
    $('#timer').text('updating');
  }
  else {
  $('#timer').text(minutes + ':' + seconds);
    g_seconds--;
  }
}

/**
* @method getRssFeed
*
* @memberOf OAA_EXAMPLES
*
* @desc a callback to obtain the top 5 items from an RSS feed. the function checks
* the entries obtained against those that may have been obtained previously (present in the live region).
* It will remove old entries and prepend newer ones it has received. This callback is passed to rssRegion.
*
* @return {N/A}
*/

function getRssFeed(){

  var $id = $('#rssFeedContent');
  var $topEntry = $id.find('.entry').first();

  $.jGFeed($('#rssFeedSelect').val(), function(feed) {
    if(!feed) {
      alert('there was an error');
    }

    // Check to see if this is a new article
    if ($topEntry) {
      var topTitle = $topEntry.find('.storyLink').text();
      var topNdx;

      // iterate through the feed entries and find the index
      // of the matching story.
      for(topNdx = 0; topNdx < feed.entries.length; topNdx++) {
        if (topTitle == feed.entries[topNdx].title) {
          break;
        }
      }

      if (topNdx == feed.entries.length) {
        // there was no match. Clear the region and
        // append all articles
        $id.empty();
      }
      else {
        // there was a match. Remove as many articles
        // as there are new ones from the feed.
        for (var ndx = 0; ndx < topNdx; ndx++) {
          // remove the last entry
          $id.find('.entry').last().remove();
        }
      }
    }

    for (var i = topNdx - 1; i >= 0; i--) {

      var entry = feed.entries[i];
      var title = entry.title;
      var link = entry.link;
      var description = entry.contentSnippet;
      var pubDate = entry.publishedDate;

      var html = '<div class="entry"><h4 class="postTitle">'
               + '<a class="storyLink" href="' + link + '" target="_blank" tabindex="0">'
        + title + '</a>';
      html += '<br><em class="date">' + pubDate + '</em></h4><div class="summary">';
      html += '<p class="description">' + description + '</p></div></div>';
        
      $id.prepend(html);
    }
  }, 5);

  // reset cowntdown
  g_seconds = $('#intervalSelect').val() * 60 - 1;

} // end getRssFeed() 

///////////////////////////////// liveRegion  Widget Definition /////////////////////////////////////

/**
* @method liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc a constructor to define an ARIA live region widget. The widget binds to a div
* on the page and accepts a callback function that is triggered at a specified interval.
*
* By default, the live region's alert level is polite, it's updates are non-atomic, additions are relevant,
* and it uses the general channel. These default values may be overridden by either specifying different
* values in the html markup or by calling the widget's corresponding update functions.
*
* @param {string} id - the html id of the div to bind to.
*
* @param (func callback) func is the callback function to execute at the specified interval
*
* @param (interval integer) interval is the initial update interval
*
* @return N/A
*/

/**
* @constructor liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc Define the object properties
*
* @property {object} $id - the jquery object of the live region
*
* @property {object} func - the callback to execute after each interval
*
* @property {integer} interval - the interval to use for the timer
*
* @property {object} timer - the interval timer object
*/

OAA_EXAMPLES.liveRegion = function(id, func, interval) {

  // define widget properties

  this.$id = $('#' + id);

  this.func = func;
  this.interval = interval;
  this.timer = null;

  // set the initial live region aria attributes. Check if the user
  // has specified values in the html markup. If so, use those
  // values.

  var tmp = this.$id.attr('aria-live');

  if (tmp) {
    this.politeness = tmp;
  }
  else {
    this.politeness = 'polite';
  }

  tmp = this.$id.attr('aria-atomic');
  if (tmp) {
    this.atomic = tmp;
  }
  else {
    this.atomic = 'false';
  }

  tmp = this.$id.attr('aria-relevant');
  if (tmp) {
    this.relevant = tmp;
  }
  else {
    this.relevant = 'additions';
  }

  this.busy = false; // set to true while the region is updating

  // create the update timer
  this.createTimer();

} // end liveRegion constructor

/**
* @method createTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to create an interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.createTimer = function() {

  if (this.timer != null) {
    // destroy the existing timer
    this.destroyTimer();
  }

  this.timer = setInterval(this.func, this.interval);

} // end createTimer()

/**
* @method destroyTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to remove the interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.destroyTimer = function() {

  if (this.timer != null) {
    clearInterval(this.timer);    
    this.timer = null;
  }

} // end createTimer()

/**
* @method setInterval
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to change the update interval
* of the live region. This function stores the new interval, clears the current
* interval timer and creates new one with the specified interval.
*
* @param {integer} interval - the new interval, in minutes, to set
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setInterval = function(interval) {
  this.interval = interval;

  this.createTimer();

} // end setInterval()

/**
* @method setPoliteness
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-polite attribute of
* the live region.
*
* @param {string} val - one of three possible states: 'off', 'polite', 'assertive';
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setPoliteness = function(val) {

  this.$id.attr('aria-live', val);
} // end setPoliteness()

/**
* @method setAtomic
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-atomic attribute of
* the live region.
*
* @param {boolean} val - true if live region updates should be atomic
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setAtomic = function(val) {

  this.$id.attr('aria-atomic', val);

} // end setAtomic()

/**
* @method setRelevant
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-relevant attribute of
* the live region.
*
* @param {string} val - may be 'additions', 'removals', or 'text'. It may also be a
* space seperated combination of these.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setRelevant = function(val) {

  this.$id.attr('aria-relevant', val);

} // end setRelevant()


"""
example_info.style       = """
div#application {
  height: 30em;
}
div.controls {
  margin-left: 10px;
  padding: 5px 10px;
  width: 21em;
  float: left;
  clear: both;
  border-bottom: 1px solid #008;
}
button,
select {
  float: right;
}
h2 {
  clear: both;
}
div.example {
  margin-top: 50px;
  margin-left: 30px;
  width: 22em;
  float: left;
}
div#region1Container {
  margin-left: 4em;
  padding: 10px;
  width: 11em;
  height: 1.6em;
  float: left;
}
div#region1Container label {
  padding-top: 10px;
  font-weight: bold;
}
div#liveregion1 {
  margin: 0;
  padding: 2px 5px;
  float: right;
  width: 2em;
  text-align: right;
  border: 1px solid black;
}
label#region2Label {
  font-weight: bold;
  font-size: 1.2em;
}
div#liveregion2 {
  padding: 2px 5px;
  width: 22em;
  border: 1px solid black;
  height: 9em;
  overflow: auto;
}
"""

example1 = create_example(example_info)

ref = add_script_reference( example1, script1 )

CodingPattern.objects.get(slug='rss').examples.add(example1)

# =============================
# Example 2
# =============================


example_info             = example_object()
example_info.title       = 'Live Region 2'
example_info.permanent_slug = 'live2'

example_info.description = """
Simple example of a live region widget with two timers.
"""
example_info.keyboard    = """
"""

example_info.aria_labelledby = True
example_info.html_label = True
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='log')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='option')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='timer')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-activedescendant')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-atomic')
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-live')
m7 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-relevant')
m8 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-selected')

example_info.markup = [m1,m2,m3,m4,m5,m6,m7,m8]

rr1 = rule_reference_object("KEYBOARD_1", "pass", "pass", "KEYBOARD_1_T1", "", "")
rr2 = rule_reference_object("KEYBOARD_2", "pass", "pass", "KEYBOARD_2_T1", "", "")
rr3 = rule_reference_object("WIDGET_1","pass", "pass", "WIDGET_1_T3","","")
rr4 = rule_reference_object("WIDGET_2","pass", "na", "WIDGET_2_T2","WIDGET_2_T3","")
rr5 = rule_reference_object("WIDGET_3","pass", "na", "WIDGET_3_T1","","")
rr6 = rule_reference_object("WIDGET_6","pass", "na", "WIDGET_6_T1","","")

example_info.rule_references = [rr1,rr2,rr3,rr4,rr5,rr6]

example_info.html        = """
<div class="controls">
   <h2>Live Region 1: Simple Counter</h2>
   <p><label for="time1">Change Interval (seconds)</label>:
      <select id="time1">
         <option id="time1_opt1" selected>1</option>
         <option id="time1_opt2">2</option>
         <option id="time1_opt3">3</option>
         <option id="time1_opt4">4</option>
         <option id="time1_opt5">5</option>
         <option id="time1_opt6">6</option>
         <option id="time1_opt7">7</option>
         <option id="time1_opt8">8</option>
         <option id="time1_opt9">9</option>
         <option id="time1_opt10">10</option>
      </select>
   </p>

   <p><label for="politeness1">Live Property Value</label>:
      <select id="politeness1" >
         <option id="polite1_opt1">off</option>
         <option id="polite1_opt2">polite</option>
         <option id="polite1_opt3" selected>assertive</option>
         <option id="polite1_opt4">rude</option>
      </select>
   </p>

   <p><label for="atomic1">Atomic Property Value</label>:
         <select id="atomic1">
            <option id="atomic1_opt1" selected>true</option>
            <option id="atomic1_opt2">false</option>
          </select>
   </p>

   <p><label for="relevant1">Relevant Property Value</label>:
         <select id="relevant1" >
            <option id="relevant1_opt1">additions</option>
            <option id="relevant1_opt2">removals</option>
            <option id="relevant1_opt3">text</option>
            <option id="relevant1_opt4" selected>all</option>
          </select>
   </p>
</div>
<div class="example">
   <div id="region1Container">
      <label for="liveregion1">Changing value</label>:
      <div id="liveregion1">XXX
      </div>
   </div>
</div>
<div class="controls">
   <h2>Live Region 2: Text Log</h2>
   <p><label for="time2">Change Interval (in seconds)</label>:
      <select id="time2">
         <option id="time2_opt1">1</option>
         <option id="time2_opt2">2</option>
         <option id="time2_opt3">3</option>
         <option id="time2_opt4">4</option>
         <option id="time2_opt5" selected>5</option>
         <option id="time2_opt6">6</option>
         <option id="time2_opt7">7</option>
         <option id="time2_opt8">8</option>
         <option id="time2_opt9">9</option>
         <option id="time2_opt10">10</option>
      </select>
   </p>

   <p><label for="politeness2">Live Property Value</label>:
      <select id="politeness2">
         <option id="polite2_opt1">off</option>
         <option id="polite2_opt2"selected>polite</option>
         <option id="polite2_opt3">assertive</option>
         <option id="polite2_opt4">rude</option>
      </select>
   </p>

   <p><label id="atomic2Label" for="atomic2">Atomic Property Value</label>:
         <select id="atomic2" aria-labelledby="atomic2Label" aria-activedescendant="atomic2_opt2">
            <option id="atomic2_opt1" role="option" aria-selected="false">true</option>
            <option id="atomic2_opt2" role="option" aria-selected="true" selected>false</option>
          </select>
   </p>

   <p><label id="relevant2Label" for="relevant2">Relevant Property Value</label>:
         <select id="relevant2" aria-labelledby="relevant2Label" aria-activedescendant="relevant2_opt1">
            <option id="relevant2_opt1" role="option" aria-selected="true" selected>additions</option>
            <option id="relevant2_opt2" role="option" aria-selected="false">removals</option>
            <option id="relevant2_opt3" role="option" aria-selected="false">text</option>
            <option id="relevant2_opt4" role="option" aria-selected="false">all</option>
          </select>
   </p>
</div>

<div class="example">
   <label for="liveregion2">Log Text</label>

   <div id="liveregion2">
   </div>
</div> 
"""

example_info.script = """
var OAA_EXAMPLES = OAA_EXAMPLES ||{};
/**
* @method liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc a constructor to define an ARIA live region widget. The widget binds to a div
* on the page and accepts a callback function that is triggered at a specified interval.
*
* By default, the live region's alert level is polite, it's updates are non-atomic, additions are relevant,
* and it uses the general channel. These default values may be overridden by either specifying different
* values in the html markup or by calling the widget's corresponding update functions.
*
* @param {string} id - the html id of the div to bind to.
*
* @param (func callback) func is the callback function to execute at the specified interval
*
* @param (interval integer) interval is the initial update interval
*
* @return N/A
*/

/**
* @constructor liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc Define the object properties
*
* @property {object} $id - the jquery object of the live region
*
* @property {object} func - the callback to execute after each interval
*
* @property {integer} interval - the interval to use for the timer
*
* @property {object} timer - the interval timer object
*/
OAA_EXAMPLES.liveRegion = function(id, func, interval) {

  // define widget properties

  this.$id = $('#' + id); 

  this.func = func; 
  this.interval = interval;
  this.timer = null;

  // set the initial live region aria attributes. Check if the user
  // has specified values in the html markup. If so, use those
  // values.

  var tmp = this.$id.attr('aria-live');

  if (tmp) {
    this.politeness = tmp;
  }
  else {
    this.politeness = 'polite';
  }

  tmp = this.$id.attr('aria-atomic');
  if (tmp) {
    this.atomic = tmp;
  }
  else {
    this.atomic = 'false';
  }

  tmp = this.$id.attr('aria-relevant');
  if (tmp) {
    this.relevant = tmp;
  }
  else {
    this.relevant = 'additions';
  }

  this.busy = false; // set to true while the region is updating

  // create the update timer
  this.createTimer();

} // end liveRegion constructor

/**
* @method createTimer
*
* @memberOf OAA_EXAMPLES
* 
* @desc a member function to create an interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.createTimer = function() {

  if (this.timer != null) {
    // destroy the existing timer
    this.destroyTimer();
  }

  this.timer = setInterval(this.func, this.interval);

} // end createTimer()

/**
* @method destroyTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to remove the interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.destroyTimer = function() {

  if (this.timer != null) {
    clearInterval(this.timer);    
    this.timer = null;
  }

} // end createTimer()

/**
* Function setInterval() is a member function to change the update interval
* of the live region. This function stores the new interval, clears the current
* interval timer and creates new one with the specified interval.
*
* @param (interval integer) interval is the new interval, in minutes, to set
*
* @return N/A
*/

OAA_EXAMPLES.liveRegion.prototype.setInterval = function(interval) {
  this.interval = interval;

  this.createTimer();

} // end setInterval()

/**
* @method setPoliteness
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-polite attribute of
* the live region.
*
* @param {string} val - one of three possible states: 'off', 'polite', 'assertive';
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setPoliteness = function(val) {

  this.$id.attr('aria-live', val);
} // end setPoliteness()

/**
* @method setAtomic
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-atomic attribute of
* the live region.
*
* @param {boolean} val - true if live region updates should be atomic
*
* @return N/A
*/

OAA_EXAMPLES.liveRegion.prototype.setAtomic = function(val) {

  this.$id.attr('aria-atomic', val);

} // end setAtomic()

/**
* @method setRelevant
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-relevant attribute of
* the live region.
*
* @param {string} val may be 'additions', 'removals', or 'text'. It may also be a
* space seperated combination of these.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setRelevant = function(val) {

  this.$id.attr('aria-relevant', val);

} // end setRelevant() 


var g_msg1 = {
  msgArray: new Array("0","1","2","3","4","5","6","7","8","9"),  
  index: 0
};

var g_msg2 = {
  msgArray: new Array(
    "The birch canoe slid on the smooth planks.",
    "Glue the sheet to the dark blue background.",
    "It's easy to tell the depth of a well.",
    "These days a chicken leg is a rare dish.",
    "Rice is often served in round bowls.",
    "The juice of lemons makes fine punch.",
    "The box was thrown beside the parked truck.",
    "The hogs were fed chopped corn and garbage.",
    "Four hours of steady work faced us.",
    "Large size in stockings is hard to sell."
  ),  
  index: 0
};

var g_msg1index = 0;
var g_msg2index = 0;

$(document).ready(function() {
  var live1 = new OAA_EXAMPLES.liveRegion('liveregion1', function() {OAA_EXAMPLES.updateRegion('liveregion1', g_msg1, false);}, 1000);
  var live2 = new OAA_EXAMPLES.liveRegion('liveregion2', function() {OAA_EXAMPLES.updateRegion('liveregion2', g_msg2, true);}, 5000);

  //Bind event handlers for live1 controls

  // bind a change event handler for the interval select
  $('#time1').change(function(e) {

    
    // set the interval
    live1.setInterval($(this).val()*1000);

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the politeness select
  $('#politeness1').change(function(e) {

    // set the politeness
    live1.setPoliteness($(this).val());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic select
  $('#atomic1').change(function(e) {

    // set the politeness
    live1.setAtomic($(this).val());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#relevant1').change(function(e) {

    // set the update revelance setting
    live1.setRelevant($(this).val());

    e.stopPropagation();
    return false;
  });

  //Bind event handlers for live2 controls
  
  $('#time2').change(function(e) {

    // set the interval
    live2.setInterval($(this).val()*1000);

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the politeness select
  $('#politeness2').change(function(e) {

    // set the politeness
    live2.setPoliteness($(this).val());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic select
  $('#atomic2').change(function(e) {

    // set the politeness
    live2.setAtomic($(this).val());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#relevant2').change(function(e) {

    // set the update revelance setting
    live2.setRelevant($(this).val());

    e.stopPropagation();
    return false;
  });

}); // end ready()

/**
* @method updateRegion()
*
* @memberOf OAA_EXAMPLES
*
* @desc called by a liveRegion timer to updates the live region
* with new content based on the passed messageArray.
*
* @param {object} LiveRegion - the liveRegion widget object
*
* @param {array} msgArray - an array of messages to use for the update
*
* @param {boolean} append - true if messages should be appended, false if message should
* replace live region content
*
* @return {N/A}
*/

OAA_EXAMPLES.updateRegion = function(region, msgObj, append) {

  var $regionID = $('#' + region);
  var msg = '';
  
  if (msgObj.index == msgObj.msgArray.length) {
    // We've reached the end of the array, reset the index.
    msgObj.index = 0;

    // clear the region
    $regionID.empty();
  }

  if (append == false) {

    msg = msgObj.msgArray[msgObj.index];

    // messages should replace live region contents.
    // Empty the live region
    $regionID.empty();
  }
  else {
    msg = msgObj.msgArray[msgObj.index] + '<br/>';
  }

  // append the new message to the live region
  $regionID.append(msg);

  if (append == true) {
    $regionID.scrollTop($regionID.attr('scrollHeight'));
  }

  // increment the message index
  msgObj.index++;
 
} 

"""
example_info.style       = """
div#application {
  height: 30em;
}
div.controls {
  margin-left: 10px;
  padding: 5px 10px;
  width: 21em;
  float: left;
  clear: both;
  border-bottom: 1px solid #008;
}
button,
select {
  float: right;
}
h2 {
  clear: both;
}
div.example {
  margin-top: 50px;
  margin-left: 30px;
  width: 22em;
  float: left;
}
div#region1Container {
  margin-left: 4em;
  padding: 10px;
  width: 11em;
  height: 1.6em;
  float: left;
}
div#region1Container label {
  padding-top: 10px;
  font-weight: bold;
}
div#liveregion1 {
  margin: 0;
  padding: 2px 5px;
  float: right;
  width: 2em;
  text-align: right;
  border: 1px solid black;
}
label#region2Label {
  font-weight: bold;
  font-size: 1.2em;
}
div#liveregion2 {
  padding: 2px 5px;
  width: 22em;
  border: 1px solid black;
  height: 9em;
  overflow: auto;
}
"""

example2 = create_example(example_info)

ref = add_script_reference( example2, script1 )

CodingPattern.objects.get(slug='rss').examples.add(example2)



# =============================
# Example 3
# =============================


example_info             = example_object()
example_info.title       = 'Live Region 3'
example_info.permanent_slug = 'live3'

example_info.description = """
Simple example of a live region widget with two timers.
"""
example_info.keyboard    = """
"""

example_info.aria_labelledby = True
example_info.html_label = True
spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')

m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='log')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='option')
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute='role', value='timer')
m4 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-activedescendant')
m5 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-atomic')
m6 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-live')
m7 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-relevant')
m8 = ElementDefinition.objects.get(spec=spec_aria10, attribute='aria-selected')

example_info.markup = [m1,m2,m3,m4,m5,m6,m7,m8]

rr1 = rule_reference_object("KEYBOARD_1", "pass", "pass", "KEYBOARD_1_T1", "", "")
rr2 = rule_reference_object("KEYBOARD_2", "pass", "pass", "KEYBOARD_2_T1", "", "")
rr3 = rule_reference_object("WIDGET_1","pass", "pass", "WIDGET_1_T3","","")
rr4 = rule_reference_object("WIDGET_2","pass", "na", "WIDGET_2_T2","WIDGET_2_T3","")
rr5 = rule_reference_object("WIDGET_3","pass", "na", "WIDGET_3_T1","","")
rr6 = rule_reference_object("WIDGET_6","pass", "na", "WIDGET_6_T1","","")

example_info.rule_references = [rr1,rr2,rr3,rr4,rr5,rr6]

example_info.html        = """
<script type="text/javascript" src="http://localhost/coding/examples/js/jquery-1.4.2.min.js"></script>
  <div class="controls">  
    <h2>Set Text Live Region ARIA Properties</h2>
    <p>
    <label for="interval">Seconds before a change</label>:
    <select id="interval">
      <option>1</option>
      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
      <option>6</option>
      <option>7</option>
      <option>8</option>
      <option>9</option>
      <option selected>10</option>
      <option>11</option>
      <option>12</option>
      <option>13</option>
      <option>14</option>
      <option>15</option>
    </select>
    </p>
    <p>
    <label for="textPoliteness">Politeness Level</label>:
    <select id="textPoliteness">
       <option>off</option>
       <option>polite</option>
       <option selected>assertive</option>
       <option>rude</option>
    </select>
    </p>
    <p>
    <label for="textAtomic">Atomic</label>:
    <select id="textAtomic">
      <option id="textAtomic1">true</option>
      <option id="textAtomic2" selected>false</option>
    </select>
    </p>
    <p>
    <label for="replaceText">Replace or Append Text?</label>:
    <select id="replaceText">
      <option>Append</option>
      <option>Replace</option>
    </select>
    </p>
  </div>
  
  <div class="controls">  
    <h2>Set Message Live Region ARIA Properties</h2>
    <p>
    <label for="msgPoliteness">Politeness Level</label>:
    <select id="msgPoliteness">
      <option>off</option>
      <option>polite</option>
      <option selected>assertive</option>
      <option>rude</option>
    </select>
    </p>
  </div>

  <div class="example">
    <h2>Live region example: Reader</h2>

    <p>Description: Click the button below to start reading your messages.  Each sentence will appear for the time set above.  Every so often another message will replace the previous one.</p>

    <p><button id="startButton">Begin reading</button> </p>

    <h3>Message</h3>
    <div id="liveMsg" class="message"></div>

    <h3>Text</h3>
    <div id="liveText" class="text"></div>
    <div id="loadedText" class="hidden">
</div>
  </div> 
"""
example_info.script = """
var OAA_EXAMPLES = OAA_EXAMPLES ||{};

var $i = 0 //Global variable pointing to which text line to put in the Live Region

/**
* @method liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc a constructor to define an ARIA live region widget. The widget binds to a div
* on the page and accepts a callback function that is triggered at a specified interval.
*
* By default, the live region's alert level is polite, it's updates are non-atomic, additions are relevant,
* and it uses the general channel. These default values may be overridden by either specifying different
* values in the html markup or by calling the widget's corresponding update functions.
*
* @param {string} id - the html id of the div to bind to.
*
* @param (func callback) func is the callback function to execute at the specified interval
*
* @param (interval integer) interval is the initial update interval
*
* @return N/A
*/

/**
* @constructor liveRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc Define the object properties
*
* @property {object} $id - the jquery object of the live region
*
* @property {object} func - the callback to execute after each interval
*
* @property {integer} interval - the interval to use for the timer
*
* @property {object} timer - the interval timer object
*/

OAA_EXAMPLES.liveRegion = function(id, func, interval) {

  // define widget properties

  this.$id = $('#' + id); 

  this.func = func;
  this.interval = interval;
  this.timer = null;

  // set the initial live region aria attributes. Check if the user
  // has specified values in the html markup. If so, use those
  // values.

  var tmp = this.$id.attr('aria-live');

  if (tmp) {
    this.politeness = tmp;
  }
  else {
    this.politeness = 'polite';
  }

  tmp = this.$id.attr('aria-atomic');
  if (tmp) {
    this.atomic = tmp;
  }
  else {
    this.atomic = 'false';
  }

  tmp = this.$id.attr('aria-relevant');
  if (tmp) {
    this.relevant = tmp;
  }
  else {
    this.relevant = 'additions';
  }

  this.busy = false; // set to true while the region is updating

  // create the update timer
  this.createTimer();

} // end liveRegion constructor

/**
* @method createTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to create an interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.createTimer = function() {

  if (this.timer != null) {
    // destroy the existing timer
    this.destroyTimer();
  }

  this.timer = setInterval(this.func, this.interval);

} // end createTimer()

/**
* @method destroyTimer
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to remove the interval timer for
* the live region widget.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.destroyTimer = function() {

  if (this.timer != null) {
    clearInterval(this.timer);    
    this.timer = null;
  }

} // end destroyTimer()

/**
* @method setInterval
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to change the update interval
* of the live region. This function stores the new interval, clears the current
* interval timer and creates new one with the specified interval.
*
* @param {integer} interval - the new interval, in minutes, to set
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setInterval = function(interval) {
  this.interval = interval;

  this.createTimer();

} // end setInterval()

/**
* @method setPoliteness
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-polite attribute of the live region.
*
* @param {string} val - one of three possible states: 'off', 'polite', 'assertive';
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setPoliteness = function(val) {

  this.$id.attr('aria-live', val);
} // end setPoliteness()

/**
* @method setAtomic
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-atomic attribute of
* the live region.
*
* @param {boolean} val - true if live region updates should be atomic
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setAtomic = function(val) {

  this.$id.attr('aria-atomic', val);

} // end setAtomic()

/**
* @method setRelevant
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to set the aria-relevant attribute of the live region.
*
* @param {string} val - may be 'additions', 'removals', or 'text'. It may also be a
* space seperated combination of these.
*
* @return {N/A}
*/

OAA_EXAMPLES.liveRegion.prototype.setRelevant = function(val) {

  this.$id.attr('aria-relevant', val);

} // end setRelevant()


var $g_text = new Array(); // the jQuery objects of the text loaded from the file
var $g_curLine = null; // the jQuery object of the current line in g_text
var g_append = ''; // set to either 'Append' or 'Replace'
var g_msgLive = null; // the message live region
var g_textLive = null; // the text live region

var g_messages = {
    msgArray: new Array("...","you have new mail.", "there are new news feeds."),
    index: 0
};

$.ajaxSetup({async: 'false'});


$(document).ready(function() {

$g_text[0] = "Moby Dick";
$g_text[1] = "Call me Ishmael.  Some years ago--never mind how long";
$g_text[2] = "precisely--having little or no money in my purse, and nothing";
$g_text[3] = "particular to interest me on shore, I thought I would sail about a";
$g_text[4] = "little and see the watery part of the world.  It is a way I have of";
$g_text[5] = "driving off the spleen and regulating the circulation.  Whenever I";
$g_text[6] = "find myself growing grim about the mouth; whenever it is a damp,";
$g_text[7] = "drizzly November in my soul; whenever I find myself involuntarily";
$g_text[8] = "pausing before coffin warehouses, and bringing up the rear of every";
$g_text[9] = "funeral I meet; and especially whenever my hypos get such an upper";
$g_text[10] = "hand of me, that it requires a strong moral principle to prevent me";
$g_text[11] = "from deliberately stepping into the street, and methodically knocking";

OAA_EXAMPLES.init();


  

}); // end ready()

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc performs initial processing for the app
*
* @return {N/A}
*/

OAA_EXAMPLES.init = function() {
  var interval = $('#interval').val() * 1000;

  g_msgLive = new OAA_EXAMPLES.liveRegion('liveMsg', 'OAA_EXAMPLES.updateMsgRegion()', 7000);
  g_textLive = new OAA_EXAMPLES.liveRegion('liveMsg', 'OAA_EXAMPLES.updateTextRegion()', interval);
  // set g_append based on the select value
  g_append = $('#replaceText').val();
  alert(g_append);


} // end init()


/**
* @method updateMsgRegion
*
* @memberOf OAA_EXAMPLES
* with new messages
*
* @return {N/A}
*/

OAA_EXAMPLES.updateMsgRegion = function() {

  var $regionID = $('#liveMsg');
  var msg = g_messages.msgArray[g_messages.index];
  
  g_messages.index++;
  if (g_messages.index == g_messages.msgArray.length) {
    g_messages.index = 0;
  }

  $regionID.empty();
  $regionID.append(msg);
} // end updateMsgRegion()

/**
* @method updateTextRegion
*
* @memberOf OAA_EXAMPLES
*
* @desc called by a liveRegion timer to update the text live region
* with new content from the $g_text array
*
* @return {N/A}
*/

OAA_EXAMPLES.updateTextRegion = function() {
  var $regionID = $('#liveText');
  var msg = '';
  var $g_curline = $i;
  g_append = $('#replaceText').val();
  interval = $('#interval').val() * 1000;
  alert(interval);

  tempInterval = interval;
  
  if ($g_curLine == $g_text.length - 1) {
    // last line - start from the beginning
    $g_curLine = $g_text[0];

    // empty the region
    $regionID.empty();
  }
  else {
    // get the next line from the text array
    $g_curLine = $g_curLine +1;
  }

  if (g_append == 'Replace') {

    // messages should replace live region contents.
    // Empty the live region
    $regionID.empty();

    msg = $g_text[$i] + ' ';

  if ($i == $g_text.length-1) {
      $i = 0; $regionID.empty();
  }
  else {
    $i = $i+1;
   }

  }
  else {
    $regionID.find('.new').removeClass('new');
    msg = '<span class="new">' + $g_text[$i] + ' </span><br/>';
  }

  // append the new message to the live region
  $regionID.append(msg);

  if (g_append == 'Append') {
    $regionID.scrollTop($regionID.attr('scrollHeight'));

  if ($i == $g_text.length-1){
    $i = 0; $regionID.empty();
  }
  else {$i = $i+1;}
}

} // end updateTextRegion() 

"""
example_info.style       = """
div.controls {
  margin-left: 30px;
  padding: 5px 10px;
  width: 28em;
}
label {
  margin-left: 20px;
}
select {
  float: right;
  display: inline;
  margin-right: 13em;
}

div.example {
  margin: 20px;
  padding: 10px;
  width: 50em;
  border: 1px solid black;
}
div.message {
  padding: 2px 5px;
  height: 1.2em;
  border: thin solid black;
  background-color: #CCCCCC;
}
div.text {
  padding: 2px 5px;
  height: 8em;
  border: thin solid black;
  overflow: auto;
}

div#loadedText {
  display: none;
}
span.title {
  font-weight: bold;
  font-size: 1.3em;
  margin-left: 6em;
  margin-bottom: .5em;
  display: block;
}
span.new {
  color: #922;
} 
"""

example3 = create_example(example_info)

ref = add_script_reference( example3, script2 )

CodingPattern.objects.get(slug='rss').examples.add(example3)



