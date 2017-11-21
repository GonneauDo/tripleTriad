from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

def post_list(request):
	return render(request, 'index.html')

def index(request):
	return render_to_response("index/index/html", context_instance=RequestContext(request))
