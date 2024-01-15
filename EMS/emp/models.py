from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name



class Employee(models.Model):
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12, blank=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    salary = models.FloatField(default=0)

    def __str__(self):
        return self.first_name