from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
def killer_view(request):
    user = request.user
    # return HttpResponse("欢迎%s"%(user.username))
    return render(request, 'killer/killer.html')
