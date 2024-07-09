from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from .forms import UploadForm
# from message.models import Message, File


def main(request):
    
    return render(request, "send_files/send_files.html")

def test(request):
    return HttpResponse("<h1>Hi this is the send files page</h1>")

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})