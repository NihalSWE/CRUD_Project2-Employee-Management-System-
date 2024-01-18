from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Employee,Role,Department
from .forms import EmployeeRegistration
from django.db.models import Q
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
        if fm.is_valid():
            fname = fm.cleaned_data['first_name']
            lname = fm.cleaned_data['last_name']
            email = fm.cleaned_data['email']
            phone = fm.cleaned_data['phone']
            role = fm.cleaned_data['role'].id
            dept = fm.cleaned_data['dept'].id
            salary = fm.cleaned_data['salary']
            emp = Employee(first_name=fname,last_name=lname,email=email,phone=phone,role_id=role,dept_id=dept,salary=salary)
            emp.save()
            return redirect ('allemp')
                                            
    else:
        fm = EmployeeRegistration()
    return render(request,'add_emp.html',{'form':fm})

def remove(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return redirect ('allemp')
        except:
            return HttpResponse("Error in Deleting the data")


    emps = Employee.objects.all()
    context ={
        'emps':emps
    }
    
    return render(request,'remove.html',context)

def update(request,id):
    if request.method == 'POST':
        uf = Employee.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST,instance=uf)
        if fm.is_valid():
            fm.save()
    else:
        uf = Employee.objects.get(pk=id)
        fm = EmployeeRegistration(instance=uf)
        
    return render(request, 'update.html', {'form':fm})
    

def search(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        

        context ={
            "emps": emps,
        }
        return render(request,"all_emp.html",context)
    elif request.method == 'GET':
        return render(request,"search.html")
    else:
        return HttpResponse("Not a valid Request")
            