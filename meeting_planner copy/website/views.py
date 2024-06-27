from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.

def welcome(request):
    if request.user.is_authenticated:
        context = {"meetings": Meeting.objects.all()}
    else:
        context = {}
    return render(request, 'website/welcome.html', context)

def aboutme(request):
    return HttpResponse("Hi! My name is Kris Aziabor and I am learning Django through this app/course.")