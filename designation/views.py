from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import designation
from django.urls import reverse


# Create your views here.

@login_required(login_url='/login')
def insert_des(request):
    title='Employee Designation'
    if request.method=='POST':
        des_name=request.POST['des_name']
        data=designation.objects.create(des_name=des_name)
        data.save()
        return redirect(reverse('show-des'))
    else:
        return (render(request,template_name='insert_des.html',context={'title':title}))

@login_required(login_url='/login')
def show_des(request):
    des=designation.objects.all()
    title='Showing designation'
    return render(request,template_name='show_des.html',context={'des':des,'title':title})

@login_required(login_url='/login')
def edit_des(request, pk):
    des=designation.objects.get(id=pk)
    title='Editing designstion'
    if request.method=='POST':
        des.des_name=request.POST['des_name']
        des.save()
        return redirect(reverse('show-des'))
    return render(request,template_name='edit_des.html',context={'des':des,'title':title})

@login_required(login_url='/login')
def remove_des(request,pk):
    title='Removing designation'
    des = designation.objects.get(id=pk)
    if request.method == 'POST':
        des.delete()
        return redirect(reverse('show-des'))

    return render(request,template_name='delete_des.html',context={'des':des,'title':title})