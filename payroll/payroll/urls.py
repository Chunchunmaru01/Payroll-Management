
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')), 
    path('leave/', include('leave.urls')),          
]
