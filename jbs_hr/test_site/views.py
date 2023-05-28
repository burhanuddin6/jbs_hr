from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
    # proper method
    # template = loader.get_template("test_site/index.html")
    # context = {}
    # return HttpResponse(template.render(context, request))
    
    # shortcut method:
    return render(request, "test_site/index.html", context={})

def home(request):
    auth = False
    username = 'admin' #request.GET.get('uname','')
    password = 'admin' #request.POST.get('psw','')
    if username == 'admin' and password == 'admin':
        auth = True
    if auth:
        return render(request, "test_site/home.html", context={})
    else:
        return request
    

def insights(request):
    return HttpResponse('This is the insights page')

def tasks(request):
    return HttpResponse('This is the tasks page')

def projects(request):
    return HttpResponse('This is the projects page')