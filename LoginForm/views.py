from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def loginView(request):
    form = LoginForm()
    context = {
        "heading":"Login",
        "form":form
    }
    if request.method == "POST":
        nama = request.POST["username"]
        sandi = request.POST["password"]
        akun = authenticate(username=nama, password=sandi)
        if akun is not None:
            login(request,akun)
            return redirect("blog")
    return render(request,'login.html',context)

def logoutView(request):
    logout(request)
    return redirect("login")

def blog(request):
    context = {
        "heading":"Blog"
    }
    return render(request,"blog.html",context)