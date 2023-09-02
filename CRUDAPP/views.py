from django.shortcuts import render, redirect
from .models import Employee
# from django.conf import settings


# Create your views here.

def insert_emp(request):
    if request.method=="POST":
        EmpId=request.POST['EmpId']
        EmpName=request.POST['EmpName']
        EmpGender=request.POST['EmpGender']
        EmpEmail=request.POST['EmpEmail']
        EmpDesignation=request.POST['EmpDesignation']
        data=Employee(EmpId=EmpId,EmpName=EmpName,EmpGender=EmpGender,
            EmpEmail=EmpEmail,EmpDesignation=EmpDesignation)
        data.save()

        return redirect('show/')
    else:
        # breakpoint()
        return render(request, template_name='insert.html')
def show_emp(request):
    employees=Employee.objects.all()
    return render(request,template_name='show.html', context={'employees':employees})
def edit_emp(request,pk):
    employee=Employee.objects.get(id=pk)
    if request.method =='POST':
        employee.EmpGender = request.POST['EmpGender']
        # breakpoint()
        # employee.EmpName = request.POST['EmpName']
        employee.EmpEmail = request.POST['EmpEmail']
        employee.EmpDesignation = request.POST['EmpDesignation']
        employee.save()
        return redirect('/show')

    context={
        'employees': employee,
    }

    return render(request,'edit.html',context)
def remove_emp(request,pk):
    employees=Employee.objects.get(id=pk)

    if request.method=='POST':
        employees.delete()
        return redirect('/show')

    context={
        'employees':employees,
    }

    return render(request,'delete.html',context)