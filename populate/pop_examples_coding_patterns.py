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

rc = RuleCategory.objects.get(slug='forms')

eg_basic_labeling = create_example_group(rc, 'label_basic', 'Basic HTML form control labeling', 'Shows labeling options for standard HTML form controls and describe the features of each technique from an accessibility and usability perspective.')
eg_unique_names   = create_example_group(rc, 'label_unique', 'Unique accessible names for form controls', 'Shows techniques that can be used to make unique accessible names for HTML form controls that share the same label text')

rc = RuleCategory.objects.get(slug='widgets')
eg_dialog_boxes   = create_example_group(rc, 'dialog_boxes', 'Dialog and Alert Boxes', 'Shows techniques for creating ARIA enabled diaplog and alert boxes')
eg_check_boxes    = create_example_group(rc, 'check_boxes', 'Checkboxes', 'Shows techniques for creating ARIA enabled Check Boxes')
eg_combo_boxes    = create_example_group(rc, 'combo_boxes', 'Combo Boxes', 'Shows techniques for creating ARIA enabled Combo Boxes')
eg_tooltip        = create_example_group(rc, 'tooltip', 'Tooltips', 'Shows techniques for creating ARIA enabled Tooltips')
eg_visibility     = create_example_group(rc, 'visibility', 'Tabpanels and Hide/Show', 'Shows techniques for creating ARIA enabled Tabpanels and Hide/Show widgets')
eg_trees          = create_example_group(rc, 'trees', 'Treeviews', 'Shows techniques for creating ARIA enabled Treeviews')
eg_slide          = create_example_group(rc, 'slide', 'Sliders and Spinbuttons', 'Shows techniques for creating ARIA enabled Sliders and Spinbuttons')
eg_rss            = create_example_group(rc, 'rss', 'RSS feeds', 'Shows techniques for creating ARIA enabled RSS feeds')
eg_carousel       = create_example_group(rc, 'carousel', 'Image Carousels', 'Shows techniques for creating Image carousels')

