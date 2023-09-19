from django.db import models
from department.models import Department
from designation.models import designation

# Create your models here.

class Employee(models.Model):
    EmpId=models.CharField(max_length=3)
    EmpName=models.CharField(max_length=200)
    EmpGender=models.CharField(max_length=10)
    EmpEmail=models.EmailField(max_length=255)
    EmpDepartment=models.ManyToManyField(Department)
    designation=models.ForeignKey(designation,on_delete=models.CASCADE)
    class Meta:
        db_table = "Employee"