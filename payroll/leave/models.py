
from django.db import models

class LeaveRequest(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
