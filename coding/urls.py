from django.conf.urls import patterns, include, url
from django.contrib import admin
#from users.forms import RegistrationFormExtended
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Home
    url(r'^$',                                'abouts.views.home',             name='show_home'),
        
    # Ruleset and Rule Views
    url(r'^rulesets/$',                         'rulesets.views.show',          name='show_rulesets'),
    url(r'^ruleset/(?P<ruleset_slug>[\w-]+)/$', 'rulesets.views.ruleset',       name='show_ruleset'),
    url(r'^ruleset/rule/(?P<rule_id>[\w-]+)/$', 'rulesets.views.rule',          name='show_rule'),
    url(r'^rulesets/rule_category/$',           'rulesets.views.rule_category', name='show_rulesets_rule_category'),
    url(r'^rulesets/wcag20/$',                  'rulesets.views.wcag20',        name='show_rulesets_wcag20'),
    url(r'^rulesets/scope/$',                   'rulesets.views.scope',         name='show_rulesets_scope'),

    # Example Views
    url(r'^examples/$',                                     'examples.views.ruleCategories', name='show_examples'),
    url(r'^example_rc/(?P<rule_category_slug>[\w-]+)/$',    'examples.views.ruleCategory',   name='show_examples_for_rule_category'),
    url(r'^example_group/(?P<example_group_slug>[\w-]+)/$', 'examples.views.exampleGroup',   name='show_examples_for_example_group'),
    url(r'^example/(?P<example_id>[\w-]+)/$',               'examples.views.example',        name='show_example'),
    
    url(r'^examplep/(?P<example_slug>[\w-]+)/$', 'examples.views.examplePermanent', name='show_example_permanent'),
    
    # Markup Views
    url(r'^markup/(?P<url_slug>[\w-]+)/$',      'markup.views.specfication',     name='show_markup'),

    # Tool Views
    url(r'^tools/(?P<tool_slug>[\w-]+)/$',    'tools.views.tool',              name='show_tool'),
    
    # About Views
    url(r'^abouts/(?P<about_slug>[\w-]+)/$',  'abouts.views.about',            name='show_about'),
    
    # User Views
    url(r'^login/$',  'django.contrib.auth.views.login',                       name='login'),
    url(r'^logout/$',  'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^permission_denied/$',  'users.views.denied', name='denied'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
)
