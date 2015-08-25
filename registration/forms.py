"""
Forms and validation code for user registration.

Note that all of these forms assume Django's bundle default ``User``
model; since it's not possible for a form to anticipate in advance the
needs of custom user models, you will need to write your own forms if
you're using a custom model.

"""


from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.forms import PasswordInput
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import check_password


class RegistrationForm(forms.Form):
    """
    Form for registering a new user account.
    
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    required_css_class = 'required'
    email = forms.EmailField(label=_("E-mail"))
    first = forms.CharField(label=_("first"))
    last = forms.CharField(label=_("last"))
    organization = forms.CharField(label=_("organization"))    

    options = [('rules',"Rules"),('examples', "Examples"), ('testers', "Testers")]
    permissions = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=options, required=False)

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data


class RegistrationFormTermsOfService(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.
    
    """
    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_(u'I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})


class RegistrationFormUniqueEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.
    
    """
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which disallows registration with
    email addresses from popular free webmail services; moderately
    useful for preventing automated spam registrations.
    
    To change the list of banned domains, subclass this form and
    override the attribute ``bad_domains``.
    
    """
    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']
    
    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.
        
        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        return self.cleaned_data['email']
        
        
        
class ActivationForm(forms.Form):
    """
    Form for activating user accounts. 
    
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    required_css_class = 'required'
    email = forms.EmailField(label=_("E-mail"))
    first = forms.CharField(label=_("first"))
    last = forms.CharField(label=_("last"))
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    organization = forms.CharField(label=_("organization"))    

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data
        
        
class UserForm(ModelForm):
  organization = forms.CharField()

  class Meta:
    model = User
    include = ['email', 'first_name', 'last_name'] 
    exclude = ['password', 'last_login', 'date_joined', 'username', 'is_active']    
"""        
        
class UserForm(forms.Form):
    email = forms.EmailField(label=_("E-mail"))
    first_name = forms.CharField(label=_("first"))
    last_name = forms.CharField(label=_("last"))
    passwordOld = forms.CharField(widget=PasswordInput(), label=_("old_password"),required=True)
    passwordNew1 = forms.CharField(widget=PasswordInput(), label=_("new_password1"),required=False)
    passwordNew2 = forms.CharField(widget=PasswordInput(), label=_("new_password2"),required=False)
    
    def clean_old_password(self, user):
      if check_password(self.cleaned_data['passwordOld'], user.password):
        return self.cleaned_data['passwordOld']
      else:
        raise forms.ValidationError(_("Your old password is incorrect"))
      
    def clean_username(self):
"""
"""
        Validate that the username is alphanumeric and is not already
        in use.
"""        
"""
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that email already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
"""
"""
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
"""        
"""
        if 'passwordNew1' in self.cleaned_data and 'passwordNew2' in self.cleaned_data:
            if self.cleaned_data['passwordNew1'] != self.cleaned_data['passwordNew2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data
"""
