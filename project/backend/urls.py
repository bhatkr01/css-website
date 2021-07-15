from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('roster', views.roster, name='roster'),
    path('eventsignup',views.event_signup, name='event_signup'),
    path('signup', views.signup, name='signup'),
    path('login', views.login,name='login'), 
    path('eventcalendar', views.event_calendar, name='event_calendar'),
]