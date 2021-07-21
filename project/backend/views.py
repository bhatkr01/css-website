from django.shortcuts import render, redirect
from django.http import Http404
from .models import Post, Event
from accounts.models import MyUser
from backend.forms import PostForm, EventForm
from datetime import datetime, date, timedelta
from django.views import generic
from django.utils.safestring import mark_safe
from backend.calendar import Calendar
import calendar
# Create your views here.

def index(request):
    try: 
        allposts=Post.objects.all()
    except Post.DoesNotExist: 
        raise Http404("Post does not exist")
    
    return render(request, "backend/index.html", {"posts":allposts})
    

def roster(request):
    try:
       allusers=MyUser.objects.all()
    except MyUser.DoesNotExist: 
        raise Http404("User does not exist")
    
    return render(request, "backend/roster.html", {"users":allusers})
    
def event_signup(request):
   pass

def createpost(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:index')
    else:
        form=PostForm()
    return render(request, 'backend/newpost.html', {'form':form})


def about(request):
   return render(request, 'backend/about.html')


class event_calendar(generic.ListView):
    model=Event
    template_name='backend/event_calendar.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)

        d=get_date(self.request.GET.get('month', None))

        cal=Calendar(d.year, d.month)

        html_cal=cal.formatmonth(withyear=True)
        context['calendar']=mark_safe(html_cal)
        context['prev_month']=prev_month(d)
        context['next_month']=next_month(d)
        return context
    
def get_date(req_month):
    if req_month:
        year,month=(int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()    

def prev_month(d):
    first=d.replace(day=1)
    prev_month=first-timedelta(days=1)
    month='month='+str(prev_month.year)+'-'+str(prev_month.month)
    return month

def next_month(d):
    days_in_month=calendar.monthrange(d.year, d.month)[1]
    last=d.replace(day=days_in_month)
    next_month=last+timedelta(days=1)
    month='month='+str(next_month.year)+'-'+str(next_month.month)
    return month

def addevent(request):
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backend:event_calendar')
    else:
        form=EventForm()
    return render(request, 'backend/addevent.html', {'form':form})