from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .models import Book
from .forms import BookForm


def home(request): 
    return render(request, 'home.html', {})

def login_user(request): 
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.success(request, ("Username atau Password salah ! Silahkan coba lagi.."))
            return redirect('login')
    else :
        return render(request, 'login.html', {})


def register_user(request):
    if request.method == "POST" :
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Berhasil Membuat Akun ! Silahkan Login.. "))
            return redirect('login')
    else : 
        form = RegisterUserForm()

    return render(request, 'register_user.html', {
        'form':form,
    })


def book(request): 
    submitted = False
    if request.method == "POST" :
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/yourbook?submitted=True')
    else : 
        form = BookForm
        if 'submitted' in request.GET :
            submitted = True

    return render(request, 'book.html', {'form' :form, 'submitted' : submitted})


def yourbook(request): 
    booking_mu = Book.objects.all()
    return render(request, 'yourbook.html', {'booking_mu' : booking_mu})


def jadwal(request) :
    return render(request, 'jadwal.html', {})

def detailjadwal(request) :
    return render(request, 'detailjadwal.html', {})

def about(request) :
    return render(request, 'about.html', {})

def help(request) :
    return render(request, 'help.html', {})