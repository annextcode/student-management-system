# enrollment/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'number', 'age', 'enrollment_date', 'course']
        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
        }
