from django.db import models
from django.contrib.auth.models import User

class EmployeeDetail(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    empcode=models.CharField(max_length=50,null=True)
    empdept=models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    joiningdate=models.DateField(null=True)
    

    
    def __str__(self):
        return self.user.username 
    
class EmployeeEducation(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    coursepg=models.CharField(max_length=100,null=True)
    schoolclgpg=models.CharField(max_length=200,null=True)
    yearofpassingpg=models.CharField(max_length=20,null=True)
    percentagepg=models.CharField(max_length=30)
    coursegra=models.CharField(max_length=100,null=True)
    schoolclggra=models.CharField(max_length=200,null=True)
    yearofpassinggra=models.CharField(max_length=20,null=True)
    percentagegra=models.CharField(max_length=30)
    coursessc=models.CharField(max_length=100,null=True)
    schoolclgssc=models.CharField(max_length=200,null=True)
    yearofpassingssc=models.CharField(max_length=20,null=True)
    percentagessc=models.CharField(max_length=30)
    coursehsc=models.CharField(max_length=100,null=True)
    schoolclghsc=models.CharField(max_length=200,null=True)
    yearofpassinghsc=models.CharField(max_length=20,null=True)
    percentagehsc = models.FloatField(default=0.0)

    
    def __str__(self):
        return self.user.username 
    
class EmployeeExperience(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    company1name=models.CharField(max_length=100,null=True)
    company1desig=models.CharField(max_length=50,null=True)
    company1salary=models.CharField(max_length=100,null=True)
    company1duretion=models.CharField(max_length=100)
    company2name=models.CharField(max_length=150,null=True)
    company2desig=models.CharField(max_length=100,null=True)
    company2salary=models.CharField(max_length=100,null=True)
    company2duretion=models.CharField(max_length=100)
    company3name=models.CharField(max_length=100,null=True)
    company3desig=models.CharField(max_length=100,null=True)
    company3salary=models.CharField(max_length=100,null=True)
    company3duretion=models.CharField(max_length=100)



    
    def __str__(self):
        return self.user.username 
class EmployeeReport(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)  # Link report to user
    department = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    report_details = models.TextField()

    def __str__(self):
        return f"Report {self.id} - {self.employee.username}"