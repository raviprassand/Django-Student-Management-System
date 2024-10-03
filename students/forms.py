from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if not (1 <= grade <= 12):
            raise forms.ValidationError("Grade must be between 1 and 12.")
        return grade
