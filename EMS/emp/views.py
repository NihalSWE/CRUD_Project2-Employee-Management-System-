from django.shortcuts import render
from .models import Employee,Role,Department
from .forms import EmployeeRegistration

# Create your views here.

def base(request):
    return render(request, 'base.html')

def allemp(request):
    emps = Employee.objects.all()
    context ={
        'emps':emps
    }
    return render(request,'all_emp.html',context)

def add(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
    else:
        fm = EmployeeRegistration()
    return render(request,'add_emp.html',{'form':fm})

def remove(request):
    return render(request,'remove.html')