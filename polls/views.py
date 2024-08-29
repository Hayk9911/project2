from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
# Create your views here.


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/detail.html', {'course': course})

def rate_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        new_rating = float(request.POST['rating'])
        course.rate = (course.rate * course.count + new_rating) / (course.count + 1) 
        course.count += 1
        course.save()
        return redirect('course_detail', pk=pk)
    return render(request, 'courses/rate.html', {'course': course})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('course_list')
    else:
        form = UserCreationForm()
    return render(request, 'courses/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('course_list')
    else:
        form = AuthenticationForm()
    return render(request, 'courses/login.html', {'form': form})


