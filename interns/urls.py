from django.urls import path
from .views import *

urlpatterns = [
    path('application_tracking/', application_tracking, name='application_tracking'),
    path('intern_dashboard/', dashboard, name='intern_dashboard'),
    # path('dashboard_tasks/',dashboard_tasks , name='dashboard_tasks'),
    path('application/', show_application, name='application'),
    path('tasks/', tasks, name='tasks'),
    path('tasks/<str:intern_day>/', task_details, name='task_details'),
    path('intern_details/', intern_details, name='intern_details'),
    path('other_details/<str:intern_day>/<str:task>', other_details, name='other_details')
]

