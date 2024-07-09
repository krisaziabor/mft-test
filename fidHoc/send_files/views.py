from django.shortcuts import render, get_object_or_404, redirect
from message.models import Message, File

# Create your views here.
def insert_file(request):
    return render(request, "")