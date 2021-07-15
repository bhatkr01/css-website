from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    try: 
        allposts=Post.objects.all()
    except Post.DoesNotExist: 
        raise Http404("Post does not exist")
    
    return render(request, "backend/index.html", {"posts":allposts})
    

def roster(request):

    try:
       allusers=User.objects.all()
    except User.DoesNotExist: 
        raise Http404("User does not exist")
    
    return render(request, "backend/roster.html", {"users":allusers})
    
def event_signup(request):
   pass
def signup(request):
   pass
def login(request):
   pass
def event_calendar(request):
   pass
