from django.shortcuts import render, redirect
from CRUDAPP.models import Employee
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from CRUDAPP.forms import EmployeeForm,EditForm
from department.models import Department
from designation.models import designation
# from django.conf import settings


# Create your views here.


@login_required(login_url='/login')
def insert_emp(request):
    title = "Employees Information"
    EmpForm = EmployeeForm()
    if request.method=="POST":
        EmpForm = EmployeeForm(request.POST)
        if EmpForm.is_valid():
            EmpId=request.POST['EmpId']
            EmpName=request.POST['EmpName']
            EmpGender=request.POST['EmpGender']
            EmpEmail=request.POST['EmpEmail']
            desig = request.POST['designation']
            desig = designation.objects.get(id=int(desig))
           # EmpDesignation=request.POST['EmpDesignation']

            emp_obj = Employee.objects.create(EmpId=EmpId,EmpName=EmpName,EmpGender=EmpGender,
                EmpEmail=EmpEmail, designation=desig)
            departments = request.POST.getlist('EmpDepartment')
            for dept in departments:
                dept = Department.objects.get(id=int(dept))
                emp_obj.EmpDepartment.add(dept)

            emp_obj.save()

            return redirect(reverse('show-emp'))      # /show or show/ is same
        else:
            return render(request, template_name='insert.html', context={'title': title, 'form': EmpForm})
    else:
        return render(request, template_name='insert.html', context={'title':title, 'form': EmpForm})

@login_required(login_url='/login')
def show_emp(request):
    employees=Employee.objects.all()
    # breakpoint()desig=request.POST.getlist('EmpDes')
    for emp in employees:
        emp.depts = emp.EmpDepartment.all()

    title = "List Employees"
    return render(request,template_name='show.html', context={'employees':employees, 'title': title})

@login_required(login_url='/login')
def edit_emp(request,pk):

    employee=Employee.objects.get(id=pk)
    title='Editing Employees'
    Empform = EditForm(initial={'EmpEmail':employee.EmpEmail,})
    if request.method =='POST':
        Empform=EditForm(request.POST)
        if Empform.is_valid():
            #employee.EmpGender = request.POST['EmpGender']
            # breakpoint()
            employee.EmpEmail = request.POST['EmpEmail']
            #employee.EmpDesignation = request.POST['EmpDesignation']
            employee.save()
            return redirect(reverse('show-emp'))
        else:
            return render(request, template_name='edit.html', context={'title': title,'myform':Empform})


    return render(request,template_name='edit.html',context={'title':title,'myform':Empform})

@login_required(login_url='/login')
def remove_emp(request,pk):
    title='Removing Employees'
    employees=Employee.objects.get(id=pk)

    if request.method=='POST':
        employees.delete()
        return redirect(reverse('show-emp'))

    context={
        'employees':employees,
    }

    return render(request,'delete.html',context={'title':title})

