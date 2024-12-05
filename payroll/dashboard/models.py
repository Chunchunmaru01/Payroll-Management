# employees/models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    date_hired = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

# Additional model if you want to track actions on the dashboard
class DashboardStats(models.Model):
    total_employees = models.IntegerField(default=0)
    total_departments = models.IntegerField(default=0)

    def update_stats(self):
        self.total_employees = Employee.objects.count()
        self.total_departments = Department.objects.count()
        self.save()
