from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def login(request, err_msg=''):
    return render(request, "test_site/login.html", context={"err_msg": err_msg})

def home(request):
    print(request.GET)
    auth = False
    email = 'be07724@st.habib.edu.pk'
    username = request.GET.get('uname')
    password = request.POST.get('psw')
    print(username,password)
    if username == 'admin': #and password == 'admin':
        auth = True
    if auth == True:
        return render(request, "test_site/home.html", context={"username": username, "email": email})
    else:
        return redirect('login')
    # return HttpResponseRedirect(reverse('login', args=("Login Failed",)))    

def insights(request):
    return HttpResponse('This is the insights page')

def tasks(request):
    return HttpResponse('This is the tasks page')

def projects(request):
    return HttpResponse('This is the projects page')