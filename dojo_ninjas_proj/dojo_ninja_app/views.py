from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def method1(request):
    context={
        'alldojos':Dojo.objects.all(),
    }
    return render(request,"form.html",context)
def method2(request):
    Dojo.objects.create(name=request.POST['dname'])
    return redirect("/")

def method3(request):
    Ninja.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'] ,dojo=Dojo.objects.get(id=request.POST['dojo']))
    return redirect("/")