from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from message.models import Message, File


def main(request):
    
    return render(request, "website/send_files.html")

def test(request):
    return HttpResponse("<h1>Hi this is the send files page</h1>")

