from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
def killer_view(request):
    user = request.user
    # return HttpResponse("欢迎%s"%(user.username))
    list = ["GPS","屏","指纹","性能","相机","通话","电池","wifi","蓝牙"]
    return render(request, 'killer/killer.html',{"username":user,"module_list":list})
