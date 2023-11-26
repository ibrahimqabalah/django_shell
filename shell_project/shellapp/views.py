from django.shortcuts import render,HttpResponse,redirect
from .models import user
# Create your views here.
def method1(request):
    context={
        'allusers':user.objects.all(),
        }
    return render(request,"user.html",context)

def method2(request):
    user.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],age=request.POST['age'] )
    return redirect("/")

