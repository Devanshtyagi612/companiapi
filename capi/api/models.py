from django.db import models

# Create your models here.
class Company(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField( max_length=50)
    about=models.TextField()
    date=models.DateTimeField()
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.name +"-"+ self.location
    
    
    
    
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.TextField()
    phone=models.IntegerField()
    position=models.CharField(max_length=50,choices=(('Manager','manger'),('Developer','developer'),('Tester','tester')))
    
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    
    
    
