from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import SignUpForm

def sign_up(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:log_in')
    else:
        form=SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})

def log_in(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('backend:index') 
        else:
            return render(request, 'accounts/login.html', {'message':"Invalid Credentials. Please try again."}) 
    return render(request, 'accounts/login.html')

def log_out(request):
    logout(request)
    return redirect('backend:index')


def profile(request):
   pass