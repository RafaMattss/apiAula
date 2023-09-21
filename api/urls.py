from django.contrib import admin
from django.urls import path

from api.views.discipline import DisciplineView, DisciplineDetailView
from api.views.student import StudentView, StudentDetailView
from api.views.task import TaskView, TaskDetailView
from api.views.taskStudent import TaskStudentView


apiUrls = [
    path('discilplines/', DisciplineView.as_view()),
    path('discilplines/<int:pk>/', DisciplineDetailView.as_view()),
    path('students/', StudentView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    path('students/<int:pk>/tasks/', TaskStudentView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    
]
