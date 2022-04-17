from django.shortcuts import render
from .models import userFiles
from .forms import FileForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File Uploaded Successfully')
    form = FileForm()
    return render(request, 'upload_files.html', {'form': form})


def download(request):
    files = userFiles.objects.all()
    return render(request, 'download_files.html', {'files': files})
