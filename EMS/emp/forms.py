from .models import Department,Role,Employee
from django import forms


class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = Employee
        fields=['first_name','last_name', 'email', 'phone','dept','role','salary']
        
