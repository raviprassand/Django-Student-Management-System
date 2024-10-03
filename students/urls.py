from django.urls import path
from .views import student_list, student_detail, add_student, edit_student
from .views import register, user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('', student_list, name='student_list'),  # Root URL for student list
    path('student/<int:student_id>/', student_detail, name='student_detail'),  # URL for student detail
    path('student/add/', add_student, name='add_student'),  # URL to add a new student
    path('student/edit/<int:student_id>/', edit_student, name='edit_student'),  # URL to edit a student
]
