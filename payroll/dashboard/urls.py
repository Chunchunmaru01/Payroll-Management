# dashboard/urls.py
from django.urls import path
from .views import dashboard_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),  # Dashboard view at root of dashboard app
    # Add more patterns as needed...
]
