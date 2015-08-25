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

from examples.models       import ExampleImage, ExampleObject, ExampleStyle, ExampleScript
from examples.models       import Example
from examples.models       import ExampleGroup
from ruleCategories.models import RuleCategory


# =============================
# Clear example database
# =============================

ExampleImage.objects.all().delete()
ExampleObject.objects.all().delete()
ExampleStyle.objects.all().delete()
ExampleScript.objects.all().delete()
ExampleGroup.objects.all().delete()
Example.objects.all().delete()
