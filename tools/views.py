from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from tools.models import Tool

from breadCrumbs   import breadCrumbs

  

def tool(request, tool_slug):
   tool  = Tool.objects.get(tool_slug=tool_slug)
   tools = Tool.objects.all()

   request.session['oaa_bread_crumb_1_title'] = tool.title
   request.session['oaa_bread_crumb_1_url']   = reverse('show_tool', args=(tool.tool_slug,))   
   request.session['oaa_bread_crumb_2_title'] = ''
   request.session['oaa_bread_crumb_2_url']   = ''
   request.session['oaa_bread_crumb_3_title'] = ''
   request.session['oaa_bread_crumb_3_url']   = ''      

   request.session['oaa_main_tools_url'] = reverse('show_tool', args=(tool.tool_slug,))   
      
   return render_to_response('tools/tool.html',{
      'title'        : tool.title,
      'main'         : 'tools',
      'tool'         : tool,
      'tools'        : tools,
      'bread_crumbs' : breadCrumbs(request),
   },context_instance=RequestContext(request))
