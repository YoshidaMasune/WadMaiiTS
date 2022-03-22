from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'login.html')

def createuser(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')