from django.contrib import admin
from .models import User, Student, Faculty

admin.site.register(User)
admin.site.register(Faculty)
admin.site.register(Student)
