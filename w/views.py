from django.shortcuts import render
from .models import *
# Create your views here.

def courses(request):
    courses = Course.objects.all()
    return render(request, 'home.html', context={'courses' : courses})


def modules(request):
    course = request.GET.get('course')
    modules = Module.objects.filter(course=course)
    return render(request, 'home.html', context={'modules':modules})  

def rooms(request):
    modules = request.GET.get('modules')
    rooms = Room.objects.filter(modules=modules)
    return render(request, 'modules.html', context={'rooms':rooms})  