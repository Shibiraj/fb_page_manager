import json, requests
from django.http import HttpResponse
from fb_app.utils import FacebookPageManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # Home page of the application
    social_user = request.user.social_auth.filter(provider='facebook', ).first() 
    access_token = social_user.extra_data['access_token']
    fb_page_manager = FacebookPageManager(access_token)
    page_info = fb_page_manager.get_page_info()
    return render(request, 'fb_app/home.html', context=page_info)

@login_required
def update_page_info(request):
    # Updates the page information
    if request.method == 'POST':
        social_user = request.user.social_auth.filter(provider='facebook', ).first() 
        access_token = social_user.extra_data['access_token']
        fb_page_manager = FacebookPageManager(access_token)
        data = fb_page_manager.update_page_info(request.POST)
        return HttpResponse(json.dumps({'success' : 1 if data.get('success') else 2}), content_type="application/json")
