from django.db import models
from django import forms
from django.contrib.auth.models import User, Group, Permission
from registration.forms import RegistrationForm
from models import UserProfile
from registration.models import RegistrationProfile
# Create your models here.

class RegistrationFormExtended(RegistrationForm):
  organization = forms.CharField(required=True)

  def save(self, commit=True):
    new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['username'], password=self.cleaned_data['password1'],email=self.cleaned_data['email'])
    new_profile = UserProfile(user = new_user, organization = self.cleaned_data['organization'])
    new_profile.save()
    return new_profile
    
    
"""
  OPTIONS = [('rules',"Rules"),('examples', "Examples"),('javascripting', "JavaScripting"),('testing', "Testing"),('commenting', "Commenting")]
  permissions = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=OPTIONS, required=False)
  class Meta:
    model = User
    fields = ["username", "email", "first", "last", "password1", "password2", "organization", "permissions"]
    
    
    if self.cleaned_data["permissions"]:
      for value in self.cleaned_data["permissions"]:
        if value == 'rules':
          rule_group = Group.objects.get(name='Rule Editors')
          rule_group.user_set.add(user)
        if value == 'examples':
          rule_group = Group.objects.get(name='Example Editors')
          rule_group.user_set.add(user)
        if value == 'javascripting':
          rule_group = Group.objects.get(name='Rule Coders')
          rule_group.user_set.add(user)
        if value == 'testing':
          rule_group = Group.objects.get(name='Testers')
          rule_group.user_set.add(user)
        if value == 'commenting':
          rule_group = Group.objects.get(name='Commenters')
          rule_group.user_set.add(user)
    user.is_active = False
"""
