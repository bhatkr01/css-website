from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('roster', views.roster, name='roster'),
    path('about', views.about, name='about'),
    path('createpost', views.createpost, name='createpost'),
    path('eventsignup',views.event_signup, name='event_signup'),
    path('addevent',views.addevent, name='addevent'),
    path('eventcalendar', views.event_calendar.as_view(), name='event_calendar'),
]