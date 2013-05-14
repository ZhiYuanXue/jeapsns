from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.template import Template, Context
from django.shortcuts import render_to_response
from jeapsns.forms import *
from jeapsns.models import *
from django.template import RequestContext

from django.contrib.auth.forms import *

from django.contrib import admin
from jeapsns.models import content
admin.site.register(Pub)
admin.site.register(content)


def register(request,template_name):
	form = UserCreationForm()
	if request.method == 'GET':
		return render_to_response(template_name,{'form':form},context_instance=RequestContext(request))
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
		return HttpResponseRedirect("/")

def index_temp_file(request,color):
	f = PuForm()
	all = Pub.objects.all()
	return render_to_response('index_temp_file.html', {'all':all,'f':f},context_instance=RequestContext(request))


def index_save(request):
	if request.method == 'POST':
		a = Content()
		for n in request.POST.keys():
			if hasattr(a,n):
				setattr(a,n,request.POST[n])
		a.save()
        print a.text
	return HttpResponseRedirect('') 

def index_delete(request,id):
	a = Pub.objects.get(id=id)
	a.delete()
	return HttpResponseRedirect('/index_temp_file/32') 


def index_edit(request,id):
	if request.method == 'POST':
		a = Pub()
		for n in request.POST.keys():
			if hasattr(a,n):
				setattr(a,n,request.POST[n])
		a.id = id
		a.save()
		return HttpResponseRedirect('/index_temp_file/32') 
		
	a = Pub.objects.get(id=id)
	d = {}
	for n in a._meta.fields:
		d[n.name]=getattr(a,n.name)
	f = PuForm(d)
	return render_to_response('index_edit.html', {'f':f,'id':id},context_instance=RequestContext(request))
 


def index_temp(request,input_name,color):
	t = Template('My name is <font color=#{{c}}> {{ name }} </font>.')
	c = Context({'name': input_name,'c':color})
	return HttpResponse(t.render(c))

def hello(request):
	if 'q' in request.GET:
		message = "You input :%r"% request.GET['q']
	return HttpResponse(message)

def index(request):
	if request.user.is_authenticated():
		name = request.user.username
	contents = content.objects.all()
	return render_to_response('index.html',{'contents':contents},context_instance=RequestContext(request))

def current_time(request,s,offset):
	offset = int(offset)
	if s == 'get':
		dt = datetime.datetime.now()
		return HttpResponse("current_time !<h1>%s</h1><h1>%s</h1>"%(offset,dt))

	return HttpResponse("current_time !<h1>%s</h1><h1>%s</h1>"%(offset,s))
