from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from . import models
# Create your views here.
def login_view(request):
    if request.method=='GET':
        return render(request,'useradmin/login.html')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if not user:
            message = "用户名或密码错误!"
            return render(request,'useradmin/login.html',{'error_msg':message})
        else:
            login(request,user)
            return HttpResponseRedirect('/killer/killer')
        pass


