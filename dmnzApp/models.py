from distutils.command.upload import upload
from email.policy import default
from turtle import position
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Admin_register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200,default="")
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50) 
    
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    
    
class categories(models.Model):
    
    category_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE, null=True,default='')
    modelname = models.CharField(max_length=200,default='')
    description = models.CharField(max_length=255,default='')
    gib = models.FileField( upload_to="images/",null=True,blank=True,default='')
    price = models.FloatField(default='')
    types = models.CharField(max_length=255,default='')
    format = models.CharField(max_length=255,default='')
    modeltype = models.CharField(max_length=255,default='')
    image = models.ImageField(null=True, blank=True,default='')

class Register_freelance(models.Model):
    #profileinfo
    full_name=models.CharField(max_length=255,default='')
    country=models.CharField(max_length=255,default='')
    mobile=models.CharField(max_length=255,default='')
    email=models.CharField(max_length=255,default='')
    profile_pic=models.FileField(upload_to="profile/",null=True,blank=True,default='')
    #portfio
    url=models.CharField(max_length=255,default='')
    project_title=models.CharField(max_length=255,default='')
    position2=models.CharField(max_length=255,default='')
    file=models.FileField( upload_to="images/",null=True,blank=True,default='')
    #Expirence
    company=models.CharField(max_length=255,default='')
    position=models.CharField(max_length=255,default='')
    Rate=models.CharField(max_length=255,default='')
    start=models.DateField()
    end=models.DateField()
    #education
    startdate=models.DateField()
    enddate=models.DateField()
    college=models.CharField(max_length=255,default='')
    special=models.CharField(max_length=255,default='')
    education=models.CharField(max_length=255,default='')
    #skills
    proffecional_title=models.CharField(max_length=255,default='')
    service=models.CharField(max_length=255,default='')
    skills=models.CharField(max_length=255,default='')
    over_view=models.CharField(max_length=255,default='')
    
class cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    User=models.ForeignKey(User,on_delete=models.CASCADE)    
    



class designation(models.Model):
    designations= models.CharField(max_length=100)

    def __str__(self): 
        return self.designations

class Service_form(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    user_name=models.CharField(max_length=100,default='')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default='')
    service_freelancer=models.ForeignKey(Register_freelance,on_delete=models.CASCADE,default='')
    phone_number=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    Address=models.CharField(max_length=100,default='')
    description=models.CharField(max_length=100,default='')
    status=models.CharField(max_length=100,default='')

    




