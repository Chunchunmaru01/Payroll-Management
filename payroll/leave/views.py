
from django.shortcuts import render
from .models import LeaveRequest

def employee_list(request):
    leave = LeaveRequest.objects.all()
    return render(request, 'leave/leave_report.html', {'leave': leave})