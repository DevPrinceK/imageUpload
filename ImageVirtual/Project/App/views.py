from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .models import *
# Create your views here.


def home(request):
    # pull database items and render on page
    return render(request, 'home.html', {})


def upload_img(request):
    # Handles the upload of images
    if (request.method == 'POST'):
        img_form = ImageForm(request.POST)
        if img_form.is_valid():
            img_form.save()
        else:
            # return HttpResponse(f'<h1>Didnt Validate  -- {img_form} </h1>')
            return render(request, 'upload.html', {})
    else:
        # return HttpResponse('<h1> Didnt save </h1>')
        return render(request, 'upload.html', {})


def login(request):
    # Credentials
    admin = 'kate'
    key = 'etak'

    # If the form is filled
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']

        if (user == admin) and (password == key):
            # queries all images from the database
            all_images = Image.objects.all
            return render(request, 'home.html', {'all_images': all_images})
        else:
            return render(request, 'login.html', {})
    # if the form is not filled
    else:
        return render(request, 'login.html', {})
