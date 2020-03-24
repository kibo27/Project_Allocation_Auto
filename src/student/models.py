from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Faculty(models.Model):
    id=models.PositiveIntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=120)
    saa=models.BooleanField(default=False)
    sa=models.IntegerField(null=True,blank=True)
    sba=models.BooleanField(default=False)
    sb=models.IntegerField(null=True,blank=True)
    sca=models.BooleanField(default=False)
    sc=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name


class student(models.Model):
    name=models.CharField(max_length=120,blank=False)
    regno=models.IntegerField(null=False,editable=True)
    cpi=models.DecimalField(max_digits=3, decimal_places=2,null=True,blank=False)
    gender_choices=[('M','Male'),('F','Female')]
    gender=models.CharField(choices=gender_choices,max_length=1,default=None,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fac_allocated=models.BooleanField(default=False)
    sa=models.ForeignKey('Faculty',on_delete=models.SET_NULL,blank=True,
    null=True)
    to=models.BooleanField(default=False)


class choice(models.Model):
    cfilled=models.BooleanField(default=False)
    student=models.OneToOneField(student,on_delete=models.CASCADE)
    choice1=models.IntegerField(null=True)
    choice2=models.IntegerField(null=True)
    choice3=models.IntegerField(null=True)
    choice4=models.IntegerField(null=True)
    choice5=models.IntegerField(null=True)
    choice6=models.IntegerField(null=True)
    choice7=models.IntegerField(null=True)
    choice8=models.IntegerField(null=True)
    choice9=models.IntegerField(null=True)
    choice10=models.IntegerField(null=True)
    choice11=models.IntegerField(null=True)
    choice12=models.IntegerField(null=True)
    choice13=models.IntegerField(null=True)
    choice14=models.IntegerField(null=True)
    choice15=models.IntegerField(null=True)
    choice16=models.IntegerField(null=True)
    choice17=models.IntegerField(null=True)
    choice18=models.IntegerField(null=True)
    choice19=models.IntegerField(null=True)
    choice20=models.IntegerField(null=True)
    