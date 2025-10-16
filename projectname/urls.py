"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from appname.views import index, registration ,emp_login,emp_home,profile,Logout,admin_login,my_experience,edit_myexperience,my_education,edit_myeducation,change_password,admin_home,change_passwordadmin,all_employee,admin_dashboard,admin_reports 
from appname import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('registration/', registration, name='registration'),
    path('emp_login', emp_login, name='emp_login'),
    path('emp_home', emp_home, name='emp_home'),
    path('profile', profile, name='profile'),
    path('logout', Logout, name='logout'),
    path('admin_login', admin_login, name='admin_login'),
    path('my_experience', my_experience, name='my_experience'),
    path('edit_myexperience', edit_myexperience, name='edit_myexperience'),
    path('my_education', my_education, name='my_education'),
    path('edit_myeducation', edit_myeducation, name='edit_myeducation'),
    path('change_password', change_password, name='change_password'),
    path('admin_home', admin_home, name='admin_home'),
    path('change_passwordadmin', change_passwordadmin, name='change_passwordadmin'),
    path('all_employee', all_employee, name='all_employee'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin_reports/', admin_reports, name='admin_reports'),
    path('view-reports/', views.view_reports, name='view_reports'),
    

]


