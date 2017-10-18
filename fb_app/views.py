from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    print(request.user)
    print(dir(request.user))
    return render(request, 'fb_app/home.html')