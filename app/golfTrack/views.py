from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Course

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'golfTrack/index.html', context)

def course_list(request):
    courses = Course.objects.all()
    output = ', '.join([c.__str__() for c in courses])
    return HttpResponse(output)

def course_detail(request, course_id):
    course = Course.objects.all()[course_id-1]
    output = course.__str__()
    return HttpResponse("You're looking at course %s." % output)