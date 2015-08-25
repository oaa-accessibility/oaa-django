from django.shortcuts         import render, render_to_response, HttpResponseRedirect
from django.http              import HttpResponse, Http404
from django.template          import RequestContext
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

   
def denied(request):
  return render(request, "users/denied.html", {
  })
   
class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

