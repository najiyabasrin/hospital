from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Departments(models.Model):
    deptname=models.CharField(max_length=200)
    deptimage=models.ImageField(upload_to='images')
    year=models.DateField(auto_now_add=True)
    description=models.TextField()
    

    def __str__(self):
        return self.deptname



class DepartmentHead(models.Model):
    name=models.CharField(max_length=200)
    empno=models.CharField(max_length=50)
    age=models.IntegerField()
    proimage=models.ImageField(upload_to='images')
    prodescription=models.TextField()
    deptname=models.CharField(max_length=200)


class Employees(models.Model):
    ename=models.CharField(max_length=200)
    empno=models.CharField(max_length=50)
    age=models.IntegerField()
    proimage=models.ImageField(upload_to='images')
    prodescription=models.TextField()
    deptname=models.CharField(max_length=200)






