import sys,os
sys.path.append(os.path.abspath('..'))

from django.core.management import setup_environ 
import coding.settings as settings
setup_environ(settings)

from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.backends import ModelBackend
from django.contrib.contenttypes.models import ContentType
###################################################Create Example Editors######################################################################################################

from examples.models import Example, ExampleGroup
from markup.models import ElementDefinition, LanguageSpec

example_editors = Group(name="example_editors")
example_editors.save()
content_type = ContentType.objects.get_for_model(Example)
permissionsExample = Permission.objects.filter(content_type=content_type)
content_type = ContentType.objects.get_for_model(LanguageSpec)
permissionsSpec = Permission.objects.filter(content_type=content_type)
content_type = ContentType.objects.get_for_model(ElementDefinition)
permissionsElementDefinition = Permission.objects.filter(content_type=content_type)
content_type = ContentType.objects.get_for_model(ExampleGroup)
permissionsExampleGroup = Permission.objects.filter(content_type=content_type)
example_editors.permissions.add(permissionsExample[0], permissionsExample[1],permissionsSpec[0],permissionsSpec[1],permissionsElementDefinition[0], permissionsElementDefinition[1], permissionsExampleGroup[0], permissionsExampleGroup[1])
example_editors.save()

###################################################Create Rule Editors######################################################################################################

from rules.models import Rule, InformationalLink
from manualChecks.models import ManualCheck
from techniques.models import Technique

rule_editors = Group(name="rule_editors")
rule_editors.save()
content_type = ContentType.objects.get_for_model(Rule)
permissionsRule = Permission.objects.filter(content_type=content_type)
content_type = ContentType.objects.get_for_model(ManualCheck)
permissionsManualCheck = Permission.objects.filter(content_type=content_type)
content_type = ContentType.objects.get_for_model(Technique)
permissionsTechnique = Permission.objects.filter(content_type=content_type)
content_type = ContentType.objects.get_for_model(InformationalLink)
permissionsInformationalLink = Permission.objects.filter(content_type=content_type)
rule_editors.permissions.add(permissionsRule[0], permissionsRule[1],permissionsManualCheck[0],permissionsManualCheck[1],permissionsTechnique[0], permissionsTechnique[1], permissionsInformationalLink[0], permissionsInformationalLink[1])
rule_editors.save()

###################################################Create Testers######################################################################################################

from examples.models import ExampleCompatibility, ExampleUserAgent

test_editors = Group(name="testers")
test_editors.save()
content_type = ContentType.objects.get_for_model(ExampleCompatibility)
permissionsExampleCompatibility = Permission.objects.filter(content_type=content_type)
content_type = ContentType.objects.get_for_model(ExampleUserAgent)
permissionsUserAgent = Permission.objects.filter(content_type=content_type)
test_editors.permissions.add(permissionsExampleCompatibility[0], permissionsExampleCompatibility[1],permissionsUserAgent[0],permissionsUserAgent[1])
test_editors.save()
