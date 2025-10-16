from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.contrib.auth import login,logout,authenticate
from appname.models import EmployeeExperience 
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'index.html')

def registration(request):
    error=""
    if request.method =="POST":
        fn=request.POST["firstname"]
        ln=request.POST["lastname"]
        em=request.POST["email"]
        ec=request.POST["empcode"]
        pwd=request.POST["pwd"]
        
       
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
           
            error="no"
        except Exception as e:
            print("Error:", e)  # Print the error to debug
            error = "yes"
    
    return render(request, 'registration.html',locals())

def emp_login(request):
    error=""
    if request.method=="POST":
        U=request.POST['emailid']
        P=request.POST['password']
        User = authenticate(username=U, password=P)
        if User:
            login(request,User)
            error="no"
        else:
            error="yes"
    return render(request, 'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user

    # ✅ Ensure EmployeeDetail record exists
    employee, created = EmployeeDetail.objects.get_or_create(user=user)

    if request.method == "POST":
        fn = request.POST.get("firstname")
        ln = request.POST.get("lastname")
        ec = request.POST.get("empcode")
        designation = request.POST.get("designation")
        dept = request.POST.get("department")
        contact = request.POST.get("contact")
        jdate = request.POST.get("jdate")
        gender = request.POST.get("gender")

        # ✅ Update user details
        user.first_name = fn
        user.last_name = ln
        user.save()

        # ✅ Update EmployeeDetail fields
        employee.empcode = ec
        employee.designation = designation
        employee.empdept = dept
        employee.contact = contact
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            error = "no"
        except Exception as e:
            print(f"Error: {e}")  # Debugging
            error = "yes"

    return render(request, 'profile.html', {'employee': employee, 'error': error})

def admin_login(request):
    return render(request, 'admin_login.html')

def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user

    # ✅ Ensure EmployeeExperience record exists
    experience, created = EmployeeExperience.objects.get_or_create(user=user)

    return render(request, 'my_experience.html', {'experience': experience})


def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user

    # ✅ Ensure experience exists to prevent 'NoneType' errors
    experience, created = EmployeeExperience.objects.get_or_create(user=user)

    if request.method == "POST":
        experience.company1name = request.POST.get("company1name", experience.company1name)
        experience.company1desig = request.POST.get("company1desig", experience.company1desig)
        experience.company1salary = request.POST.get("company1salary", experience.company1salary)
        experience.company1duretion = request.POST.get("company1duretion", experience.company1duretion)

        experience.company2name = request.POST.get("company2name", experience.company2name)
        experience.company2desig = request.POST.get("company2desig", experience.company2desig)
        experience.company2salary = request.POST.get("company2salary", experience.company2salary)
        experience.company2duretion = request.POST.get("company2duretion", experience.company2duretion)

        experience.company3name = request.POST.get("company3name", experience.company3name)
        experience.company3desig = request.POST.get("company3desig", experience.company3desig)
        experience.company3salary = request.POST.get("company3salary", experience.company3salary)
        experience.company3duretion = request.POST.get("company3duretion", experience.company3duretion)

        try:
            experience.save()
            error = "no"
        except Exception as e:
            print(f"Error: {e}")  # Debugging
            error = "yes"

    return render(request, 'edit_myexperience.html', {'experience': experience, 'error': error})


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user

    # ✅ Ensure EmployeeEducation record exists
    education, created = EmployeeEducation.objects.get_or_create(user=user)

    return render(request, 'my_education.html', {'education': education})


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user

    # ✅ Ensure education record exists
    education, created = EmployeeEducation.objects.get_or_create(user=user)

    if request.method == "POST":
        education.coursepg = request.POST.get("coursepg", education.coursepg)
        education.schoolclgpg = request.POST.get("schoolclgpg", education.schoolclgpg)
        education.yearofpassingpg = request.POST.get("yearofpassingpg", education.yearofpassingpg)
        education.percentagepg = request.POST.get("percentagepg", education.percentagepg)

        education.coursegra = request.POST.get("coursegra", education.coursegra)
        education.schoolclggra = request.POST.get("schoolclggra", education.schoolclggra)
        education.yearofpassinggra = request.POST.get("yearofpassinggra", education.yearofpassinggra)
        education.percentagegra = request.POST.get("percentagegra", education.percentagegra)

        education.coursessc = request.POST.get("coursessc", education.coursessc)
        education.schoolclgssc = request.POST.get("schoolclgssc", education.schoolclgssc)
        education.yearofpassingssc = request.POST.get("yearofpassingssc", education.yearofpassingssc)
        education.percentagessc = request.POST.get("percentagessc", education.percentagessc)

        education.coursehsc = request.POST.get("coursehsc", education.coursehsc)
        education.schoolclghsc = request.POST.get("schoolclghsc", education.schoolclghsc)
        education.yearofpassinghsc = request.POST.get("yearofpassinghsc", education.yearofpassinghsc)
        education.percentagehsc = request.POST.get("percentagehsc", education.percentagehsc)

        try:
            education.save()
            error = "no"
        except Exception as e:
            print(f"Error: {e}")  # Debugging
            error = "yes"

    return render(request, 'edit_myeducation.html', {'education': education, 'error': error})

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error=""
    user=request.user
    if request.method =="POST":
        c = request.POST['currentpassword']
        n =  request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
            
        
                error="no"
            else:
                eror="not"
        except:
            error="yes"
    
    return render(request, 'change_password.html',locals())

def admin_login(request):
    error=""
    if request.method=="POST":
        U=request.POST['username']
        P=request.POST['pwd']
        User = authenticate(username=U, password=P)
        try:
            
            if User.is_staff:
                login(request,User)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    return render(request, 'admin_login.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    user=request.user
    if request.method =="POST":
        c = request.POST['currentpassword']
        n =  request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
            
        
                error="no"
            else:
                eror="not"
        except:
            error="yes"
    
    return render(request, 'change_passwordadmin.html',locals())

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee=EmployeeDetail.objects.all()
    return render(request, 'all_employee.html',locals())


def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('emp_login')  # Only admin can access

    total_employees = EmployeeDetail.objects.count()
    total_education = EmployeeEducation.objects.count()
    total_experience = EmployeeExperience.objects.count()

    context = {
        'total_employees': total_employees,
        'total_education': total_education,
        'total_experience': total_experience,
    }
    return render(request, 'admin_dashboard.html', context)


def admin_reports(request):
    if not request.user.is_staff:
        return redirect('emp_login')

    employees = EmployeeDetail.objects.all()

    context = {
        'employees': employees,
    }
    return render(request, 'admin_reports.html', context)

@login_required 
def view_reports(request):
    reports = EmployeeReport.objects.filter(employee=request.user)
    return render(request, 'view_reports.html', {'reports': reports})



