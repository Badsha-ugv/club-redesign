from django.shortcuts import render,redirect
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout


# my model
from .models import User
# Create your views here.

def test(request):
    return render(request,'base/base.html')


def register_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        student_id = request.POST.get('student_id')
        user_type = request.POST.get('user_type')
        semester = request.POST.get('semester')
        section = request.POST.get('section')
        department = request.POST.get('department')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username:
            print ('please enter username')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if User.objects.filter(username=username).exists():
            print ('username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if password != password2:
            print('Incorrect password') 
            messages.warning(request,'Incorrect password')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # exit()
            # messages.error('Please enter username')
        user = User(
            username=username,
            user_type = user_type,
            semester = semester,
            section=section,
            phone=phone,
            department = department,
            student_id = student_id,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        print('user saved successfully')
        messages.success(request,'User saved successfully')
        user.save()
        return redirect('login_view')


    return render(request,'frontend/register.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home_view')
        else:
            messages.warning(request,'Authentication failed') 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request,'frontend/login.html')


def home_view(request):

    return render(request,'frontend/home.html')