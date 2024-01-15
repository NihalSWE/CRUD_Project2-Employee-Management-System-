from django.contrib import admin
from .models import Department,Role,Employee

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('name','location')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin): # A comma-separated
    list_display = ('id','first_name', 'last_name','email', 'phone', 'dept', 'role', 'salary')
    search_fields = ['first_name', 'last_name'] 


    def dept(self, obj):
        return obj.dept.name

    def role(self, obj):
        return obj.role.name