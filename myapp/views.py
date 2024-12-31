# enrollment/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student, Course

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Check if the student is already enrolled in a course
            email = form.cleaned_data.get('email')
            existing_student = Student.objects.filter(email=email).first()
            if existing_student:
                # If student is already enrolled, show a message
                messages.error(request, 'You are already enrolled in a course.')
                return redirect('register')
            
            # Save the student if they are not already enrolled
            form.save()
            messages.success(request, 'Student enrolled successfully.')
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'enrollment/register.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'enrollment/student_list.html', {'students': students})

def course_details(request, course_id):
    course = Course.objects.get(id=course_id)
    students = Student.objects.filter(course=course)
    return render(request, 'enrollment/course_details.html', {'course': course, 'students': students})

