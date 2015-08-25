from django.db import models
from django.forms import ModelForm
from examples.models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class RuleReferenceCreationForm(ModelForm):
  class Meta:
    model = ExampleRuleReference
    exclude = ['note', 'note_html', 'rule']
