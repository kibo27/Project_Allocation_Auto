from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Faculty(models.Model):
    id=models.PositiveIntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=120)

class student(models.Model):
    name=models.CharField(max_length=120,blank=False)
    cpi=models.DecimalField(max_digits=3, decimal_places=2,null=True,blank=False)
    gender_choices=[('M','Male'),('F','Female')]
    gender=models.CharField(choices=gender_choices,max_length=1,default=None,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)