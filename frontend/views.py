from django.shortcuts import render


# my views 
from .models import SliderImage,Event
from .forms import ProjectForm
# Create your views here.

def home_view(request):
    slider_image = SliderImage.objects.all()[:3]
    context = {
        'slider': slider_image,
        'active': True,
    }
    return render(request,'frontend/home.html',context) 

def event_view(request):
    event_list = Event.objects.all()
    context = {
        'event_list': event_list,
        'active': True,
    }
    return render(request,'frontend/event.html',context) 

def project_view(request):
    
    return render(request,'frontend/project.html')

def blog_view(request):

    return render(request,'frontend/blog.html')

def rank_view(request):

    return render(request,'frontend/rank.html')

def contest_view(request):

    return render(request,'frontend/contest.html')


def create_project(request):
    form = ProjectForm()
    context = {
        'form': form,
    }
    return render(request,'user_control/create_project.html', context)
