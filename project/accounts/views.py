from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from accounts.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from backend.models import Post, Event 
from accounts.models import MyUser
from django.urls import reverse

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

@login_required(login_url='accounts/login/')
def profile(request):
    user=request.user
    posts=Post.objects.filter(author_id__email=user.email)
    context={
        'posts':posts,
        'user':user
    }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='accounts/login/')
def editaccount(request, id):
    user=get_object_or_404(MyUser,id=id)
    form=SignUpForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect(reverse('accounts:profile', kwargs={"id":id}))
    return render(request, 'accounts/editaccount.html', {'form':form})

@login_required(login_url='accounts/login/')
def deleteaccount(request, id):
    user=get_object_or_404(MyUser,id=id)
    user.delete()
    return render(request, 'backend/index.html')