from django.shortcuts import render, redirect

from accounts.forms import SignUpForm

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form=SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login(request):
   pass