"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home_v,name='home'),
    path('faculty/',v.Faculty_list,name='faculty'),
    path('register/',v.register_v,name='register'),
    path('login/',v.login_v,name='login'),
    path('login/edit/',v.edit_v,name='edit'),
    path('logout/',v.logout_v,name='logout'),
    path('profile/',v.profile,name='profile'),
    path('choice/',v.choice_v,name='choice'),
    path('teacher/',v.teacher_v,name='teacher'),
]
