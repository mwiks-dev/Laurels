from django.shortcuts import render,redirect
from .models import Profile,Project
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostProjectForm



# Create your views here.
def index(request):
    project = Project.objects.all().order_by('-id')
    return render(request,'all-awards/index.html',{'project':project})
    
@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)

    return render(request,"all-awards/index.html",{'profile':profile,'project':project})

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)

    return render(request,"profile.html",{'profile':profile,'project':project})

@login_required(login_url='/accounts/login/')
def upload_project(request):
    if request.method == "POST":
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form = PostProjectForm()
    return render(request, 'upload_project.html', {"form": form})


