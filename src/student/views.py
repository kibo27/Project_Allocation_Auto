from django.shortcuts import render, redirect
from .forms import UserForm, RegistrationForm, LoginForm,choices,TeacherForm
from django.http import HttpResponse, Http404
from .models import Faculty,student,choice
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_v(request):
    if request.user.is_authenticated:
    	return redirect('profile')
    else:
        form = UserForm()
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                new_user=form.save(commit=False)
                new_user.save()
                cd = form.cleaned_data
                stud=student.objects.create(user=new_user,regno=cd['username'])
                choice.objects.create(student=stud)
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
        return redirect('profile')
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

@login_required    
def edit_v(request):
    form = RegistrationForm(instance=request.user.student)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=request.user.student)
        if form.is_valid():
            form.save()
            student = request.user.student
            return render(request, 'profile.html', {'student': student})
        
    return render(request, 'edit.html', {'form': form})

@login_required
def choice_v(request):
    if request.method=="POST":
        ch =choice.objects.get(student=request.user.student)
        form= choices(request.POST)
        if form.is_valid():
            le=len(form.fields)
            for i in form.fields:
                cd = form.cleaned_data[i]
                setattr(ch,i,cd.id)
            ch.save()
            return redirect('profile')
    else:    
        form = choices()
        ch =choice.objects.get(student=request.user.student)
        if ch.cfilled == True:
            for i in form.fields:
                cd=getattr(ch,i)
                form.fields[i].initial=cd
            print("true")
        else:
            setattr(ch,'cfilled',True)
            ch.save()
            print("false")
        return render(request, 'choice.html',{"form":form})
@login_required
def logout_v(request):
	logout(request)
	return redirect('login')

@login_required
def profile(request):
    student = request.user.student
    print(student.sa)
    return render(request, 'profile.html', {'student': student})

def home_v(request):
    return render(request,'home.html',{})

def teacher_v(request):
    if request.method=="POST":
        form =TeacherForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data['id']
            fac=get_object_or_404(Faculty,id=cd)
            print("you are "+fac.name+" child alloacted "+str(fac.sa))
            if fac.saa ==True:
                ca=get_object_or_404(student,regno=fac.sa)
                if fac.sba ==True:
                    cb=get_object_or_404(student,regno=fac.sb)
                    if fac.sca ==True:
                        cc=get_object_or_404(student,regno=fac.sc)
                        return render(request,'teacher_list.html',{'fac':fac, 'ca':ca,'cb':cb,'cc':cc})
                    else:
                        return render(request,'teacher_list.html',{'fac':fac, 'ca':ca,'cb':cb})
                else:
                    print(fac.saa)
                    print(ca.name)
                    return render(request,'teacher_list.html',{'fac':fac, 'ca':ca})
            else:
                return render(request,'teacher_list.html',{'fac':fac}) 
    else:
        form=TeacherForm()
        return render(request,'teacher.html',{'form':form})