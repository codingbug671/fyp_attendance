from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Student, Faculty


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    registration_no = forms.CharField(required=True)
    enrollment_no = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.registration_no = self.cleaned_data.get('registration_no')
        student.enrollment_no = self.cleaned_data.get('enrollment_no')
        student.save()
        return user


class FacultySignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_faculty = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        faculty = Faculty.objects.create(user=user)
        faculty.designation = self.cleaned_data.get('designation')
        faculty.save()
        return user
