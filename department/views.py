from django.shortcuts import render,redirect
from department.models import Department
from django.urls import reverse
# Create your views here.
def insert_dept(request):
    title='Employees Department'
    if request.method=='POST':
        EmpDept = request.POST['EmpDept']
        EmpManName = request.POST['EmpManName']
        EmpManNameEmail = request.POST['EmpManNameEmail']
        EmpDob = request.POST['EmpDob']
        EmpPhone = request.POST['EmpPhone']
        EmpSalary = request.POST['EmpSalary']
        data=Department(EmpDept=EmpDept,EmpManName=EmpManName,EmpManNameEmail=EmpManNameEmail,EmpDob=EmpDob,EmpPhone=EmpPhone,EmpSalary=EmpSalary)
        data.save()
        return redirect(reverse('show-dept'))
    else:
        return render(request, template_name='insert_dept.html',context={'title':title})

def show_dept(request):
    departments=Department.objects.all()
    title='Showing Department'
    return render(request,template_name='show_dept.html',context={'departments':departments,'title':title})

def edit_dept(request,pk):
    department=Department.objects.get(id=pk)
    title='Editing Department'
    if request.method=='POST':
        department.EmpDept=request.POST['EmpDept']
        department.EmpManName=request.POST['EmpManName']
        department.EmpManNameEmail=request.POST['EmpManNameEmail']
        department.EmpPhone=request.POST['EmpPhone']
        department.EmpSalary=request.POST['EmpSalary']
        department.save()
        return redirect('show/')
    return render(request,template_name='edit_dept.html',context={'department':department,'title':title})

def remove_dept(request,pk):
    title='Removing Department'
    department = Department.objects.get(id=pk)
    if request.method == 'POST':
        department.delete()
        return redirect(reverse('show-dept'))

    return render(request,template_name='delete_dept.html',context={'department':department,'title':title})