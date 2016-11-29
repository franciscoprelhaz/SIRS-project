from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
#login required is to not allow any non authenticated views
@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")
