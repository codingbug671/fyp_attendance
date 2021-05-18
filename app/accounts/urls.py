from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('student_register/', views.student_register.as_view(),
         name='student_register'),
    path('faculty_register/', views.faculty_register.as_view(),
         name='faculty_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
