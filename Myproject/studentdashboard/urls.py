from django.urls import path
from . import views #(.) means current directory bata sabai file haru import garne milcha
from django.contrib.auth import views as auth_views

app_name = 'studentdashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('student/add/', views.add_student, name='add_student'),
    path('student/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('student/delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
