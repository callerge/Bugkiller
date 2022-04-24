from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
            return HttpResponse("--成功--")
            # return HttpResponseRedirect('/index')
        pass
#
# @login_required
# def index_view(request):
#     #未登录则跳转至settings.LOGIN_URL
#     user=request.user
#     return HttpResponse('欢迎 %s'%(user.username))


