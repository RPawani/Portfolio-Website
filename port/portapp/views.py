from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import cform, pform, sform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return HttpResponse('WELCOME TO HOME PAGE')


def cand(request):
    form = None
    if request.method == "POST":
        form = cform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/project')
        else:
            pass
    else:
        form = cform()
    return render(request, 'reg.html', {'form': form})

def proj(request):
    form = None
    if request.method == 'POST':
        form = pform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/skills')
        else:
            pass
    else:
        form = pform()
    return render(request, 'project.html', {'form': form})

def skil(request):
    form = None
    if request.method == "POST":
        form = sform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            pass
    else:
        form = sform()
    return render(request, 'skill.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            return HttpResponse('Invalid Username')

        user = authenticate(username=username, password=password)

        if user is None:
            login(request, user)
            return redirect('/home')

        else:
            return redirect('/login')



    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name', not None)
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username Already Exists')
            return redirect('/login')
        user.set_password(password)
        user.save()
        # messages.info(request, 'Account is succefully Created')
        return redirect('/login')
    return render(request,'signup.html')
