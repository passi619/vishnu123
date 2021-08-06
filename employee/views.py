from typing import Any
from django.shortcuts import render,redirect
from employee.models import Department,Employee
from employee.forms import DepartmentForm,EmployeeForm
from django.contrib import messages
from django.contrib.auth.models import User,auth






def home(request):
    return redirect(request,"")


def dept(request):
    if request.method == "POST":

        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = DepartmentForm()
    return render(request, "index.html", {'form':form})


def show(request):
    departments = Department.objects.all()
    return render(request, "show.html", {'departments':departments})


def edit(request, cName):
    department = Department.objects.get(cName=cName)
    return render(request, "edit.html", {'department':department})


def update(request, cName):
    department = Department.objects.get(cName=cName)
    form = DepartmentForm(request.POST, instance= department)
    if form.is_valid():
        
            form.save()
            return redirect("/show")
    return render(request , "edit.html",{'department': department})   

def searchde(request):
    if request.method == 'GET':
        searchs=request.GET.get('searchs')
        departments=Department.objects.all().filter(cName=searchs)
        return render(request,'searchdept.html',{'departments':departments})

    else :
        return redirect("/showemp")   


def delete(request, cName):
    department = Department.objects.get(cName=cName)
    department.delete()
    return redirect("/show")




      
        
    

def emp(request):
    if request.method == "POST":

        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form':form})

def showemp(request):
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})


def searchem(request):
    if request.method == 'GET':
        searchs=request.GET.get('searchs')
        employees=Employee.objects.all().filter(eFname=searchs)
        return render(request,'searchemp.html',{'employees':employees})

    else :
        return redirect("/showemp")



def deleteEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")


def editemp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    return render(request, "editemployee.html", {'employee':employee})

def updateEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    form = EmployeeForm(request.POST, instance= employee)
    if form.is_valid():
       
        form.save()
        return redirect("/showemp")
        
    return render(request, "editemployee.html", {'employee': employee})


def sorta(request):
    
    employees = Employee.objects.all().order_by('eFname')
    return render(request, "sortaem.html", {'employees':employees})

def sortdem(request):
    employees = Employee.objects.all().order_by('-eFname')
    return render(request, "sortaem.html", {'employees':employees})

def sortade(request):
    departments=Department.objects.all().order_by('cName')
    return render(request, "sortd.html", {'departments':departments})

def sortdde(request):
    departments=Department.objects.all().order_by('-cName')
    return render(request, "sortd.html", {'departments':departments})
    