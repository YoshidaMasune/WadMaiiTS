from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def signin(request):
    
    email = request.POST['email']
    password = request.POST['password']

    return render(request, 'login.html',)

def register(request):
    return render(request, 'register.html')

def createuser(request):

    username = request.POST['username']
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.create_user(
        username = username,
        first_name =first_name,
        last_name = last_name,
        email = email,
        password = password,
        )
    user.save()
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')