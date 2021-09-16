from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def login(request):
    # Credentials
    admin = 'kate'
    key = 'etak'

    # If the form is filled
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']

        if (user == admin) and (password == key):
            return render(request, 'home.html', {})
            # if the form is not filled
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})
