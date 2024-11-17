from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Description
from django.contrib import messages

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('add_course')
        else:
            description = Description.objects.create(content=request.POST['description_content'])
            Course.objects.create(name=request.POST['name'], description=description)
            return redirect('index')
    return render(request, 'add_course.html')

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('index')
    return render(request, 'delete_course.html', {'course': course})