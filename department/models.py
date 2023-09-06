from django.db import models

# Create your models here.

class Department(models.Model):
    EmpDept=models.CharField(max_length=50)
    EmpManName = models.CharField(max_length=100)
    EmpManNameEmail = models.EmailField(max_length=100)
    EmpDob = models.CharField(max_length=10)
    EmpPhone=models.CharField(max_length=10)
    EmpSalary=models.CharField(max_length=10)