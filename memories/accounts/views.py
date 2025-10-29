from django.shortcuts import render, get_object_or_404, redirect
from django. contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')