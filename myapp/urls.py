# enrollment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('students/', views.student_list, name='student_list'),
    path('course/<int:course_id>/', views.course_details, name='course_details'),
]

