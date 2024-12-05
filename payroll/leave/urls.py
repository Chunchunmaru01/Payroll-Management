
from django.urls import path
from .views import LeaveRequest

urlpatterns = [
    path('report/', LeaveRequest, name='leave_report'),
    #path('', leave_list, name='leave_list'),
]
