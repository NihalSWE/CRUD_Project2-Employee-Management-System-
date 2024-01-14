from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def allemp(request):
    return render(request,'all_emp.html')

def add(request):
    return render(request,'add_emp.html')

def remove(request):
    return render(request,'remove.html')