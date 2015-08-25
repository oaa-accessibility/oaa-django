"""
Views which allow users to create and activate accounts.

"""
from django.contrib.auth.decorators import user_passes_test
from django.template  import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from registration import signals
from coding import settings, settings_local
from registration.forms import RegistrationForm, UserForm
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from users.models import Organization

class _RequestPassingFormView(FormView):
    """
    A version of FormView which passes extra arguments to certain
    methods, notably passing the HTTP request nearly everywhere, to
    enable finer-grained processing.
    
    """
    def get(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        if form.is_valid():
            # Pass request to form_valid.
            return self.form_valid(request, form)
        else:
            return self.form_invalid(form)

    def get_form_class(self, request=None):
        return super(_RequestPassingFormView, self).get_form_class()

    def get_form_kwargs(self, request=None, form_class=None):
        return super(_RequestPassingFormView, self).get_form_kwargs()

    def get_initial(self, request=None):
        return super(_RequestPassingFormView, self).get_initial()

    def get_success_url(self, request=None, user=None):
        # We need to be able to use the request and the new user when
        # constructing success_url.http://www.robgolding.com/blog/2012/07/12/django-class-based-view-mixins-part-1/
        return super(_RequestPassingFormView, self).get_success_url()

    def form_valid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_valid(form)

    def form_invalid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_invalid(form)


class StaffRequiredMixin(object):
  """
  View mixin which requires that the authenticated user is a staff member
  (i.e. `is_staff` is True).
  """
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_superuser:
      return redirect('/')
    return super(StaffRequiredMixin, self).dispatch(request,
      *args, **kwargs)


class RegistrationView(StaffRequiredMixin, _RequestPassingFormView):
    """
    Base class for user registration views.
    
    """
    disallowed_url = 'registration_disallowed'
    form_class = RegistrationForm
    http_method_names = ['get', 'post', 'head', 'options', 'trace']
    success_url = None
    template_name = 'registration/registration_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        """
        Check that user signup is allowed before even bothering to
        dispatch or do other processing.
        
        """


        if not self.registration_allowed(request):
            return redirect(self.disallowed_url)
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, request, form):
        new_user = self.register(request, **form.cleaned_data)
        success_url = self.get_success_url(request, new_user)
        
        # success_url may be a simple string, or a tuple providing the
        # full argument set for redirect(). Attempting to unpack it
        # tells us which one it is.
        try:
            to, args, kwargs = success_url
            return redirect(to, *args, **kwargs)
        except ValueError:
            return redirect(success_url)

    def registration_allowed(self, request):
        """
        Override this to enable/disable user registration, either
        globally or on a per-request basis.
        
        """
        return True

    def register(self, request, **cleaned_data):
        """
        Implement user-registration logic here. Access to both the
        request and the full cleaned_data of the registration form is
        available here.
        
        """
        raise NotImplementedError
                

class ActivationView(TemplateView):
    """
    Base class for user activation views.
    
    """
    http_method_names = ['get']
    template_name = 'registration/activate.html'

    def get(self, request, *args, **kwargs):
        activated_user = self.activate(request, *args, **kwargs)
        if activated_user:
            signals.user_activated.send(sender=self.__class__,
                                        user=activated_user,
                                        request=request)
            success_url = self.get_success_url(request, activated_user)
            try:
                to, args, kwargs = success_url
                return redirect(to, *args, **kwargs)
            except ValueError:
                return redirect(success_url)
        return super(ActivationView, self).get(request, *args, **kwargs)

    def activate(self, request, *args, **kwargs):
        """
        Implement account-activation logic here.
        
        """
        raise NotImplementedError

    def get_success_url(self, request, user):
        raise NotImplementedError

def set_organization(new_user, organization):
  if Organization.objects.filter(title = organization):
    userOrganization = Organization.objects.get(title = organization)
    userOrganization.users.add(new_user)
    userOrganization.save()
    return userOrganization
  else:
    userOrganization = Organization.objects.create(title = organization)
    userOrganization.users.add(new_user)
    userOrganization.save()
    return userOrganization

@login_required
def changeUser(request):
  user = request.user
  if request.POST:
    form = UserForm(request.POST, instance = user)
    if form.is_valid():
      form.save()
      user.username = user.email
      user.is_active = True
      organization = set_organization(user, form.cleaned_data['organization'])
      user.organization_set.clear()
      user.organization_set.add(organization)
      user.save()
      return HttpResponseRedirect("/")
  else:
    organization = user.organization_set.all()
    form = UserForm(instance = user)
    if organization:    
      organization = organization[0]
      form.fields['organization'].initial = organization.title
    
  return render_to_response("registration/edit_user.html", {
    'form': form
  },context_instance=RequestContext(request))   
  
  
  
