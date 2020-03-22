from django.shortcuts import render, redirect
from .forms import UserForm, RegistrationForm, LoginForm
from django.http import HttpResponse, Http404
from .models import Faculty,student
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 

# Create your views here.

def register_v(request):
    if request.user.is_authenticated:
    	return redirect('/')
    else:
        form = UserForm()
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                new_user=form.save(commit=False)
                new_user.save()
                student.objects.create(user=new_user)
                cd = form.cleaned_data
                user = authenticate(
                    request,
                    username=cd['username'],
                    password=cd['password1'])
                if user is not None:
                    login(request, user)
                    return redirect('/login/edit')
                else:
                    return HttpResponse('Invalid Login')
            
        return render(request,"register.html",{"form":form})

def login_v(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form= LoginForm(request.POST)
            if form.is_valid():
                cd=form.cleaned_data
                user=authenticate(
                    request,
                    username=cd["username"],
                    password=cd["password"]
                )
            if user is not None:
                login(request,user)
                student = request.user.student
                return render(request, 'profile.html', {'student': student})
            else:
                return HttpResponse("Invalid username or password")
        else:
            form= LoginForm()
            return render(request,"login.html",{"form":form})

def Faculty_list(request):
    list=Faculty.objects.all()
    return render(request,'faculty_list.html',{'list':list})
    
def edit_v(request):
    form = RegistrationForm(instance=request.user.student)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=request.user.student)
        if form.is_valid():
            form.save()
            student = request.user.student
            return render(request, 'profile.html', {'student': student})
        
    return render(request, 'edit.html', {'form': form})


def logout_v(request):
	logout(request)
	return redirect('login')

def profile(request):
    student = request.user.student
    return render(request, 'profile.html', {'student': student})
