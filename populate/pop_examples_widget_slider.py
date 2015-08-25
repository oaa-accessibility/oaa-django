"""This file is for populating the database with projects,  users,  etc whenever
I empty it. Run as a standalone script!"""

from django.core.exceptions import ObjectDoesNotExist
from pop_examples_common import *


# =============================
# Example 1
# =============================

order = 1
eg_range = ExampleGroup.objects.get(slug="aria-range")
eg_focus    = ExampleGroup.objects.get(slug="focus")
eg_widgets  = ExampleGroup.objects.get(slug="widgets")

example_info             = example_object()
example_info.order          = order
example_info.example_groups = [eg_range, eg_widgets]
example_info.title       = 'Slider'
example_info.permanent_slug = 'slider1'

example_info.description = """
Simple examples of a slider widget.
"""
example_info.keyboard    = """
* Left / Down: Decrease (one unit)
* Right / Up: Increase (one unit)
* PgUp / Pgdown: Large change (10 units)
* Home: Set slider to minimum
* End: Set slider to maximum
* Tab: Navigate between slider controls
"""
example_info.aria_labelledby = True

spec_aria10 = LanguageSpec.objects.get(url_slug='aria10')


m1 = ElementDefinition.objects.get(spec=spec_aria10, attribute="role", value='slider')
m2 = ElementDefinition.objects.get(spec=spec_aria10, attribute="aria-valuemax")
m3 = ElementDefinition.objects.get(spec=spec_aria10, attribute="aria-valuemin")
m4 = ElementDefinition.objects.get(spec=spec_aria10,  attribute="aria-valuenow")

example_info.markup = [m1,m2,m3,m4]

rr1 = rule_reference_object("KEYBOARD_1", "pass", "pass", "KEYBOARD_1_T1", "", "")
rr2 = rule_reference_object("KEYBOARD_2", "pass", "pass", "KEYBOARD_2_T1", "", "")
rr3 = rule_reference_object("WIDGET_1","pass", "pass", "WIDGET_1_T3","","")
rr4 = rule_reference_object("WIDGET_10","pass","na","WIDGET_10_T1","","")
rr5 = rule_reference_object("WIDGET_11","pass","na","WIDGET_11_T1","","")
rr6 = rule_reference_object("WIDGET_3","pass","na","WIDGET_3_T1","","")
rr7 = rule_reference_object("WIDGET_4","pass","na","WIDGET_4_T1","","")
rr8 = rule_reference_object("WIDGET_5","pass","na","WIDGET_5_T1","","")

example_info.rule_references = [rr1,rr2,rr3,rr4,rr5,rr6,rr7,rr8]

example_info.html        = """
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<div role="application">

  <h3>Slider Example 1: A Simple Slider</h3>
	
  <div id="sr1_label" class="hidden">Example 1 Slider</div>
  <div class="hslider" aria-label="slider 1" id="sr1"></div>	
		  
  <h3>Slider Example 2: A Range Slider</h3>
	
  <div id="sr2_label1" class="hidden">Example 2 Slider Low</div>
  <div id="sr2_label2" class="hidden">Example 2 Slider High</div>
  <div class="hslider" aria-label="slider 2" id="sr2"></div>	

  <h3>Slider Example 3: A Vertical Slider</h3>
	
  <div id="sr3_label" class="hidden">Example 3 Slider</div>
  <div class="vslider" aria-label="slider 3" id="sr3"></div>	
</div>
"""
example_info.script      = """
var OAA_EXAMPLES = OAA_EXAMPLES || {};

$(document).ready(function() {
	// slider1 is a horizontal slider
	var slider1 = new OAA_EXAMPLES.slider('sr1', false, 0, 100, 5, 10, true, false, 30); 

	// slider2 is a horizontal range slider
	var slider2 = new OAA_EXAMPLES.slider('sr2', false, 1900, 2013, 1, 10, true, true, 1955, 2000);

	// slider3 is a vertical range slider
	//var slider3 = new OAA_EXAMPLES.slider('sr3', true, 0, 100, 1, true, false, 25);
	var slider3 = new OAA_EXAMPLES.slider('sr3', true, 1900, 2013, -1, 10, true, true, 1950, 2000);
}); // end document ready


/**
 function keyCodes() is an object to contain key code values for the application
*/
function keyCodes() {
	// Define values for keycodes
	this.backspace  = 8;
	this.tab        = 9;
	this.enter      = 13;
	this.esc        = 27;

	this.space      = 32;
	this.pageup     = 33;
	this.pagedown   = 34;
	this.end        = 35;
	this.home       = 36;

	this.left       = 3;
	this.up         = 38;
	this.right      = 39;
	this.down       = 40; 

} // end keyCodes

/**
* @constructor slider
*
* @memberOf OAA_EXAMPLES
*
* @desc function slider() is a class to define an ARIA-enabled slider widget. The class
* will create needed handles and define ARIA attributes for the slider
*
* @param {String} container_id -  is the containing div for the slider
*
* @param {boolean} vert -  is true if the slider is vertical; false if horizontal
*
* @param {integer} inc - is the increment value for the slider
*
* @param {integer} jump - is the large increment value for the slider (pgUp/pgDown keys)
*
* @param {boolean} showVals - is true if the slider should display the value of the handles
*
* @param {boolean} range - is true if the slider is a range slider
*
* @param {integer} val1 - specifies the initial value of the slider or of the first
*         slide handle if this is a range slider. Must be >= min.
*
* @param {integer} val2 - specifies the initial value of the second slide handle.
*         Ignored if range is false (i.e. not a range slider). Must be <= max.
*
* @return {N/A}
*/

/**
* @private
* @constructor Internal Properties
* 
* @property {keyCodes} keys - assigns a key-coded value to properties
*
* @property {String} id - Identifies each slider
*
* @property {String} $container - 
*
* @property {boolean} vert - True for vertical slider, false for horizontal
*
* @property {integer} range - Range of values that the sliders can slide through
*
* @property {boolean} showVals - True for values to appear on slider, false for hidden values
*
* @property {integer} width - Store the size (width) of the slider
* @property {integer} height - Store the size (height) of the slider
*
* @property {integer} left - Store the page position of the slider
* @property {integer} top - Store the page position of the slider
*
* @property {integer} min - Store the minimum value of the slider
* @property {integer} max - Store the maximum value of the slider
* @property {integer} inc - Store the increment value of the slider
* @property {integer} jump - Store the jump value
* @property {integer} val1 -Store the first initial value
* @property {integer} val2 - Store the second initial value (only used for range sliders)
*
* @property {obj} $handle1 - Assigns an object pointer for the handle for val1
* @property {obj} $handle2 - Assigns an object pointer for the handle for val2
*/

OAA_EXAMPLES.slider = function(container_id, vert, min, max, inc, jump, showVals, range, val1, val2){
	this.keys = new keyCodes();

	this.id = container_id;
	this.$container = $('#' + container_id);
	this.vert = vert;
	this.range = range;
	this.showVals = showVals;

	this.width = this.$container.outerWidth();
	this.height = this.$container.outerHeight();

	this.left = Math.round(this.$container.offset().left);
	this.top = Math.round(this.$container.offset().top);

	this.min = min;
	this.max = max;
	this.inc = inc;
	this.jump = jump;
	this.val1 = val1;

	if (range == true) {
		this.val2 = val2;
	}
	
	this.$handle1 = undefined;
	this.$handle2 = undefined;

	if ( range == false) {
		// Create the handle
		this.$handle1 = this.createHandle(val1);
	}
	else {
		// create the range highlight div
		this.createRangeDiv();

		// Create the first handle
		this.$handle1 = this.createHandle(val1, 1);

		// create the second handle
		this.$handle2 = this.createHandle(val2, 2);
	}

} // end slider constructor

/**
* @method createHandle
* 
* @memberOf OAA_EXAMPLES
*
* @desc Creates a handle for the slider. It defines ARIA attributes for
* the handle and positions it at the specified value in the slider range. if showVals
* is true, create and position divs to display the handle value
* 
* @param {integer} val - is the initial value of the handle
*
* @param {integer} num - is the handle number. (optional)
*
* @return {obj} returns the object pointer of the newly created handle
*
*/

OAA_EXAMPLES.slider.prototype.createHandle = function(val, num) {

	var id = this.id + '_handle' + (num == undefined ? '' : num);
	var label = this.id + '_label' + (num == undefined ? '' : num);
	var controls = this.id + '_text' + (num == undefined ? '' : num);
	var $handle;

	var handle = '<img id="' + id + '" class="' + (this.vert == true ? 'v':'h') +'sliderHandle" ' +
		'src="{{EXAMPLE_MEDIA}}images/slider_' + (this.vert == true ? 'v':'h') + '.png" ' + 'role="slider" ' +
		'aria-valuemin="' + this.min +
		'" aria-valuemax="' + this.max +
		'" aria-valuenow="' + (val == undefined ? this.min : val) +
	       	'" aria-labelledby="' + label +
	       	'" aria-controls="' + controls + '" tabindex="0"></img>';

	// Create the handle
	this.$container.append(handle);

	// store the handle object
	$handle = $('#' + id);

	if (this.showVals == true) {
		var valContainer = '<div id="' + id + '_val" class="' + (this.vert == true ? 'v':'h') + 'sliderValue" role="presentation"></div>'

		// Create the container.
		this.$container.append(valContainer);
	}

	// store the value object
	$handle = $('#' + id);

	// position handle
	this.positionHandle($handle, val);
	
	// bind handlers
	this.bindHandlers($handle);
	
	return $handle;
	
} // end createHandle()

/**
* @method createRangeDiv
*
* @memberOf OAA_EXAMPLES
*
* @desc creates a div for the highlight of a range slider. It sets the initial top  
* or left position
*
* @return {N/A}
*/

OAA_EXAMPLES.slider.prototype.createRangeDiv = function() {

	var id = this.id + '_range';

	var range = '<div id="' + id + '" class="sliderRange"></div>';

	// Create the range div
	this.$container.append(range);

	// Store the div object
	this.$rangeDiv = $('#' + id);

	if (this.vert == false) { // horizontal slider
		this.$rangeDiv.css('top', this.top + 'px');
		this.$rangeDiv.css('height', this.$container.height() + 'px');
	}
	else { // vertical slider
		this.$rangeDiv.css('left', this.left + 'px');
		this.$rangeDiv.css('width', this.$container.width() + 'px');
	}
	
} // end createRangeDiv()

/**
* @method positionHandle
*
* @memberOf OAA_EXAMPLES
*
* @desc is a member function to position a handle at the specified value for the
* slider. If showVal is true, it also positions and updates the displayed value
* container.
*
* @param {obj} $handle - is a pointer to the handle jQuery object to manipulate
*
* @param {integer} val - is the new value of the slider
*
* @return {N/A}
*/

OAA_EXAMPLES.slider.prototype.positionHandle = function($handle, val) {

	var handleHeight = $handle.outerHeight(); // the total height of the handle
	var handleWidth = $handle.outerWidth(); // the total width of the handle
	var handleOffset; // the distance from the value position for centering the handle
	var xPos; // calculated horizontal position of the handle;
	var yPos; // calculated vertical position of the handle;
	var valPos; //calculated new pixel position for the value;

	if (this.vert == false) {
		// horizontal slider
		
		// calculate the horizontal pixel position of the specified value
		valPos = ((val - this.min) / (this.max - this.min)) * this.width + this.left;

		xPos = Math.round(valPos - (handleWidth / 2));
		yPos = Math.round(this.top + (this.height / 2) - (handleHeight / 2));
	}
	else {
		// vertical slider

		// calculate the vertical pixel position of the specified value
		valPos = ( (val - this.min) / (this.max - this.min) ) * this.height + this.top;

		xPos = Math.round(this.left + (this.width / 2) - (handleWidth / 2));
		yPos = Math.round(valPos - (handleHeight / 2));
	}

	// Set the position of the handle
	$handle.css('top', yPos + 'px');
	$handle.css('left', xPos + 'px');

	// Set the aria-valuenow position of the handle
	$handle.attr('aria-valuenow', val);

	// Update the stored handle values
	if (/1$/.test($handle.attr('id')) == true) {
		// first handle
		this.val1 = val;
	}
	else {
		// second handle
		this.val2 = val;
	}

	// if range is true, set the position of the range div
	if (this.range == true) {
		this.positionRangeDiv();
	}

	// if showVal is true, update the value container
	if (this.showVals == true) {
		this.updateValBox($handle, Math.round(valPos));
	}

} // end positionHandle()

/**
* @method positionRangeDiv
*
* @memberOf OAA_EXAMPLES
*
* @desc positionRangeDiv is a member function to reposition the range div when a
* handle is moved
*
*@return {N/A}
*/

OAA_EXAMPLES.slider.prototype.positionRangeDiv = function() {

	var pos; //calculated new range start position;
	var size; //calculated new range size;

	if (this.vert == false) { // Horizontal slider

		// calculate the range start position
		pos = Math.round( ((this.val1 - this.min) / (this.max - this.min)) * this.width) + this.left;

		// calculate the new range width
		size = Math.round( ((this.val2 - this.min) / (this.max - this.min)) * this.width) + this.left - pos;

		// set the new range position
		this.$rangeDiv.css('left', pos + 'px');

		// set the new range width
		this.$rangeDiv.css('width', size + 'px');
	}
	else {
		// calculate the range start position
		pos = Math.round(( (this.val1 - this.min) / (this.max - this.min)) * this.height)+ this.top;

		// calculate the new range width
		size = Math.round(( (this.val2 - this.min) / (this.max - this.min) ) * this.height) + this.top - pos;
	
		// set the new range position
		this.$rangeDiv.css('top', pos + 'px');

		// set the new range width
		this.$rangeDiv.css('height', size + 'px');
	}

} // end positionRangeDiv()

/**
* @method updateValBox
*
* @memberOf OAA_EXAMPLES
*
* @desc is a member function to reposition a handle value box and
* update its contents
*
* @param {obj} $handle - the jQuery object of the handle that was moved
*
* @param {integer} valPos - the pixel position of the slider value
*
* @return {N/A}
*/

OAA_EXAMPLES.slider.prototype.updateValBox = function($handle, valPos) {

	var $valBox = $('#' + $handle.attr('id') + '_val');

	var xPos; // horizontal pixel position of the box
	var yPos; // vertical pixel position of the box

	// Set the position of the handle
	if (this.vert == false) {
		var boxWidth = $valBox.outerWidth();

		yPos = $handle.css('top');

		// Adjust the horizontal position to center the value box on the value position
		xPos = Math.round(valPos - (boxWidth / 2)) + 'px';

	}
	else {
		var boxHeight = $valBox.outerHeight();

		xPos = $handle.css('left');

		// Adjust the vertical position to center the value box on the value position
		yPos = Math.round(valPos - (boxHeight / 2)) + 'px';
	}

	// Set the position of the value box
	$valBox.css('top', yPos);
	$valBox.css('left', xPos);

	// Set the text in the box to the handle value
	$valBox.text($handle.attr('aria-valuenow'));

} // end updateValBox()

/**
* @method bindHandlers
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to bind event handlers to a slider handle
*
* @param {obj} $handle - the object pointer of the handle to bind handlers to
*
* @return N/A
*/

OAA_EXAMPLES.slider.prototype.bindHandlers = function($handle) {

	var thisObj = this; // store the this pointer

	$handle.keydown(function(e) {
		return thisObj.handleKeyDown($handle, e);
	});

	$handle.keypress(function(e) {
		return thisObj.handleKeyPress($handle, e);
	});

	$handle.focus(function(e) {
		return thisObj.handleFocus($handle, e);
	});

	$handle.blur(function(e) {
		return thisObj.handleBlur($handle, e);
	});

	$handle.mousedown(function(e) {
		return thisObj.handleMouseDown($handle, e);
	});

} // end bindHandlers()

/**
* @method handleKeyDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keydown events for a slider handle
*
* @param {obj} $handle - the object associated with the event
*
* @param {obj} evt - the event object associated witthe the event
*
* @return {boolean} true if propagating; false if consuming event
*/

OAA_EXAMPLES.slider.prototype.handleKeyDown = function($handle, evt) {

	if (evt.ctrlKey || evt.shiftKey || evt.altKey) {
		// Do nothing
		return true;
	}

	switch (evt.keyCode) {
		case this.keys.home: {
			// move the handle to the slider minimum
			if (this.range == false) {
				this.positionHandle($handle, this.min);
			}
			else {
				if (/1$/.test($handle.attr('id')) == true) {
					// handle 1 - move to the min value
					this.positionHandle($handle, this.min);
				}
				else {
					// handle 2 - move to the position of handle 1
					this.positionHandle($handle, this.val1);
				}
			}
			evt.stopPropagation;
			return false;
			break;
		}
		case this.keys.end: {
			if (this.range == false) {
				// move the handle to the slider maximum
				this.positionHandle($handle, this.max);
			}
			else {
				if (/1$/.test($handle.attr('id')) == true) {
					// handle 1 - move to the position of handle 2
					this.positionHandle($handle, this.val2);
				}
				else {
					// handle 2 - move to the max value
					this.positionHandle($handle, this.max);
				}
			}
			evt.stopPropagation;
			return false;
			break;
		}
		case this.keys.pageup: {

			// Decrease by jump value

			var newVal = $handle.attr('aria-valuenow') - this.jump;
			var stopVal = this.min; // where to stop moving
			
			if (this.range == true) {
				// if this is handle 2, stop when we reach the value
				// for handle 1
				if (/2$/.test($handle.attr('id')) == true) {
					stopVal = this.val1;
				}
			}

			// move the handle one jump increment toward the slider minimum
			// If value is less than stopVal, set at stopVal instead
			this.positionHandle($handle, (newVal > stopVal ? newVal : stopVal));

			evt.stopPropagation;
			return false;
			break;
		}
		case this.keys.pagedown: {

			// Increase by jump value

			var newVal = parseInt($handle.attr('aria-valuenow')) + this.jump;
			var stopVal = this.max; // where to stop moving

			if (this.range == true) {
				// if this is handle 1, stop when we reach the value
				// for handle 2
				if (/1$/.test($handle.attr('id')) == true) {
					stopVal = this.val2;
				}
			}

			// move the handle one jump increment toward the slider maximum
			// If value is greater than maximum, set at maximum instead
			this.positionHandle($handle, (newVal < stopVal ? newVal : stopVal));

			evt.stopPropagation;
			return false;
			break;
		}
		case this.keys.left:
		case this.keys.up: { // decrement

			var newVal = $handle.attr('aria-valuenow') - this.inc;
			var stopVal = this.min; // where to stop moving
			
			if (this.range == true) {
				// if this is handle 2, stop when we reach the value
				// for handle 1
				if (/2$/.test($handle.attr('id')) == true) {
					stopVal = this.val1;
				}
			}

			// move the handle one jump increment toward the stopVal
			// If value is less than stopVal, set at stopVal instead
			this.positionHandle($handle, (newVal > stopVal ? newVal : stopVal));

			evt.stopPropagation;
			return false;
			break;
		}
		case this.keys.right:
		case this.keys.down: { // increment

			var newVal = parseInt($handle.attr('aria-valuenow')) + this.inc;
			var stopVal = this.max; // where to stop moving

			if (this.range == true) {
				// if this is handle 1, stop when we reach the value
				// for handle 2
				if (/1$/.test($handle.attr('id')) == true) {
					stopVal = this.val2;
				}
			}

			// move the handle one increment toward the slider maximum
			// If value is greater than maximum, set at maximum instead
			this.positionHandle($handle, (newVal < stopVal ? newVal : stopVal));

			evt.stopPropagation;
			return false;
			break;
		}
	} // end switch

	return true;

} // end handleKeyDown

/**
* @method handleKeyPress
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process keypress events for a slider handle. Needed for
* browsers that perform window scrolling on keypress rather than keydown events.
*
* @param {obj} $handle - the object associated with the event
*
* @param {obj} evt - the event object associated witthe the event
*
* @return {boolean} true if propagating; false if consuming event
*/

OAA_EXAMPLES.slider.prototype.handleKeyPress = function($handle, evt) {

	if (evt.ctrlKey || evt.shiftKey || evt.altKey) {
		// Do nothing
		return true;
	}

	switch (evt.keyCode) {
		case this.keys.home:
		case this.keys.pageup:
		case this.keys.end:
		case this.keys.pagedown:
		case this.keys.left:
		case this.keys.up:
		case this.keys.right:
		case this.keys.down: {

			// Consume the event
			evt.stopPropagation;
			return false;
			break;
		}
	} // end switch

	return true;

} // end handleKeyDown

/**
* @method handleFocus
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process focus events for a slider handle
*
* @param {obj} $handle - the object associated with the event
*
* @param {obj} evt - the event object associated with the event
*
* @return {boolean} true if propagating; false if consuming event
*/

OAA_EXAMPLES.slider.prototype.handleFocus = function($handle, evt) {

	$handle.attr('src', '{{EXAMPLE_MEDIA}}images/slider_' + (this.vert == true ? 'v' : 'h') + '-focus.png');
	$handle.addClass('focus');
	$handle.css('z-index', '20');

	return true;

} // end handleFocus()

/**
* @method handleBlur
*
* @member of OAA_EXAMPLES
*
* @param {obj} $handle - the object associated with the event
*
* @param {obj} evt - the event object associated witthe the event
*
* @return {boolean} true if propagating; false if consuming event
*/

OAA_EXAMPLES.slider.prototype.handleBlur = function($handle, evt) {

	$handle.attr('src', '{{EXAMPLE_MEDIA}}images/slider_' + (this.vert == true ? 'v' : 'h') + '.png');
	$handle.removeClass('focus');
	$handle.css('z-index', '10');

	return true;

} // end handleBlur()

/**
* @method handleMouseDown
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process mousedown events for a slider handle. The function
* binds a mousemove handler
*
* @param {obj} $handle - the object associated with the event
*
* @param {obj} evt - the event object associated witthe the event
*
* @return {boolean} true if propagating; false if consuming event
*/
OAA_EXAMPLES.slider.prototype.handleMouseDown = function($handle, evt) {

	var thisObj = this; // store the this pointer

	// remove focus highlight from all other slider handles on the page
	$('.hsliderHandle').attr('src', '{{EXAMPLE_MEDIA}}images/slider_h.png').removeClass('focus').css('z-index', '10');
	$('.vsliderHandle').attr('src', '{{EXAMPLE_MEDIA}}images/slider_v.png').removeClass('focus').css('z-index', '10');

	// Set focus to the clicked handle
	$handle.focus();

	// bind a mousemove event handler to the document to capture the mouse
	$(document).mousemove(function(e) {
		thisObj.handleMouseMove($handle, e);
	});

	//bind a mouseup event handler to the document to capture the mouse
	$(document).mouseup(function(e) {
		return thisObj.handleMouseUp($handle, e);
	});

	evt.stopPropagation;
	return false;

} // end handleMouseDown()

/**
* @method handleMouseUp
*
* @memberOf OAA_EXAMPLES
*
* @desc a member function to process mouseup events for a slider handle. The function
* unbinds the mousemove handler
*
* @param {obj} $handle - the object associated with the event
*
* @param {obj} evt - the event object associated witthe the event
*
* @return {boolean} true if propagating; false if consuming event
*/

OAA_EXAMPLES.slider.prototype.handleMouseUp = function($handle, evt) {

	// unbind the event listeners to release the mouse
	$(document).unbind('mousemove');
	$(document).unbind('mouseup');

	evt.stopPropagation;
	return false;

} // end handleMouseUp()

/**
* @method handleMouseMove
*
* @memberOf OAA_EXAMPLES
* @desc a member function to process mousemove events for a slider handle.
*
* @param {obj} $handle - the object associated with the event
*
* @param {obj} evt - the event object associated witthe the event
*
* @return {boolean} true if propagating; false if consuming event
*/

OAA_EXAMPLES.slider.prototype.handleMouseMove = function($handle, evt) {

	var curVal = parseInt($handle.attr('aria-valuenow'));
	var newVal;
	var startVal = this.min;
	var stopVal = this.max;

	if (this.range == true) {
		// if this is handle 1, set stopVal to be the value
		// for handle 2
		if (/1$/.test($handle.attr('id')) == true) {
			stopVal = this.val2;
		}
		else {
			// This is handle 2: Set startVal to be the value
			// for handle 1
			startVal = this.val1;
		}
	}

	if (this.vert == false) {
		// horizontal slider

		// Calculate the new slider value based on the horizontal pixel position of the mouse
		newVal = Math.round((evt.pageX - this.left) / this.width * (this.max - this.min)) + this.min;
	}
	else {
		// vertical slider

		// Calculate the new slider value based on the vertical pixel position of the mouse
		newVal = Math.round((evt.pageY - this.top) / this.height * (this.max - this.min)) + this.min;
	}

	if (newVal >= startVal && newVal <= stopVal) {

		// Do not move handle unless new value is a slider increment
		if (newVal%this.inc == 0) {
			this.positionHandle($handle, newVal);
		}
	}
	else if (newVal < startVal) {

		// value is less than minimum for slider - set handle to min
		this.positionHandle($handle, startVal);
	}
	else if (newVal > stopVal) {

		// value is greater than maximum for slider - set handle to max
		this.positionHandle($handle, stopVal);
	}

	evt.stopPropagation;
	return false;

} // end handleMouseMove
"""

example_info.style       = """
/* CSS Document */

.label {
  margin: 0;
  padding: 0;
  margin-top: 2em;
  margin-bottom: .5em;  
  clear: both;
  font-weight: bold;
}

div.hslider {
  margin: 50px;
  padding: 0;
  width: 540px;
  height: 20px;
  background-color: #eef;
  border: 2px solid black;
}

.hsliderHandle  {
  margin: 0;
  padding: 7px 2px;
  width: 24px;
  height: 12px;
  background-color: #808080;

  position: absolute;
  left: -300em;
  top: -30em;
  z-index: 10;

  border: 1px solid black;
  -webkit-border-radius: 5px; /* Safari and Chrome rounded corners */
  -moz-border-radius: 5px; /* Firefox rounded corners */
  border-radius: 5px; /* Opera rounded corners */ 

}

.hsliderValue  {
  margin: 24px 0 0 0;
  padding: 5px;
  width: 30px;
  height: 15px;
  text-align: center;
  font-weight: bold;

  position: absolute;
  left: -30em;
  top: -30em;
  z-index: 10;
}

div.vslider {
  margin: 50px;
  padding: 0;
  height: 540px;
  width: 20px;
  background-color: #eef;
  border: 2px solid black;
}

.vsliderHandle  {
  margin: 0;
  padding: 2px 7px;
  width: 12px;
  height: 24px;
  background-color: #808080;

  position: absolute;
  left: -300em;
  top: -30em;
  z-index: 10;

  border: 1px solid black;
  -webkit-border-radius: 5px; /* Safari and Chrome rounded corners */
  -moz-border-radius: 5px; /* Firefox rounded corners */
  border-radius: 5px; /* Opera rounded corners */ 
}

.vsliderValue  {
  margin: 0 0 0 30px;
  padding: 5px;
  width: 30px;
  height: 15px;
  text-align: center;
  font-weight: bold;

  position: absolute;
  left: -30em;
  top: -30em;
  z-index: 10;
}

div.sliderRange {
  margin: 2px;
  padding: 0;
  width: 1px;
  height: 1px;
  background-color: #00f;

  position: absolute;
  left: -300em;
  top: -30em;
  z-index: 0;
}

.hidden {
  position: absolute;
  top: -20em;
  left: -200em;
}

.focus {
  background-color: #eee !important;
}
"""

example1 = create_example(example_info)

ExampleScriptReference.objects.filter(example=example1).delete()
script1      = ExampleScript.objects.get(script='examples/js/jquery-1.4.2.min.js')
add_script_reference( example1, script1 )

ExampleGroup.objects.get(slug='aria-range').examples.add(example1)

