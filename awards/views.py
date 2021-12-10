from django.shortcuts import render,redirect
from .models import Profile,Project
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,'all-awards/index.html')
    
@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    # project = Project.objects.filter(user_id=current_user.id)

    return render(request,"profile.html",{'profile':profile})




