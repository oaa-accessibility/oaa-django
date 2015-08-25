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

from examples.models import Example, ExampleGroup
from ruleCategories.models import RuleCategory

# =============================
# Initial codingPatterns
# =============================

rc = RuleCategory.objects.get(slug='structure')
eg_headings  = create_example_group(rc,  1, 'headings',  'Using @h1-h6@ to identify sections and sub sections of a web page', '')
eg_landmarks = create_example_group(rc,  2, 'landmarks', 'Using ARIA landmarks to identify sections of a web page', '')
eg_html5s    = create_example_group(rc,  3, 'html5s',    'HTML 5 section elements and accessibility', '')
eg_valid     = create_example_group(rc,  4, 'valid',     'Using valid HTML markup', '')

rc = RuleCategory.objects.get(slug='images')
eg_informative = create_example_group(rc,  1, 'informative',  'Text alternatives for informative images', '')
eg_decorative = create_example_group(rc,  2, 'decorative',    'Alternatives to using images for styling, positioning and decoration', '')

rc = RuleCategory.objects.get(slug='forms')
eg_labeling = create_example_group(rc,  1, 'labeling',  'Basic form control labeling techniques', 'labeling options for standard HTML form controls and describe the features of each technique from an accessibility and usability perspective.')
eg_checkbox = create_example_group(rc,  2, 'checkbox',  'Checkbox labeling and focus styling', 'Labeling and focus styling options for standard HTML checkbox controls.')
eg_radio    = create_example_group(rc,  3, 'radio',     'Radio button group labeling and focus styling', 'Labeling and focus styling options for standard HTML radio button controls.')
eg_unique   = create_example_group(rc,  4, 'unique',    'Insuring form controls have unique and meaningful labels', 'Shows techniques that can be used to make unique accessible names for HTML form controls that share the same label text')
eg_errors   = create_example_group(rc,  5, 'errors',    'Providing accessible error correction feedback', 'Shows techniques that can be used to to make error validation and reporting accessible')
eg_html5f   = create_example_group(rc,  6, 'html5f',    'Accessibility features of HTML 5 form controls', 'Shows HTML 5 techniques that can be used to form controls accessible')
eg_misc   = create_example_group(rc,  7, 'misc',    'Miscellaneous', '')


rc = RuleCategory.objects.get(slug='tables')
eg_dtables = create_example_group(rc,  1, 'dtables',  'Data Table Accessibility Markup', '')
eg_ltables = create_example_group(rc,  2, 'ltables',  'Layout Table Accessibility Markup', '')
eg_mtables = create_example_group(rc,  3, 'mtables',  'Data Tables nested in Layout Tables', '')

rc = RuleCategory.objects.get(slug='links')
eg_links   = create_example_group(rc,  1, 'links',   'Techniques to define accessible name for a link', '')
eg_context = create_example_group(rc,  2, 'context', 'Providing context to links that share the same link text', '')

rc = RuleCategory.objects.get(slug='navigation')
eg_multiple   = create_example_group(rc,  1, 'multiple',    'Multiple ways to find content', '')
eg_consistent = create_example_group(rc,  2, 'consistent',  'Consistent ordering and labeling', '')

rc = RuleCategory.objects.get(slug='keyboard')
eg_focus = create_example_group(rc,  1, 'focus',   'Keyboard focus styling', '')
eg_tabbing = create_example_group(rc,  2, 'tabbing', 'Links, form controls and widgets are in an effecient and logical tab order', '')
eg_widgets = create_example_group(rc,  3, 'widgets', 'Keyboard support for accessible widgets', '')

rc = RuleCategory.objects.get(slug='media')
eg_video = create_example_group(rc,  1, 'video',     'Captioning and descriptions for Video', '')
eg_audio = create_example_group(rc,  2, 'audio',     'Captioning and text transcripts for Audio', '')
eg_animation = create_example_group(rc,  3, 'animation',      'Animated graphics and text', '')

rc = RuleCategory.objects.get(slug='styling')
eg_dorder = create_example_group(rc,  1, 'dorder',  'Document Order', '')
eg_ccr    = create_example_group(rc,  2, 'ccr',     'Color Contrast of Text', '')
eg_color  = create_example_group(rc,  3, 'color',   'Converying information using more than just color', '')

rc = RuleCategory.objects.get(slug='widgets')
create_example_group(rc,  1, 'hideshow',        'Dynamic techniques to show and hide content', '')
create_example_group(rc,  2, 'dmenu',           'Pull down and popup menus', '')
create_example_group(rc,  3, 'carousels',       'Carousels for rotating pictures and scrolling news on a website', '')
create_example_group(rc,  4, 'aria-dialogbox',  'Modal dialog and alert boxes', '')
create_example_group(rc,  4, 'editors',         'WYSIWYG editors for inline editing of web pages and wikis', '')
create_example_group(rc,  5, 'aria-checkbox',   'Custom checkboxes', '')
create_example_group(rc,  6, 'aria-radio',      'Custom radio buttons and radio groups', '')
create_example_group(rc,  7, 'aria-combobox',   'Comboboxes', '')
create_example_group(rc,  8, 'aria-tooltip',    'Tooltips for more information', '')
create_example_group(rc,  9, 'aria-toolbar',    'Toolbars for a group of buttons and selection boxes', '')
create_example_group(rc, 10, 'aria-tabpanel',   'Tab panel widgets', '')
create_example_group(rc, 11, 'aria-tree',       'Tree widgets', '')
create_example_group(rc, 12, 'aria-range',      'Sliders, spinbuttons and other range controls', '')
create_example_group(rc, 13, 'aria-live',       'Live regions for asynchonously dynamically changing content', '')
create_example_group(rc, 14, 'misc',   'miscellaneous widgets ', '')
