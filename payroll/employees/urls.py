from django.urls import path
from .views import dashboard, employee_list, add_employee

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('list/', employee_list, name='employee_list'),
    path('add/', add_employee, name='add_employee'),
]
