from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('homepage')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('homepage')
    else:
        pass
