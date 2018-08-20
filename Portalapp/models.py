from django.db import models

# Create your models here.

		
class form(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=100)  
    date = models.CharField(max_length=100)
    info = models.CharField(blank=True,max_length=1000)
    email= models.EmailField()
    phone= models.CharField(max_length=100)
    address= models.CharField(max_length=1000)
    approval=models.IntegerField(default=0)
class users(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usergroup = models.CharField(max_length=100)
	
class form2(models.Model):
    approval=models.CharField(max_length=10)


    

