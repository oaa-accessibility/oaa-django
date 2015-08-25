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
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>

<h2>RSS Feed Controls</h2>
<p><label id="rssFeedSelectLabel" for="rssFeedSelect">Select an RSS Feed</label>:
<select id="rssFeedSelect" role="listbox" aria-labelledby="rssFeedSelectLabel" aria-activedescendant="rssFeed1" tabindex="0">
  <option
    id="rssFeed1"
    role="option"
    aria-selected="true"
    value="http://en-us.fxfeeds.mozilla.com/en-US/firefox/headlines.xml" selected>Mozilla Latest Headlines
  </option>
  <option
    id="rssFeed2"
    role="option"
    aria-selected="false"
    value="http://news.google.com/?output=rss">Google News
  </option>
  <option
    id="rssFeed3"
    role="option"
    aria-selected="false"
    value="http://feeds.bbci.co.uk/news/rss.xml">BBC News
  </option>
  <option
    id="rssFeed4"
    role="option"
    aria-selected="false"
    value="http://hosted.ap.org/lineups/TOPHEADS.rss?SITE=AP&SECTION=HOME">Associated Press News
  </option>
  <option
    id="rssFeed5"
    role="option"
    aria-selected="false"
    value="http://rss.slashdot.org/Slashdot/slashdot">Slashdot
  </option>
</select></p>
<p><label id="intervalSelectLabel" for="intervalSelect">Select an Update Interval</label>:
<select id="intervalSelect" role="listbox" aria-labelledby="intervalSelectLabel" aria-activedescendant="interval2" tabindex="0">
  <option
    id="interval1"
    role="option"
    aria-selected="false"
    value="1">1 minute
  </option>
  <option
    id="interval2"
    role="option"
    aria-selected="true"
    value="5" selected>5 minutes
  </option>
  <option
    id="interval3"
    role="option"
    aria-selected="false"
    value="10">10 minutes
  </option>
</select></p>
<hr />
<p><label id="rssPolitenessSelectLabel" for="rssPolitenessSelect">Politeness Level (aria-live value)</label>:
<select id="rssPolitenessSelect" role="listbox" aria-labelledby="rssPolitenessSelectLabel" aria-activedescendant="rssPolite3" tabindex="0">
  <option
    id="rssPolite1"
    role="option"
    aria-selected="false"
    value="off">off
  </option>
  <option
    id="rssPolite2"
    role="option"
    aria-selected="false"
    value="polite">polite
  </option>
  <option
    id="rssPolite3"
    role="option"
    aria-selected="true"
    value="assertive" selected>assertive
  </option>
</select></p>
<p><label id="rssAtomicSelectLabel" for="rssAtomicSelect">Atomic Updates</label>:
<select id="rssAtomicSelect" role="listbox" aria-labelledby="rssAtomicSelectLabel" aria-activedescendant="rssAtomic1" tabindex="0">
  <option
    id="rssAtomic1"
    role="option"
    aria-selected="true"
    value="false" selected>false
  </option>
  <option
    id="rssAtomic2"
    role="option"
    aria-selected="false"
    value="true">true
  </option>
</select></p>
<p><label id="rssRelevantSelectLabel" for="rssRelevantSelect">Change Relevance</label>:
<select id="rssRelevantSelect" role="listbox" aria-labelledby="rssRelevantSelectLabel" aria-activedescendant="rssRelevant1" tabindex="0">
  <option
    id="rssRelevant1"
    role="option"
    aria-selected="true"
    value="additions" selected>additions
  </option>
  <option
    id="rssRelevant2"
    role="option"
    aria-selected="false"
    value="removals">removals
  </option>
  <option
    id="rssRelevant3"
    role="option"
    aria-selected="false"
    value="text">text
  </option>
  <option
    id="rssRelevant4"
    role="option"
    aria-selected="false"
    value="all">all
  </option>
</select></p>
</div>
<div class="controls">
<h2>Timer Controls</h2>
<p><label id="timerPolitenessSelectLabel" for="timerPolitenessSelect">Politeness Level (aria-live value)</label>:
<select id="timerPolitenessSelect" role="listbox" aria-labelledby="timerPolitenessSelectLabel" aria-activedescendant="timerPolite2" tabindex="0">
  <option
    id="timerPolite1"
    role="option"
    aria-selected="false"
    value="off">off
  </option>
  <option
    id="timerPolite2"
    role="option"
    aria-selected="true"
    value="polite" selected>polite
  </option>
  <option
    id="timerPolite3"
    role="option"
    aria-selected="false"
    value="assertive">assertive
  </option>
</select></p>
<p><label id="timerAtomicSelectLabel" for="timerAtomicSelect">Atomic Updates</label>:
<select id="timerAtomicSelect" role="listbox" aria-labelledby="timerAtomicSelectLabel" aria-activedescendant="timerAtomic2" tabindex="0">
  <option
    id="timerAtomic1"
    role="option"
    aria-selected="false"
    value="false">false
  </option>
  <option
    id="timerAtomic2"
    role="option"
    aria-selected="true"
    value="true" selected>true
  </option>
</select></p>
<p><label id="timerRelevantSelectLabel" for="timerRelevantSelect">Change Relevance</label>:
<select id="timerRelevantSelect" role="listbox" aria-labelledby="timerRelevantSelectLabel" aria-activedescendant="timerRelevant4" tabindex="0">
  <option
    id="timerRelevant1"
    role="option"
    aria-selected="false"
    value="additions">additions
  </option>
  <option
    id="timerRelevant2"
    role="option"
    aria-selected="false"
    value="removals">removals
  </option>
  <option
    id="timerRelevant3"
    role="option"
    aria-selected="false"
    value="text">text
  </option>
  <option
    id="timerRelevant4"
    role="option"
    aria-selected="true"
    value="all" selected>all
  </option>
</select></p>
<hr />
  <div id="countdown">
    <label id="timerlabel" for="timer">Time until next update</label>:
    <div id="timer" role="timer" aria-labelledby="timerLabel" aria-live="polite" aria-atomic="true" aria-relevant="all"></div>
  </div>
</div>

<div id="rssFeedContent" role="log" aria-live="assertive" aria-atomic="false" aria-relevant="additions">
  &nbsp;
</div> 

"""
example_info.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

/**
* @constructor liveRegion
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
* @param {string} id is the html id of the div to bind to.
*
* @param {callback} func - the callback function to execute at the specified interval
*
* @param {integer} interval - the initial update interval
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @memberOf OAA_EXAMPLES
*
* @property {object} $id - the jquery object of the live region
*
* @property {callback} func - the callback to execute after each interval
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
* @desc member function to create an interval timer for the live region widget.
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
* @desc a member function to remove the interval timer for the live region widget.
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
* @desc  member function to set the aria-atomic attribute of the live region.
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


$(document).ready(function() {

  // call init() to reset the select elements - in case of page reload
  OAA_EXAMPLES.init();

  // set the globabal second countdown variable before we create the associated
  // live region
  g_seconds =  $('#intervalSelect').val() * 60 - 1;

  var timerRegion = new OAA_EXAMPLES.liveRegion('timer', 'countdown()', 1000);
  var rssRegion = new OAA_EXAMPLES.liveRegion('rssFeedContent', 'getRssFeed()', $('#intervalSelect').val() * 60000);

  // do initial rss grab
  OAA_EXAMPLES.getRssFeed();

  //////////////////// bind event handlers for rssRegion controls /////////////////////////////

  // bind a change event handler for the RSS feed select
  $('#rssFeedSelect').change(function(e) {

    var $newItem = null;

    // select the new item
    $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    if ($newItem != null) {
      // get the new feed
      OAA_EXAMPLES.getRssFeed();
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the interval select
  $('#intervalSelect').change(function(e) {

    var $newItem = null;

    // select the new item
    $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    if ($newItem != null) {
      // set the new timer interval
      rssRegion.setInterval($newItem.val() * 60000);

      // update the countdown interval
      g_seconds = $newItem.val() * 60 - 1;
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the politeness select
  $('#rssPolitenessSelect').change(function(e) {

    var $newItem = null;

    // select the new item
    $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    if ($newItem != null) {
      // set the politeness level
      rssRegion.setPoliteness($newItem.val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic updates select
  $('#rssAtomicSelect').change(function(e) {

    var $newItem = null;

    // select the new item
    $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    if ($newItem != null) {
      // set the atomic update setting
      rssRegion.setAtomic($newItem.val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#rssRelevantSelect').change(function(e) {

    var $newItem = null;

    // select the new item
    $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    if ($newItem != null) {
      // set the update relevance setting
      rssRegion.setRelevant($newItem.val());
    }

    e.stopPropagation();
    return false;
  });

  //////////////////// bind event handlers for timer controls /////////////////////////////

  // bind a change event handler for the politeness select
  $('#timerPolitenessSelect').change(function(e) {

    var $newItem = null;

    // select the new item
    $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    if ($newItem != null) {
      // set the politeness level
      timerRegion.setPoliteness($newItem.val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic updates select
  $('#timerAtomicSelect').change(function(e) {

    var $newItem = null;

    // select the new item
    $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    if ($newItem != null) {
      // set the atomic update setting
      timerRegion.setAtomic($newItem.val());
    }

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#timerRelevantSelect').change(function(e) {

    var $newItem = null;

    // select the new item
    $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    if ($newItem != null) {
      // set the update relevance setting
      timerRegion.setRelevant($newItem.val());
    }

    e.stopPropagation();
    return false;
  });
}); // end ready

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a function to initialize the select elements to match their activedescendant values. This
* ensures that any page reloads do not introduce erroneous aria attribute values
*/

OAA_EXAMPLES.init = function() {

  var elems = new Array('rssFeedSelect', 'intervalSelect', 'rssPolitenessSelect', 'rssAtomicSelect',
      'rssRelevantSelect', 'timerPolitenessSelect', 'timerAtomicSelect', 'timerRelevantSelect');
  var $id = null;
  var val = null;

  for (ndx in elems) {
    // get the jQuery object of select to set
    $id = $('#' + elems[ndx]);

    // get the value of the active descendant
    val = $('#' + $id.attr('aria-activedescendant')).val();

    // set the value of the select
    $id.val(val);
  }

} // end init()

/**
* @method selectItem
*
* @memberOf OAA_EXAMPLES
*
* @desc a function to iterate through an option list to find a new option and select it.
* The function also updates the aria-seleced attribute of the items.
*
* @param {object} $select - the jquery object of the select that the option list is part of.
*
* @param {object} $list - the list of options to iterate through.
*
* @param {string} val - the value to find in the list.
*
* @return {object} returns the jquery object of the new item selected. Returns NULL if not found.
*/

OAA_EXAMPLES.selectItem = function($select, $list, val) {
  var $prevItem = $('#' + $select.attr('aria-activedescendant'));
  var $newItem = null;
    
  // find the list item associated with the new value
  $list.each(function() {
    if ($(this).val() == val) {
             $newItem = $(this);
    }
  });

  if ($newItem == null) {
    // no new item found
    return null;
  }

  // set the aria-selected attribute to false for the previously selected item
  $prevItem.attr('aria-selected', 'false')

  // set the aria-selected attribute to true for the new item
  $newItem.attr('aria-selected', 'true')

  // update the active descendent of the select
  $select.attr('aria-activedescendant', $newItem.attr('id'));

  // return the new item selected
  return $newItem;

} // end selectItem()

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
* Note: This function uses the jquery.jGFeed plugin in order to get around the same-domain security
* barrier for AJAX.
*
* @return {N/A}
*/

OAA_EXAMPLES.getRssFeed = function() {

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

(function($){$.extend({jGFeed:function(url,fnk,num,key){if(url==null){return false;}var gurl="http://ajax.googleapis.com/ajax/services/feed/load?v=1.0&callback=?&q="+url;if(num!=null){gurl+="&num="+num;}if(key!=null){gurl+="&key="+key;}$.getJSON(gurl,function(data){if(typeof fnk=="function"){fnk.call(this,data.responseData.feed);}else{return false;}});}});})(jQuery);


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
example_info.title       = 'Live Region2'
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
   <p><label id="time1Label" for="time1">Change Interval (seconds)</label>:
      <select id="time1" aria-labelledby="time1Label" aria-activedescendant="time1_opt1">
         <option id="time1_opt1" role="option" aria-selected="true" selected>1</option>
         <option id="time1_opt2" role="option" aria-selected="false">2</option>
         <option id="time1_opt3" role="option" aria-selected="false">3</option>
         <option id="time1_opt4" role="option" aria-selected="false">4</option>
         <option id="time1_opt5" role="option" aria-selected="false">5</option>
         <option id="time1_opt6" role="option" aria-selected="false">6</option>
         <option id="time1_opt7" role="option" aria-selected="false">7</option>
         <option id="time1_opt8" role="option" aria-selected="false">8</option>
         <option id="time1_opt9" role="option" aria-selected="false">9</option>
         <option id="time1_opt10" role="option" aria-selected="false">10</option>
      </select>
   </p>

   <p><label id="politeness1Label" for="politeness1">Live Property Value</label>:
      <select id="politeness1" aria-labelledby="politeness1Label" aria-activedescendant="polite1_opt3">
         <option id="polite1_opt1" role="option" aria-selected="false">off</option>
         <option id="polite1_opt2" role="option" aria-selected="false">polite</option>
         <option id="polite1_opt3" role="option" aria-selected="true" selected>assertive</option>
         <option id="polite1_opt4" role="option" aria-selected="false">rude</option>
      </select>
   </p>

   <p><label id="atomic1Label" for="atomic1">Atomic Property Value</label>:
         <select id="atomic1" aria-labelledby="atomic1Label" aria-activedescendant="atomic1_opt1">
            <option id="atomic1_opt1" role="option" aria-selected="true" selected>true</option>
            <option id="atomic1_opt2" role="option" aria-selected="false">false</option>
          </select>
   </p>

   <p><label id="relevant1Label" for="relevant1">Relevant Property Value</label>:
         <select id="relevant1" aria-labelledby="relevant1Label" aria-activedescendant="relevant1_opt4">
            <option id="relevant1_opt1" role="option" aria-selected="false">additions</option>
            <option id="relevant1_opt2" role="option" aria-selected="false">removals</option>
            <option id="relevant1_opt3" role="option" aria-selected="false">text</option>
            <option id="relevant1_opt4" role="option" aria-selected="true" selected>all</option>
          </select>
   </p>
</div>
<div class="example">
   <div id="region1Container">
      <label id="live1Label" for="liveregion1">Changing value</label>:
      <div id="liveregion1"
         class="region"  
         role="timer"
   aria-labelledby="live1Label"
         aria-live="assertive"
         aria-atomic="true"
         aria-relevant="all">XXX
      </div>
   </div>
</div>
<div class="controls">
   <h2>Live Region 2: Text Log</h2>
   <p><label id="time2Label" for="time2">Change Interval (in seconds)</label>:
      <select id="time2" aria-labelledby-"time2Label" aria-activedescendant="time2_opt5">
         <option id="time2_opt1" role="option" aria-selected="false">1</option>
         <option id="time2_opt2" role="option" aria-selected="false">2</option>
         <option id="time2_opt3" role="option" aria-selected="false">3</option>
         <option id="time2_opt4" role="option" aria-selected="false">4</option>
         <option id="time2_opt5" role="option" aria-selected="true" selected>5</option>
         <option id="time2_opt6" role="option" aria-selected="false">6</option>
         <option id="time2_opt7" role="option" aria-selected="false">7</option>
         <option id="time2_opt8" role="option" aria-selected="false">8</option>
         <option id="time2_opt9" role="option" aria-selected="false">9</option>
         <option id="time2_opt10" role="option" aria-selected="false">10</option>
      </select>
   </p>

   <p><label id="politeness2Label" for="politeness2">Live Property Value</label>:
      <select id="politeness2" aria-labelledby="politeness2Label" aria-activedescendant="polite2_opt2">
         <option id="polite2_opt1" role="option" aria-selected="false">off</option>
         <option id="polite2_opt2" role="option" aria-selected="true" selected>polite</option>
         <option id="polite2_opt3" role="option" aria-selected="false">assertive</option>
         <option id="polite2_opt4" role="option" aria-selected="false">rude</option>
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
   <label id="region2Label" for="liveregion2">Log Text</label>

   <div id="liveregion2"
      class="region"
      role="log"
      aria-labelledby="region2Label"
      aria-live="polite"
      aria-atomic="true"
      aria-relevant="additions">
   </div>
</div> 
"""
example_info.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

/**
* @constructor liveRegion
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
* @param {callback} func - the callback function to execute at the specified interval
*
* @param {integer} interval - the initial update interval
*
* @return {N/A}
*/

/**
* @constructor Internal Properties
*
* @memberOf OAA_EXAMPLES
*
* @property {object} $id - the jquery object of the live region
*
* @property {callback} func - the callback to execute after each interval
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
* @desc a member function to create an interval timer for the live region widget.
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
* @desc a member function to remove the interval timer for the live region widget.
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
* @desc  member function to set the aria-atomic attribute of the live region.
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

  var live1 = new OAA_EXAMPLES.liveRegion('liveregion1', function() {updateRegion('liveregion1', g_msg1, false);}, 1000);
  var live2 = new OAA_EXAMPLES.liveRegion('liveregion2', function() {updateRegion('liveregion2', g_msg2, true);}, 5000);

  // initialize the selects to ensure that their selected values match the markup
  OAA_EXAMPLES.init();

  ///////////////// Bind event handlers for live1 controls //////////////////////////

  // bind a change event handler for the interval select
  $('#time1').change(function(e) {

    // select the new item
    var $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    // set the interval
    live1.setInterval($newItem.text()*1000);

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the politeness select
  $('#politeness1').change(function(e) {

    // select the new item
    var $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    // set the politeness
    live1.setPoliteness($newItem.text());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic select
  $('#atomic1').change(function(e) {

    // select the new item
    var $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    // set the politeness
    live1.setAtomic($newItem.text());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#relevant1').change(function(e) {

    // select the new item
    var $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    // set the update revelance setting
    live1.setRelevant($newItem.text());

    e.stopPropagation();
    return false;
  });

  ///////////////// Bind event handlers for live2 controls //////////////////////////
  
  $('#time2').change(function(e) {

    // select the new item
    var $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    // set the interval
    live2.setInterval($newItem.text()*1000);

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the politeness select
  $('#politeness2').change(function(e) {

    // select the new item
    var $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    // set the politeness
    live2.setPoliteness($newItem.text());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the atomic select
  $('#atomic2').change(function(e) {

    // select the new item
    var $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    // set the politeness
    live2.setAtomic($newItem.text());

    e.stopPropagation();
    return false;
  });

  // bind a change event handler for the update relevance select
  $('#relevant2').change(function(e) {

    // select the new item
    var $newItem = selectItem($(this), $(this).find('option'), $(this).val());

    // set the update revelance setting
    live2.setRelevant($newItem.text());

    e.stopPropagation();
    return false;
  });

}); // end ready()

/**
* @method init
*
* @memberOf OAA_EXAMPLES
*
* @desc a function to initialize the select elements to match their activedescendant values. This
* ensures that any page reloads do not introduce erroneous aria attribute values
*/

OAA_EXAMPLES.init = function() {

  var elems = new Array('time1', 'politeness1', 'atomic1', 'relevant1', 'time2', 'politeness2', 'atomic2', 'relevant2');
  var $id = null;
  var val = null;

  for (ndx in elems) {
    // get the jQuery object of select to set
    $id = $('#' + elems[ndx]);

    // get the value of the active descendant
    val = $('#' + $id.attr('aria-activedescendant')).text();

    // set the value of the select
    $id.val(val);
  }

} // end init()

/**
* @method selectItem
*
* @memberOf OAA_EXAMPLES
*
* @desc a function to iterate through an option list to find a new option and select it.
* The function also updates the aria-seleced attribute of the items.
*
* @param {object} $select - the jquery object of the select that the option list is part of.
*
* @param {object} $list - the list of options to iterate through.
*
* @param {string} val - the value to find in the list.
*
* @return {object} returns the jquery object of the new item selected. Returns NULL if not found.
*/

OAA_EXAMPLES.selectItem = function($select, $list, val) {
  var $prevItem = $('#' + $select.attr('aria-activedescendant'));
  var $newItem = null;
    
  // find the list item associated with the new value
  $list.each(function() {
    if ($(this).text() == val) {
             $newItem = $(this);
    }
  });

  if ($newItem == null) {
    // no new item found
    return null;
  }

  // set the aria-selected attribute to false for the previously selected item
  $prevItem.attr('aria-selected', 'false');

  // set the aria-selected attribute to true for the new item
  $newItem.attr('aria-selected', 'true')

  // update the active descendent of the select
  $select.attr('aria-activedescendant', $newItem.attr('id'));

  // return the new item selected
  return $newItem;

} // end selectItem()

/**
* @method updateRegion
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

(function($){$.extend({jGFeed:function(url,fnk,num,key){if(url==null){return false;}var gurl="http://ajax.googleapis.com/ajax/services/feed/load?v=1.0&callback=?&q="+url;if(num!=null){gurl+="&num="+num;}if(key!=null){gurl+="&key="+key;}$.getJSON(gurl,function(data){if(typeof fnk=="function"){fnk.call(this,data.responseData.feed);}else{return false;}});}});})(jQuery);

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
<script type="text/javascript">
</script>

<h2>Set Message ARIA Live Region Properties</h2>

  <ul class="controls">
    <li>
      <label for="throttle">Minimum number of seconds before a change</label>
      <select id="throttle"  onblur="setMinimumTime('throttle');" onchange="setMinimumTime('throttle');">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
      <option selected="selected">10</option>
      </select>
  </li>
  
  <li>  
      <label for="politenessLevel">Politeness Level</label>
      <select id="politenessLevel" onblur="updateAttribute('aria-live', 'politenessLevel', lrID);" onchange="updateAttribute('aria-live','politenessLevel', lrID);">
          <option>off</option>
          <option>polite</option>
          <option selected="selected">assertive</option>
          <option>rude</option>
      </select>
  </li>  

    <li>
      <label for="channelControl">Channel</label>
      <select id="channelControl" onblur="updateAttribute('aria-channel', 'channelControl', lrID);" onchange="updateAttribute('aria-channel', 'channelControl', lrID);">
          <option>general</option>
          <option>notify</option>
      </select>
  </li>  

    <li>    
      <label for="atomControl">Atomic</label>
      <select id="atomControl" onblur="updateAttribute('aria-atomic', 'atomControl', lrID);" onchange="updateAttribute('aria-atomic', 'atomControl', lrID);">
          <option>true</option>
          <option>false</option>
      </select>
  </li>
  </ul>    
    
<h2>Message</h2>

<p>This region is designed to be an interrupt message.  It has single line messages that appear at regular intervals.  You can change the intervals, politeness, channel, and atomic attributes above to help you learn about these properties.</p>

<div class="message"><span id="messages" aria-live="assertive" aria-relevant="all" aria-channel="general"></span></div>


<div id="text">

<h2>CHAPTER 1 of Moby Dick by Herman Melville</h2>

<h3>Loomings.</h3>
<p>Call me Ishmael.  Some years ago--never mind how long
precisely--having little or no money in my purse, and nothing
particular to interest me on shore, I thought I would sail about a
little and see the watery part of the world.  It is a way I have of
driving off the spleen and regulating the circulation.  Whenever I
find myself growing grim about the mouth; whenever it is a damp,
drizzly November in my soul; whenever I find myself involuntarily
pausing before coffin warehouses, and bringing up the rear of every
funeral I meet; and especially whenever my hypos get such an upper
hand of me, that it requires a strong moral principle to prevent me
from deliberately stepping into the street, and methodically knocking
people's hats off--then, I account it high time to get to sea as soon
as I can.  This is my substitute for pistol and ball.  With a
philosophical flourish Cato throws himself upon his sword; I quietly
take to the ship.  There is nothing surprising in this.  If they but
knew it, almost all men in their degree, some time or other, cherish
very nearly the same feelings towards the ocean with me.</p>

<p>There now is your insular city of the Manhattoes, belted round by
wharves as Indian isles by coral reefs--commerce surrounds it with
her surf.  Right and left, the streets take you waterward.  Its
extreme downtown is the battery, where that noble mole is washed by
waves, and cooled by breezes, which a few hours previous were out of
sight of land.  Look at the crowds of water-gazers there.</p>

<p>Circumambulate the city of a dreamy Sabbath afternoon.  Go from
Corlears Hook to Coenties Slip, and from thence, by Whitehall,
northward.  What do you see?--Posted like silent sentinels all around
the town, stand thousands upon thousands of mortal men fixed in ocean
reveries.  Some leaning against the spiles; some seated upon the
pier-heads; some looking over the bulwarks of ships from China; some
high aloft in the rigging, as if striving to get a still better
seaward peep.  But these are all landsmen; of week days pent up in
lath and plaster--tied to counters, nailed to benches, clinched to
desks.  How then is this?  Are the green fields gone?  What do they
here?</p>

<p>But look! here come more crowds, pacing straight for the water, and
seemingly bound for a dive.  Strange!  Nothing will content them but
the extremest limit of the land; loitering under the shady lee of
yonder warehouses will not suffice.  No.  They must get just as nigh
the water as they possibly can without falling in.  And there they
stand--miles of them--leagues.  Inlanders all, they come from lanes
and alleys, streets and avenues--north, east, south, and west.  Yet
here they all unite.  Tell me, does the magnetic virtue of the
needles of the compasses of all those ships attract them thither?</p>

<p>Once more.  Say you are in the country; in some high land of lakes.
Take almost any path you please, and ten to one it carries you down
in a dale, and leaves you there by a pool in the stream.  There is
magic in it.  Let the most absent-minded of men be plunged in his
deepest reveries--stand that man on his legs, set his feet a-going,
and he will infallibly lead you to water, if water there be in all
that region.  Should you ever be athirst in the great American
desert, try this experiment, if your caravan happen to be supplied
with a metaphysical professor.  Yes, as every one knows, meditation
and water are wedded for ever.</p>

<p>But here is an artist.  He desires to paint you the dreamiest,
shadiest, quietest, most enchanting bit of romantic landscape in all
the valley of the Saco.  What is the chief element he employs?  There
stand his trees, each with a hollow trunk, as if a hermit and a
crucifix were within; and here sleeps his meadow, and there sleep his
cattle; and up from yonder cottage goes a sleepy smoke.  Deep into
distant woodlands winds a mazy way, reaching to overlapping spurs of
mountains bathed in their hill-side blue.  But though the picture
lies thus tranced, and though this pine-tree shakes down its sighs
like leaves upon this shepherd's head, yet all were vain, unless the
shepherd's eye were fixed upon the magic stream before him.  Go visit
the Prairies in June, when for scores on scores of miles you wade
knee-deep among Tiger-lilies--what is the one charm
wanting?--Water--there is not a drop of water there!  Were Niagara
but a cataract of sand, would you travel your thousand miles to see
it?  Why did the poor poet of Tennessee, upon suddenly receiving two
handfuls of silver, deliberate whether to buy him a coat, which he
sadly needed, or invest his money in a pedestrian trip to Rockaway
Beach?  Why is almost every robust healthy boy with a robust healthy
soul in him, at some time or other crazy to go to sea?  Why upon your
first voyage as a passenger, did you yourself feel such a mystical
vibration, when first told that you and your ship were now out of
sight of land?  Why did the old Persians hold the sea holy?  Why did
the Greeks give it a separate deity, and own brother of Jove?  Surely
all this is not without meaning.  And still deeper the meaning of
that story of Narcissus, who because he could not grasp the
tormenting, mild image he saw in the fountain, plunged into it and
was drowned.  But that same image, we ourselves see in all rivers and
oceans.  It is the image of the ungraspable phantom of life; and this
is the key to it all.</p>

<p>Now, when I say that I am in the habit of going to sea whenever I
begin to grow hazy about the eyes, and begin to be over conscious of
my lungs, I do not mean to have it inferred that I ever go to sea as
a passenger.  For to go as a passenger you must needs have a purse,
and a purse is but a rag unless you have something in it.  Besides,
passengers get sea-sick--grow quarrelsome--don't sleep of nights--do
not enjoy themselves much, as a general thing;--no, I never go as a
passenger; nor, though I am something of a salt, do I ever go to sea
as a Commodore, or a Captain, or a Cook.  I abandon the glory and
distinction of such offices to those who like them.  For my part, I
abominate all honourable respectable toils, trials, and tribulations
of every kind whatsoever.  It is quite as much as I can do to take
care of myself, without taking care of ships, barques, brigs,
schooners, and what not.  And as for going as cook,--though I confess
there is considerable glory in that, a cook being a sort of officer
on ship-board--yet, somehow, I never fancied broiling fowls;--though
once broiled, judiciously buttered, and judgmatically salted and
peppered, there is no one who will speak more respectfully, not to
say reverentially, of a broiled fowl than I will.  It is out of the
idolatrous dotings of the old Egyptians upon broiled ibis and roasted
river horse, that you see the mummies of those creatures in their
huge bake-houses the pyramids.</p>

<p>No, when I go to sea, I go as a simple sailor, right before the mast,
plumb down into the forecastle, aloft there to the royal mast-head.
True, they rather order me about some, and make me jump from spar to
spar, like a grasshopper in a May meadow.  And at first, this sort of
thing is unpleasant enough.  It touches one's sense of honour,
particularly if you come of an old established family in the land,
the Van Rensselaers, or Randolphs, or Hardicanutes.  And more than
all, if just previous to putting your hand into the tar-pot, you have
been lording it as a country schoolmaster, making the tallest boys
stand in awe of you.  The transition is a keen one, I assure you,
from a schoolmaster to a sailor, and requires a strong decoction of
Seneca and the Stoics to enable you to grin and bear it.  But even
this wears off in time.</p>

<p>What of it, if some old hunks of a sea-captain orders me to get a
broom and sweep down the decks?  What does that indignity amount to,
weighed, I mean, in the scales of the New Testament?  Do you think
the archangel Gabriel thinks anything the less of me, because I
promptly and respectfully obey that old hunks in that particular
instance?  Who ain't a slave?  Tell me that.  Well, then, however the
old sea-captains may order me about--however they may thump and punch
me about, I have the satisfaction of knowing that it is all right;
that everybody else is one way or other served in much the same
way--either in a physical or metaphysical point of view, that is; and
so the universal thump is passed round, and all hands should rub each
other's shoulder-blades, and be content.</p>

<p>Again, I always go to sea as a sailor, because they make a point of
paying me for my trouble, whereas they never pay passengers a single
penny that I ever heard of.  On the contrary, passengers themselves
must pay.  And there is all the difference in the world between
paying and being paid.  The act of paying is perhaps the most
uncomfortable infliction that the two orchard thieves entailed upon
us.  But BEING PAID,--what will compare with it?  The urbane activity
with which a man receives money is really marvellous, considering
that we so earnestly believe money to be the root of all earthly
ills, and that on no account can a monied man enter heaven.  Ah! how
cheerfully we consign ourselves to perdition!</p>

<p>Finally, I always go to sea as a sailor, because of the wholesome
exercise and pure air of the fore-castle deck.  For as in this world,
head winds are far more prevalent than winds from astern (that is, if
you never violate the Pythagorean maxim), so for the most part the
Commodore on the quarter-deck gets his atmosphere at second hand from
the sailors on the forecastle.  He thinks he breathes it first; but
not so.  In much the same way do the commonalty lead their leaders in
many other things, at the same time that the leaders little suspect
it.  But wherefore it was that after having repeatedly smelt the sea
as a merchant sailor, I should now take it into my head to go on a
whaling voyage; this the invisible police officer of the Fates, who
has the constant surveillance of me, and secretly dogs me, and
influences me in some unaccountable way--he can better answer than
any one else.  And, doubtless, my going on this whaling voyage,
formed part of the grand programme of Providence that was drawn up a
long time ago.  It came in as a sort of brief interlude and solo
between more extensive performances.  I take it that this part of the
bill must have run something like this:</p>


<p>"GRAND CONTESTED ELECTION FOR THE PRESIDENCY OF THE UNITED STATES.
"WHALING VOYAGE BY ONE ISHMAEL.
"BLOODY BATTLE IN AFFGHANISTAN."</p>


<p>Though I cannot tell why it was exactly that those stage managers,
the Fates, put me down for this shabby part of a whaling voyage, when
others were set down for magnificent parts in high tragedies, and
short and easy parts in genteel comedies, and jolly parts in
farces--though I cannot tell why this was exactly; yet, now that I
recall all the circumstances, I think I can see a little into the
springs and motives which being cunningly presented to me under
various disguises, induced me to set about performing the part I did,
besides cajoling me into the delusion that it was a choice resulting
from my own unbiased freewill and discriminating judgment.</p>

<p>Chief among these motives was the overwhelming idea of the great
whale himself.  Such a portentous and mysterious monster roused all
my curiosity.  Then the wild and distant seas where he rolled his
island bulk; the undeliverable, nameless perils of the whale; these,
with all the attending marvels of a thousand Patagonian sights and
sounds, helped to sway me to my wish.  With other men, perhaps, such
things would not have been inducements; but as for me, I am tormented
with an everlasting itch for things remote.  I love to sail forbidden
seas, and land on barbarous coasts.  Not ignoring what is good, I am
quick to perceive a horror, and could still be social with it--would
they let me--since it is but well to be on friendly terms with all
the inmates of the place one lodges in.</p>

<p>By reason of these things, then, the whaling voyage was welcome; the
great flood-gates of the wonder-world swung open, and in the wild
conceits that swayed me to my purpose, two and two there floated into
my inmost soul, endless processions of the whale, and, mid most of
them all, one grand hooded phantom, like a snow hill in the air.</p>

"""
example_info.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

/**
*
* The Globale Variables
*/
 var live3 = new Live3();
  widgets.add( live3 );
if (!window.Node) {
  var Node = {            // If there is no Node object, define one
    ELEMENT_NODE: 1,    // with the following properties and values.
    ATTRIBUTE_NODE: 2,  // Note that these are HTML node types only.
    TEXT_NODE: 3,       // For XML-specific nodes, you need to add
    COMMENT_NODE: 8,    // other constants here.
    DOCUMENT_NODE: 9,
    DOCUMENT_FRAGMENT_NODE: 11
  }
}


var KEY_PAGEUP   = 33;
var KEY_PAGEDOWN = 34;
var KEY_END      = 35;
var KEY_HOME     = 36;

var KEY_LEFT     = 37;
var KEY_UP       = 38;
var KEY_RIGHT    = 39;
var KEY_DOWN     = 40;

var KEY_SPACE    = 32;
var KEY_TAB      = 9;

var KEY_BACKSPACE = 8;
var KEY_DELETE    = 46;
var KEY_ENTER     = 13;
var KEY_INSERT    = 45;
var KEY_ESCAPE    = 27;

var KEY_F1        = 112;
var KEY_F2        = 113;
var KEY_F3        = 114;
var KEY_F4        = 115;
var KEY_F5        = 116;
var KEY_F6        = 117;
var KEY_F7        = 118;
var KEY_F8        = 119;
var KEY_F9        = 120;
var KEY_F10       = 121;

var KEY_M         = 77;

var NS_XHTML = "http://www.w3.org/1999/xhtml"
var NS_STATE = "http://www.w3.org/2005/07/aaa";

// **********************************************
// *
// * Commonly used helper functions
// *
// **********************************************

/**
* @contructor nextSiblingElement
*/

OAA_EXAMPLES.nextSiblingElement = function(node) {

  var next_node = node.nextSibling;

  while( next_node
    && (next_node.nodeType != Node.ELEMENT_NODE) ) {
    next_node = next_node.nextSibling;
  }  // endwhile

  return next_node;
  
}

/**
*
* @method previousSiblingElement
*
* @param {node} node - object for which you are looking for the next sibling element node
*
* @return {node} next sibling or "null"
*/

OAA_EXAMPLES.previousSiblingElement = function( node ) {

  var next_node = node.previousSibling;

  while( next_node
    && (next_node.nodeType != Node.ELEMENT_NODE) ) {
    next_node = next_node.previousSibling;
  }  // endwhile

  return next_node;
  
}

/**
*
* @method firstChildElement
*
* @param {node} node object for which you are looking for the first child element node
*
* @return {node} next sibling or "null"
*/

OAA_EXAMPLES.firstChildElement = function( node ) {

  var next_node = node.firstChild;

  while( next_node
    && (next_node.nodeType != Node.ELEMENT_NODE) ) {
    next_node = next_node.nextSibling;
  }  // endwhile


  return next_node;
  
}

/**
* @contructor getTextContentOfNode
*/

OAA_EXAMPLES.getTextContentOfNode = function( node ) {

  var next_node = node.firstChild;
  var str = "";

  while( next_node ) {
    
    if( (next_node.nodeType == Node.TEXT_NODE ) &&
      (next_node.length > 0 )
     )
      str += next_node.data;
    
    
    next_node = next_node.nextSibling;
    
  }  // endwhile

  return str;
  
}

/**
*
* setTextContentOfNode
*
* @contructor
*/

OAA_EXAMPLES.setTextContentOfNode = function( node, text ) {

   // Generate a new text node with the text value
    var text_node = document.createTextNode(text);
  
    // Remove child nodes to remove text
    while (node.firstChild) {
      node.removeChild(node.firstChild);
    } // while

    // Append new text to the container element
    node.appendChild( text_node );

} 


// JavaScript Document
// Widgets is a way to initialize widgets in the ARIA examples


OAA_EXAMPLES.Widgets = function() {
  this.widgets = new Array();
}

/**
* add is member of the Widgets Object
* and used add a widget ot the list of widgets to be intitialized
* as part of the onload event
* The controls array is the list of controls to initialize
* @member Enable
* @return none
*/

Widgets.prototype.add = function(obj) {
  this.widgets[this.widgets.length] = obj;
}

/**
* init is member of the Widgets Object
* and is called by the onload event to initialize widgets in the web resource
* The controls array is the list of controls to initialize
* @member Enable
* @return none
*/

OAA_EXAMPLES.Widgets.prototype.init = function() {
     
   for(var i = 0; i < this.widgets.length; i++ )
     this.widgets[i].init();
}

var widgets = new Widgets();

function initApp() {
  widgets.init();
}
 

// JavaScript Document
// This module is to abstract browser dependencies
// This makes the widget code cleaner and earier to read by making most browser specfic coding
// in one place rather han scatered throghot documents
var ARIA_STATE = "aria-";

//
// WebBrowser object to abstract accessibility API differences between web standards supporting browsers and Internet Explorer 7.0
//
// The state variable keeps track of current state of checkbox
OAA_EXAMPLES.WebBrowser = function() {

}


/**
* @keyCode
*
* @memberOf OAA_EXAMPLES
* 
* @desc a function to get the keycode from a keypress event
* 
* @param {object} event - an event object
*
* @return {keycode}
*/

OAA_EXAMPLES.WebBrowser.prototype.keyCode = function( event ) {
  var e = event || window.event;
  
  return e.keyCode;
}  

/**
* OnClick Event Simulator
*
* @param ( node ) DOM node object
* @return nothing
*/

if( document.createEvent ) {

  // If a web standards based browser implement this function

  WebBrowser.prototype.simulateOnClickEvent = function( node ) {
    // W3C DOM Events way to trigger a "click" event
    var e = document.createEvent('MouseEvents');
    e.initEvent( 'click', true, true );

    node.dispatchEvent( e );

  }

} else {

  // If a Microsoft IE based browser implement this function
  
  WebBrowser.prototype.simulateOnClickEvent = function( node ) {

    var e = document.createEventObject();
    node.fireEvent( "onclick", e );

  } // endif

}

if ( document.addEventListener ) {

  // If a web standards based browser implement this function

  WebBrowser.prototype.setMouseCapture = function( node, clickHandler, downHandler, moveHandler, upHandler ) {

    if( clickHandler )
      document.addEventListener( "click",     clickHandler, true );
    
    if( downHandler )
      document.addEventListener( "mousedown", downHandler,  true );

    if( moveHandler )
      document.addEventListener( "mousemove", moveHandler,  true );
    
    if( upHandler)
      document.addEventListener( "mouseup",   upHandler,    true );

  }

  WebBrowser.prototype.releaseMouseCapture = function( node, clickHandler, downHandler, moveHandler, upHandler ) {

  if( upHandler)
      document.removeEventListener( "mouseup",   upHandler,    true );
      
    if( moveHandler )
      document.removeEventListener( "mousemove", moveHandler,  true );
    
    if( downHandler )
      document.removeEventListener( "mousedown", downHandler,  true );
      
    if( clickHandler )
      document.removeEventListener( "click",     clickHandler, true );

  }

} else {

  // If a Microsoft IE based browser implement this function

  WebBrowser.prototype.setMouseCapture = function( node, clickHandler, downHandler, moveHandler, upHandler ) {

   node.setCapture();
   if( clickHandler)
     node.attachEvent( "onclick", clickHandler );
    
   if( downHandler)
     node.attachEvent( "onmousedown", downHandler );
    
   if( moveHandler )
     node.attachEvent( "onmousemove", moveHandler );
    
   if( upHandler )
     node.attachEvent( "onmouseup", upHandler );

  } // endif

  WebBrowser.prototype.releaseMouseCapture = function( node, clickHandler, downHandler, moveHandler, upHandler ) {

   if( upHandler )
     node.detachEvent( "onmouseup", upHandler );
    
   if( moveHandler )
     node.detachEvent( "onmousemove", moveHandler );
    
   if( downHandler)
     node.detachEvent( "onmousedown", downHandler );
    
   if( clickHandler)
     node.detachEvent( "onclick", clickHandler );
    
     node.releaseCapture();

  } // endif


}




if (typeof document.documentElement.setAttributeNS != 'undefined') {

  WebBrowser.prototype.stopPropagation = function( event ) {
    if( event.stopPropagation )
      event.stopPropagation();
    if( event.preventDefault )
      event.preventDefault();
    return false;
  }

  WebBrowser.prototype.target = function( event ) {
  return event.target;
  }
  
  WebBrowser.prototype.attrName = function( event ) {
  return event.attrName;
  }

  WebBrowser.prototype.testAttrName = function( event , attrName) {
  return event.attrName == attrName;
  }

  WebBrowser.prototype.charCode = function(event) {
     return event.charCode;
  }

  WebBrowser.prototype.calculateOffsetLeft = function( node ) {
  return node.offsetLeft;    
  }
  
  WebBrowser.prototype.calculateOffsetTop = function( node ) {
  return node.offsetTop;    
  }
  
  WebBrowser.prototype.pageX = function( e ) {
    return e.pageX;    
  }
  
  WebBrowser.prototype.pageY = function( e ) {
    return e.pageY;    
  }
  
  WebBrowser.prototype.setNodePosition = function(node,left,top) {
    node.style.left = left+"px";
    node.style.top = top+"px";
  }


} else {

  WebBrowser.prototype.stopPropagation = function( event ) {
    event.cancelBubble = true;
    event.returnValue = false;
    return false;
  }

  WebBrowser.prototype.charCode = function(event) {
    return window.browser.keyCode( event );
  }

  WebBrowser.prototype.target = function( event ) {
    return event.srcElement;
  }

  WebBrowser.prototype.attrName = function( event ) {
  return event.propertyName;
  }
    
  WebBrowser.prototype.testAttrName = function( event , attrName) {
        
        var str = attrName;
        
        if( attrName.indexOf("aria-") >=0 ) {
            str = attrName.replace(/aria-/,"");
            var node = document.getElementById('test1');
            if( node )
               node.innerHTML = str.substr(0,1).toUpperCase();
            var len  = str.length;
            str = "aria" + str.substr(0,1).toUpperCase() + str.substr(1, len);
            var node = document.getElementById('test2');
//            if( node )
//               node.innerHTML = node.innerHTML + "<li>" + str + "</li>";
        }
        
        return event.propertyName == str;
  }
    
  WebBrowser.prototype.calculateOffsetLeft = function(node) {
  var offset = 0;
  
  while( node ) {
    offset += node.offsetLeft;
    node = node.offsetParent;
  }
  
  return offset;    
  }
  
  WebBrowser.prototype.calculateOffsetTop = function(node) {
  var offset = 0;
  
  while( node ) {
    offset = offset + node.offsetTop;
    node = node.offsetParent;
  }
  
  return offset;    
  }
  
  WebBrowser.prototype.pageX = function( e ) {
    return e.clientX + (document.documentElement.scrollLeft || document.body.scrollLeft);    
  }
  
  WebBrowser.prototype.pageY = function( e ) {
    return e.clientY + (document.documentElement.scrollTop || document.body.scrollTop);    
  }
  
  WebBrowser.prototype.setNodePosition = function(node,left,top) {
    offsetx = 0;
    offsety = 0;
    nnode = node.offsetParent
    while( nnode ) {
      offsetx = offsetx + nnode.offsetLeft;
      offsety = offsety + nnode.offsetTop;
      nnode = nnode.offsetParent;
    }
    node.style.left = left-offsetx+"px";
    node.style.top = top-offsety+"px";
  }
  
};


if (document.addEventListener) {

     // Functions for W3C Standards compliant implementation of adding event handlers

     WebBrowser.prototype.addEvent = function(elmTarget, sEventName, fCallback) {
       elmTarget.addEventListener(sEventName, fCallback, false);
       returnValue = true;
     };

     WebBrowser.prototype.removeEvent = function(elmTarget, sEventName, fCallback) {
       elmTarget.removeEventListener(sEventName, fCallback, false);
       returnValue = true;
     };

     WebBrowser.prototype.addChangeEvent =  function(elmTarget, fCallback) {
      elmTarget.addEventListener("DOMAttrModified", fCallback, false);
      returnValue = true;
    };

} else {

  if(document.attachEvent) {

     // IE Specific Event handler functions
     WebBrowser.prototype.addEvent = function(elmTarget, sEventName, fCallback) {
       returnValue = elmTarget.attachEvent('on' + sEventName, fCallback);
     };

     WebBrowser.prototype.removeEvent = function(elmTarget, sEventName, fCallback) {
       returnValue = elmTarget.detachEvent('on' + sEventName, fCallback);
     };

    WebBrowser.prototype.addChangeEvent =  function(elmTarget, fCallback) {
      returnValue = elmTarget.attachEvent("onpropertychange", fCallback);
    };

  } else {

     // For browsers that do not support W3C or IE event functions
     WebBrowser.prototype.addEvent = function(elmTarget, sEventName, fCallback) {
       return false;
     };

     WebBrowser.prototype.removeEvent = function(elmTarget, sEventName, fCallback) {
       return false;
     };

     WebBrowser.prototype.addChangeEvent =  function(elmTarget, fCallback) {
       return false;
     };

  }

}

var browser = new WebBrowser();


var minimumTime = 10000;
var index=0;
var conter = 0;
var lrID = "messages";
var messagesArray = new Array("...","you have new mail.", "you have new messages", "there are new news feeds");



function updateLiveRegion(liveRegionID, itemNumber) {
  
    textNode= document.createTextNode(messagesArray[index]);  
    targetNode = document.getElementById(liveRegionID);
    while (targetNode.firstChild) {
        targetNode.removeChild(targetNode.firstChild);
    }
  targetNode.appendChild(textNode);
}

function Live3() {
     
}


Live3.prototype.init = function() {
  runExample();  
}

function runExample() {
    updateLiveRegion(lrID,index);
   if (index >= messagesArray.length-1){
       index=0;
   }
   else{
       index++;
   }
   window.setTimeout(runExample, minimumTime);
}


function setMinimumTime(throttleId){
   minimumTimeStr = document.getElementById(throttleId).options[document.getElementById(throttleId).selectedIndex].text;  
   minimumTime = minimumTimeStr * 1000;
}

function updateAttribute(attribute, controlId, regionId){
    input =  document.getElementById(controlId).options[document.getElementById(controlId).selectedIndex].text;
    document.getElementById(regionId).setAttribute(attribute, input);
} 

(function($){$.extend({jGFeed:function(url,fnk,num,key){if(url==null){return false;}var gurl="http://ajax.googleapis.com/ajax/services/feed/load?v=1.0&callback=?&q="+url;if(num!=null){gurl+="&num="+num;}if(key!=null){gurl+="&key="+key;}$.getJSON(gurl,function(data){if(typeof fnk=="function"){fnk.call(this,data.responseData.feed);}else{return false;}});}});})(jQuery);

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

example3 = create_example(example_info)

ref = add_script_reference( example3, script1 )

CodingPattern.objects.get(slug='rss').examples.add(example3)

# =============================
# Example 4
# =============================


example_info             = example_object()
example_info.title       = 'Live Region: 4'
example_info.permanent_slug = 'live4'

example_info.description = """
Simple example of an RSS Feed Reader using a live region widget.
"""
example_info.keyboard    = """
"""

example_info.aria_labelledby = True
example_info.html_label = True

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

  <h2>Live Region Option</h2>
  
  <ul>
    <li>  
      <label for="throttle">Minimum number of seconds before a play can happen</label>
      <select id="throttle" onblur="setMinimumTimeBetweenPlays();" onchange="setMinimumTimeBetweenPlays();">
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
        <option>6</option>
        <option>7</option>
        <option>8</option>
        <option>9</option>
        <option>10</option>
      </select>
    </li>
  </ul>      


<h2>The Reals versus The Nicks Live Region</h2>

<div id="scoreboardRegion">

  <h2>Game Clock</h2>
  <h2 id="gameClock" aria-live="off">05:00</h2>


  <div id="theReals">
     <h3 id="realsScore" aria-live="polite">The Reals: 0</h3>
  
     <table id="realNamesStats" summary="Stats for the Reals team" border="1" width="100%">
     <tbody>
       <tr>
        <th>Lineup</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
     </tr>

       <tr aria-live="polite">
        <td id="charlesName">Charles</td>
      <td id="charlesPoints"   class="statsCell" aria-labelledby="charlesName">0</td>
      <td id="charlesRebounds" class="statsCell" aria-labelledby="charlesName">0</td>
      <td id="charlesAssists"  class="statsCell" aria-labelledby="charlesName">0</td>
     </tr>

       <tr aria-live="polite">
        <td id="aaronName">Aaron</td><td id="aaronPoints" class="statsCell" aria-labelledby="aaronName">0</td>
      <td id="aaronRebounds" class="statsCell" aria-labelledby="aaronName">0</td>
      <td id="aaronAssists"  class="statsCell" aria-labelledby="aaronName">0</td>
     </tr>

       <tr aria-live="polite">
        <td id="ginnName">Ginn</td>
      <td id="ginnPoints"   class="statsCell" aria-labelledby="ginnName">0</td>
      <td id="ginnRebounds" class="statsCell" aria-labelledby="ginnName">0</td>
      <td id="ginnAssists"  class="statsCell" aria-labelledby="ginnName">0</td>
     </tr>

      <tr aria-live="polite">
       <td id="steveName">Steve</td>
     <td id="stevePoints"   class="statsCell" aria-labelledby="steveName">0</td>
     <td id="steveRebounds" class="statsCell" aria-labelledby="steveName">0</td>
     <td id="steveAssists"  class="statsCell" aria-labelledby="steveName">0</td>
    </tr>
    </tbody>
    </table>
  </div>

  <div id="theNicks">
  
    <h3 id="nicksScore" aria-live="polite">The Nicks: 0</h3>

    <table id="nickNamesStats" summary="Stats for the Nicks team" border="1" width="100%">
    <tbody>
       <tr>
       <th>Lineup</th>
     <th>Points</th>
     <th>Rebounds</th>
     <th>Assists</th>
     </tr>

      <tr aria-live="polite">
      <td id="clcName">CLC-4-TTS</td>
    <td id="clcPoints"   class="statsCell" aria-labelledby="clcName">0</td>
    <td id="clcRebounds" class="statsCell" aria-labelledby="clcName">0</td>
    <td id="clcAssists"  class="statsCell" aria-labelledby="clcName">0</td>
    </tr>

      <tr aria-live="polite">
       <td id="aaronlevName">aaronlev</td>
     <td id="aaronlevPoints"   class="statsCell" aria-labelledby="aaronlevName">0</td>
     <td id="aaronlevRebounds" class="statsCell" aria-labelledby="aaronlevName">0</td>
     <td id="aaronlevAssists"  class="statsCell" aria-labelledby="aaronlevName">0</td>
    </tr>

     <tr aria-live="polite">
      <td id="gcName">GC</td>
    <td id="gcPoints"   class="statsCell" aria-labelledby="gcName">0</td>
    <td id="gcRebounds" class="statsCell" aria-labelledby="gcName">0</td>
    <td id="gcAssists"  class="statsCell" aria-labelledby="gcName">0</td>
     </tr>

     <tr aria-live="polite">
      <td id="slName">SL</td>
    <td id="slPoints"   class="statsCell" aria-labelledby="slName">0</td>
    <td id="slRebounds" class="statsCell" aria-labelledby="slName">0</td>
    <td id="slAssists"  class="statsCell" aria-labelledby="slName">0</td>
   </tr>
   </tbody>
   </table>
  
  </div>
  
</div>

<div id="winnerDiv">
  <h2 id="theWinner" aria-live="polite"></h2>
</div> 
"""
example_info.script      = """
function Live4() {
  
}

Live4.prototype.init = function() {
   document.getElementById("throttle").selectedIndex = 4;
   runGame();  
}

var minimumWaitTime = 5;
var currentTimer = 0;

function statFlash(statID){
   document.getElementById(statID).style.backgroundColor = "black";
   document.getElementById(statID).style.color = "yellow";
   document.getElementById(statID).style.fontWeight = "bold";
   window.setTimeout(function (flashedID) {
       document.getElementById(flashedID).style.backgroundColor = "";
       document.getElementById(flashedID).style.color = "";
       document.getElementById(flashedID).style.fontWeight = "";
       },500,statID);
   }

function runGame(){
   updateGameClock();
   if (currentTimer < 1){
      makeAPlay();
      currentTimer = minimumWaitTime;
      }
   currentTimer = currentTimer-1;
   if (!gameOver()){
      window.setTimeout(runGame,1000);
      }
   }

function updateGameClock(){
   var gameclockStr = document.getElementById('gameClock').textContent;
   if (gameclockStr == null){
      gameclockStr = document.getElementById('gameClock').innerText;
      }
   var minutes = parseInt(gameclockStr.substring(0,gameclockStr.indexOf(':')));
   var seconds = parseInt(gameclockStr.substring(gameclockStr.indexOf(':')+1));
   if (seconds > 0){
      seconds = seconds-1;
      }
   else if (minutes > 0){
      minutes = minutes-1;
      seconds = 59;
      }
   var zeroPadMin = "";
   if (minutes < 10){
      zeroPadMin = "0";
      }
   var zeroPadSec = "";
   if (seconds < 10){
      zeroPadSec = "0";
      }
   document.getElementById('gameClock').textContent = zeroPadMin + minutes + ":" + zeroPadSec + seconds;
   document.getElementById('gameClock').innerText = zeroPadMin + minutes + ":" + zeroPadSec + seconds;
   }

function gameOver(){
   var gameclockStr = document.getElementById('gameClock').textContent;
   if (gameclockStr == null){
      gameclockStr = document.getElementById('gameClock').innerText;
      }
   if (gameclockStr == "00:00"){
      declareWinner();
      return true;
      }
   return false;
   }

function declareWinner(){
   var theScoreStr = document.getElementById('realsScore').textContent;
   if (theScoreStr == null){
      theScoreStr = document.getElementById('realsScore').innerText;
      }
   var theRealsScore = parseInt(theScoreStr.substring(theScoreStr.indexOf(':')+1));
   theScoreStr = document.getElementById('nicksScore').textContent;
   if (theScoreStr == null){
      theScoreStr = document.getElementById('nicksScore').innerText;
      }
   var theNicksScore = parseInt(theScoreStr.substring(theScoreStr.indexOf(':')+1));
   if (theRealsScore > theNicksScore){
      document.getElementById('theWinner').textContent = "Game over! The Reals win!";
      document.getElementById('theWinner').innerText = "Game over! The Reals win!";
      }
   else if (theRealsScore < theNicksScore){
      document.getElementById('theWinner').textContent = "Game over! The Nicks win!";
      document.getElementById('theWinner').innerText = "Game over! The Nicks win!";
      }
   else{
      document.getElementById('theWinner').textContent = "Game over! Draw!";
      document.getElementById('theWinner').innerText = "Game over! Draw!";
      }
   }

function makeAPlay(){
   var rand = Math.random();
   if (rand < .1){
      theRealsScored();
      return;
      }
   if (rand < .3){
      randomRebound();
      return;
      }
   if (rand > .9){
      theNicksScored();
      return;
      }  
   }

function theRealsScored(){
   var theScoreStr = document.getElementById('realsScore').textContent;
   if (theScoreStr == null){
      theScoreStr = document.getElementById('realsScore').innerText;
      }
   var theScore = parseInt(theScoreStr.substring(theScoreStr.indexOf(':')+1));
   theScore = theScore + 1;
   document.getElementById('realsScore').textContent = "The Reals: " + theScore;
   document.getElementById('realsScore').innerText = "The Reals: " + theScore;  
   statFlash('realsScore');
   var rand = Math.random();
   if (rand < .4){
      playerStatIncreased("charlesPoints");
      if (rand < .2){
         playerStatIncreased("steveAssists");
         }
      }
   else if (rand < .6){
      playerStatIncreased("stevePoints");
      if (rand < .5){
         playerStatIncreased("charlesAssists");
         }
      }
   else if (rand < .8){
      playerStatIncreased("ginnPoints");
      if (rand < .7){
         playerStatIncreased("aaronlevAssists");
         }
      }
   else{
      playerStatIncreased("aaronPoints");
      if (rand < .9){
         playerStatIncreased("ginnAssists");
         }
      }
   }

function theNicksScored(){
   var theScoreStr = document.getElementById('nicksScore').textContent;
   if (theScoreStr == null){
      theScoreStr = document.getElementById('nicksScore').innerText;
      }
   var theScore = parseInt(theScoreStr.substring(theScoreStr.indexOf(':')+1));
   theScore = theScore + 1;
   document.getElementById('nicksScore').textContent = "The Nicks: " + theScore;
   document.getElementById('nicksScore').innerText = "The Nicks: " + theScore;
   statFlash('nicksScore');
   var rand = Math.random();
   if (rand < .4){
      playerStatIncreased("clcPoints");
      if (rand < .2){
         playerStatIncreased("aaronlevAssists");
         }
      }
   else if (rand < .6){
      playerStatIncreased("slPoints");
      if (rand < .5){
         playerStatIncreased("gcAssists");
         }
      }
   else if (rand < .8){
      playerStatIncreased("gcPoints");
      if (rand < .7){
         playerStatIncreased("slAssists");
         }
      }
   else{
      playerStatIncreased("aaronlevPoints");
      if (rand < .9){
         playerStatIncreased("clcAssists");
         }
      }
   }

function randomRebound(){
   var rand = Math.random();
   if (rand < .2){
      playerStatIncreased("charlesRebounds");
      }
   else if (rand < .3){
      playerStatIncreased("steveRebounds");
      }
   else if (rand < .4){
      playerStatIncreased("ginnRebounds");
      }
   else if (rand < .5){
      playerStatIncreased("aaronRebounds");
      }
   else if (rand < .7){
      playerStatIncreased("clcRebounds");
      }
   else if (rand < .8){
      playerStatIncreased("slRebounds");
      }
   else if (rand < .9){
      playerStatIncreased("gcRebounds");
      }
   else{
      playerStatIncreased("aaronlevRebounds");
      }
   }

function playerStatIncreased(playerStatsIDStr){
   var theStatsStr = document.getElementById(playerStatsIDStr).textContent;
   if (theStatsStr == null){
      theStatsStr = document.getElementById(playerStatsIDStr).innerText;
      }
   var stats = parseInt(theStatsStr);
   stats = stats + 1;
   document.getElementById(playerStatsIDStr).textContent = stats;
   document.getElementById(playerStatsIDStr).innerText = stats;
   statFlash(playerStatsIDStr);
   }

function setMinimumTimeBetweenPlays(){
   minimumWaitTime = document.getElementById("throttle").options[document.getElementById("throttle").selectedIndex].text;  
   currentTimer = minimumWaitTime;
   } 

/**
*
* The Globale Variables
*/

if (!window.Node) {
  var Node = {            // If there is no Node object, define one
    ELEMENT_NODE: 1,    // with the following properties and values.
    ATTRIBUTE_NODE: 2,  // Note that these are HTML node types only.
    TEXT_NODE: 3,       // For XML-specific nodes, you need to add
    COMMENT_NODE: 8,    // other constants here.
    DOCUMENT_NODE: 9,
    DOCUMENT_FRAGMENT_NODE: 11
  }
}


var KEY_PAGEUP   = 33;
var KEY_PAGEDOWN = 34;
var KEY_END      = 35;
var KEY_HOME     = 36;

var KEY_LEFT     = 37;
var KEY_UP       = 38;
var KEY_RIGHT    = 39;
var KEY_DOWN     = 40;

var KEY_SPACE    = 32;
var KEY_TAB      = 9;

var KEY_BACKSPACE = 8;
var KEY_DELETE    = 46;
var KEY_ENTER     = 13;
var KEY_INSERT    = 45;
var KEY_ESCAPE    = 27;

var KEY_F1        = 112;
var KEY_F2        = 113;
var KEY_F3        = 114;
var KEY_F4        = 115;
var KEY_F5        = 116;
var KEY_F6        = 117;
var KEY_F7        = 118;
var KEY_F8        = 119;
var KEY_F9        = 120;
var KEY_F10       = 121;

var KEY_M         = 77;

var NS_XHTML = "http://www.w3.org/1999/xhtml"
var NS_STATE = "http://www.w3.org/2005/07/aaa";

// **********************************************
// *
// * Commonly used helper functions
// *
// **********************************************

/**
*
* nextSiblingElement
*
* @contructor
*/

function nextSiblingElement( node ) {

  var next_node = node.nextSibling;

  while( next_node
    && (next_node.nodeType != Node.ELEMENT_NODE) ) {
    next_node = next_node.nextSibling;
  }  // endwhile

  return next_node;
  
}

/**
*
* previousSiblingElement
*
* @param ( node ) node object for which you are looking for the next sibling element node
*
* @return ( node) next sibling or "null"
*/

function previousSiblingElement( node ) {

  var next_node = node.previousSibling;

  while( next_node
    && (next_node.nodeType != Node.ELEMENT_NODE) ) {
    next_node = next_node.previousSibling;
  }  // endwhile

  return next_node;
  
}

/**
*
* firstChildElement
*
* @param ( node ) node object for which you are looking for the first child element node
*
* @return ( node) next sibling or "null"
*/

function firstChildElement( node ) {

  var next_node = node.firstChild;

  while( next_node
    && (next_node.nodeType != Node.ELEMENT_NODE) ) {
    next_node = next_node.nextSibling;
  }  // endwhile


  return next_node;
  
}

/**
*
* getTextContentOfNode
*
* @contructor
*/

function getTextContentOfNode( node ) {

  var next_node = node.firstChild;
  var str = "";

  while( next_node ) {
    
    if( (next_node.nodeType == Node.TEXT_NODE ) &&
      (next_node.length > 0 )
     )
      str += next_node.data;
    
    
    next_node = next_node.nextSibling;
    
  }  // endwhile

  return str;
  
}

/**
*
* setTextContentOfNode
*
* @contructor
*/

function setTextContentOfNode( node, text ) {

   // Generate a new text node with the text value
    var text_node = document.createTextNode(text);
  
    // Remove child nodes to remove text
    while (node.firstChild) {
      node.removeChild(node.firstChild);
    } // while

    // Append new text to the container element
    node.appendChild( text_node );

} 

// JavaScript Document
// This module is to abstract browser dependencies
// This makes the widget code cleaner and earier to read by making most browser specfic coding
// in one place rather han scatered throghot documents
var ARIA_STATE = "aria-";

//
// WebBrowser object to abstract accessibility API differences between web standards supporting browsers and Internet Explorer 7.0
//
// The state variable keeps track of current state of checkbox
function WebBrowser() {

}


//
// keyCode is a function to get the keycode from a keypress event
//
// @param ( event object) event is an event object
//
// @return ( keycode )

WebBrowser.prototype.keyCode = function( event ) {
  var e = event || window.event;
  
  return e.keyCode;
}  

/**
* OnClick Event Simulator
*
* @param ( node ) DOM node object
* @return nothing
*/

if( document.createEvent ) {

  // If a web standards based browser implement this function

  WebBrowser.prototype.simulateOnClickEvent = function( node ) {
    // W3C DOM Events way to trigger a "click" event
    var e = document.createEvent('MouseEvents');
    e.initEvent( 'click', true, true );

    node.dispatchEvent( e );

  }

} else {

  // If a Microsoft IE based browser implement this function
  
  WebBrowser.prototype.simulateOnClickEvent = function( node ) {

    var e = document.createEventObject();
    node.fireEvent( "onclick", e );

  } // endif

}

if ( document.addEventListener ) {

  // If a web standards based browser implement this function

  WebBrowser.prototype.setMouseCapture = function( node, clickHandler, downHandler, moveHandler, upHandler ) {

    if( clickHandler )
      document.addEventListener( "click",     clickHandler, true );
    
    if( downHandler )
      document.addEventListener( "mousedown", downHandler,  true );

    if( moveHandler )
      document.addEventListener( "mousemove", moveHandler,  true );
    
    if( upHandler)
      document.addEventListener( "mouseup",   upHandler,    true );

  }

  WebBrowser.prototype.releaseMouseCapture = function( node, clickHandler, downHandler, moveHandler, upHandler ) {

  if( upHandler)
      document.removeEventListener( "mouseup",   upHandler,    true );
      
    if( moveHandler )
      document.removeEventListener( "mousemove", moveHandler,  true );
    
    if( downHandler )
      document.removeEventListener( "mousedown", downHandler,  true );
      
    if( clickHandler )
      document.removeEventListener( "click",     clickHandler, true );

  }

} else {

  // If a Microsoft IE based browser implement this function

  WebBrowser.prototype.setMouseCapture = function( node, clickHandler, downHandler, moveHandler, upHandler ) {

   node.setCapture();
   if( clickHandler)
     node.attachEvent( "onclick", clickHandler );
    
   if( downHandler)
     node.attachEvent( "onmousedown", downHandler );
    
   if( moveHandler )
     node.attachEvent( "onmousemove", moveHandler );
    
   if( upHandler )
     node.attachEvent( "onmouseup", upHandler );

  } // endif

  WebBrowser.prototype.releaseMouseCapture = function( node, clickHandler, downHandler, moveHandler, upHandler ) {

   if( upHandler )
     node.detachEvent( "onmouseup", upHandler );
    
   if( moveHandler )
     node.detachEvent( "onmousemove", moveHandler );
    
   if( downHandler)
     node.detachEvent( "onmousedown", downHandler );
    
   if( clickHandler)
     node.detachEvent( "onclick", clickHandler );
    
     node.releaseCapture();

  } // endif


}




if (typeof document.documentElement.setAttributeNS != 'undefined') {

  WebBrowser.prototype.stopPropagation = function( event ) {
    if( event.stopPropagation )
      event.stopPropagation();
    if( event.preventDefault )
      event.preventDefault();
    return false;
  }

  WebBrowser.prototype.target = function( event ) {
  return event.target;
  }
  
  WebBrowser.prototype.attrName = function( event ) {
  return event.attrName;
  }

  WebBrowser.prototype.testAttrName = function( event , attrName) {
  return event.attrName == attrName;
  }

  WebBrowser.prototype.charCode = function(event) {
     return event.charCode;
  }

  WebBrowser.prototype.calculateOffsetLeft = function( node ) {
  return node.offsetLeft;    
  }
  
  WebBrowser.prototype.calculateOffsetTop = function( node ) {
  return node.offsetTop;    
  }
  
  WebBrowser.prototype.pageX = function( e ) {
    return e.pageX;    
  }
  
  WebBrowser.prototype.pageY = function( e ) {
    return e.pageY;    
  }
  
  WebBrowser.prototype.setNodePosition = function(node,left,top) {
    node.style.left = left+"px";
    node.style.top = top+"px";
  }


} else {

  WebBrowser.prototype.stopPropagation = function( event ) {
    event.cancelBubble = true;
    event.returnValue = false;
    return false;
  }

  WebBrowser.prototype.charCode = function(event) {
    return window.browser.keyCode( event );
  }

  WebBrowser.prototype.target = function( event ) {
    return event.srcElement;
  }

  WebBrowser.prototype.attrName = function( event ) {
  return event.propertyName;
  }
    
  WebBrowser.prototype.testAttrName = function( event , attrName) {
        
        var str = attrName;
        
        if( attrName.indexOf("aria-") >=0 ) {
            str = attrName.replace(/aria-/,"");
            var node = document.getElementById('test1');
            if( node )
               node.innerHTML = str.substr(0,1).toUpperCase();
            var len  = str.length;
            str = "aria" + str.substr(0,1).toUpperCase() + str.substr(1, len);
            var node = document.getElementById('test2');
//            if( node )
//               node.innerHTML = node.innerHTML + "<li>" + str + "</li>";
        }
        
        return event.propertyName == str;
  }
    
  WebBrowser.prototype.calculateOffsetLeft = function(node) {
  var offset = 0;
  
  while( node ) {
    offset += node.offsetLeft;
    node = node.offsetParent;
  }
  
  return offset;    
  }
  
  WebBrowser.prototype.calculateOffsetTop = function(node) {
  var offset = 0;
  
  while( node ) {
    offset = offset + node.offsetTop;
    node = node.offsetParent;
  }
  
  return offset;    
  }
  
  WebBrowser.prototype.pageX = function( e ) {
    return e.clientX + (document.documentElement.scrollLeft || document.body.scrollLeft);    
  }
  
  WebBrowser.prototype.pageY = function( e ) {
    return e.clientY + (document.documentElement.scrollTop || document.body.scrollTop);    
  }
  
  WebBrowser.prototype.setNodePosition = function(node,left,top) {
    offsetx = 0;
    offsety = 0;
    nnode = node.offsetParent
    while( nnode ) {
      offsetx = offsetx + nnode.offsetLeft;
      offsety = offsety + nnode.offsetTop;
      nnode = nnode.offsetParent;
    }
    node.style.left = left-offsetx+"px";
    node.style.top = top-offsety+"px";
  }
  
};


if (document.addEventListener) {

     // Functions for W3C Standards compliant implementation of adding event handlers

     WebBrowser.prototype.addEvent = function(elmTarget, sEventName, fCallback) {
       elmTarget.addEventListener(sEventName, fCallback, false);
       returnValue = true;
     };

     WebBrowser.prototype.removeEvent = function(elmTarget, sEventName, fCallback) {
       elmTarget.removeEventListener(sEventName, fCallback, false);
       returnValue = true;
     };

     WebBrowser.prototype.addChangeEvent =  function(elmTarget, fCallback) {
      elmTarget.addEventListener("DOMAttrModified", fCallback, false);
      returnValue = true;
    };

} else {

  if(document.attachEvent) {

     // IE Specific Event handler functions
     WebBrowser.prototype.addEvent = function(elmTarget, sEventName, fCallback) {
       returnValue = elmTarget.attachEvent('on' + sEventName, fCallback);
     };

     WebBrowser.prototype.removeEvent = function(elmTarget, sEventName, fCallback) {
       returnValue = elmTarget.detachEvent('on' + sEventName, fCallback);
     };

    WebBrowser.prototype.addChangeEvent =  function(elmTarget, fCallback) {
      returnValue = elmTarget.attachEvent("onpropertychange", fCallback);
    };

  } else {

     // For browsers that do not support W3C or IE event functions
     WebBrowser.prototype.addEvent = function(elmTarget, sEventName, fCallback) {
       return false;
     };

     WebBrowser.prototype.removeEvent = function(elmTarget, sEventName, fCallback) {
       return false;
     };

     WebBrowser.prototype.addChangeEvent =  function(elmTarget, fCallback) {
       return false;
     };

  }

}

var browser = new WebBrowser();

"""

example_info.style       = """
div.controls {
	margin-left: 10px;
	padding: 5px 10px;
	width: 21em;
	float: left;
	display: inline;
	overflow: visible;
}
button,
select {
	float: right;
}
div#countdown {
	margin-top: 3em;
	margin-bottom: 1em;
}
#timerlabel {
	margin-left: 4em;
	font-weight: bold;
}
#timer {
	margin: 0;
	padding: 2px 5px;
	float: right;
	width: 3.5em;
	height: 1.2em;
	font-weight: bold;
	text-align: right;
	background-color: #eee;
	border: 1px solid black;
}
hr {
	height: 1px;
	width: 80%;
	color: #000088;
	background-color: #000088;
}
#rssFeedContent {
	margin: 10px;
	padding: 10px;
	width: 43em;
	border: 1px solid black;
	clear: both;
}

.entry {
	margin-bottom: 20px;
	width: 40em;
}
.postTitle {
	margin: 0;
	padding: 5px;
}
.entry a.storyLink {
	padding-bottom: 1px;
	color: #000088;
	font-size: 1.2em;
	text-decoration: none;
	border-bottom: 1px solid #000088;
}
.entry a.storyLink:hover {
	color: #880000;
	border-bottom: 2px solid #880000;
}
.entry a.storyLink:visited {
	color: #777;
}

.entry .date {
	margin: 0;
	padding: 0;
	padding-right: 10px;
	font-size: 80%;
	letter-spacing: 0.1em;
}

.entry .summary {
	margin: 0;
	padding: 0 10px;
}
"""

example4 = create_example(example_info)

ref = add_script_reference( example4, script1 )

CodingPattern.objects.get(slug='rss').examples.add(example4)

