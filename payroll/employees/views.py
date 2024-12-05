from django.shortcuts import render, redirect
from .models import Employee

def dashboard(request):
    # Here you can gather statistics or important info to display
    total_employees = Employee.objects.count()
    context = {'total_employees': total_employees}
    return render(request, 'employees/dashboard.html', context)

def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees/employee_list.html', context)

def add_employee(request):
    if request.method == 'POST':
        # Logic for adding a new employee
        # For example, process form data here
        return redirect('employee_list')  # Redirect after successful addition
    return render(request, 'employees/add_employee.html')
