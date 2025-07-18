from django.urls import path
from .views import *

urlpatterns = [
    path('interns/', show_interns, name='interns'),
    path('intern_details/<str:first_name>', intern_details, name='intern_details')
]

