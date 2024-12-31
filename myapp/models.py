from django.db import models

# Create your models here.
class addworker_model(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    skills=models.TextField()
    exp=models.TextField()
    location=models.CharField(max_length=500) 
    password=models.CharField(max_length=50)

class addjob_model(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    job_title=models.TextField()
    work_location=models.TextField()
    job_requirements=models.CharField(max_length=500)  
    password=models.CharField(max_length=50)  
    


class signupmodel(models.Model):
    fullname=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    location=models.TextField()
    email=models.EmailField()
    password=models.CharField(max_length=50)


class contactmodel(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    msg=models.TextField()

    

