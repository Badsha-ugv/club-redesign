from django.shortcuts import render


# my views 
from .models import SliderImage
# Create your views here.

def home_view(request):
    slider_image = SliderImage.objects.all()[:3]
    context = {
        'slider': slider_image,
    }
    return render(request,'frontend/home.html',context) 

def event_view(request):

    return render(request,'frontend/event.html')

def project_view(request):
    
    return render(request,'frontend/project.html')

def blog_view(request):

    return render(request,'frontend/blog.html')

def rank_view(request):

    return render(request,'frontend/rank.html')

def contest_view(request):

    return render(request,'frontend/contest.html')
