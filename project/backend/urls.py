from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('roster', views.roster, name='roster'),
    path('about', views.about, name='about'),

###post_section
    path('createpost', views.createpost, name='createpost'),
    path('postdetail/<id>', views.postdetail, name='postdetail'),
    path('editpost/<id>', views.editpost, name='editpost'),
    path('deletepost/<id>', views.deletepost, name='deletepost'),

###event_section
    path('addevent',views.addevent, name='addevent'),
    path('eventdetail/<id>',views.eventdetail, name='eventdetail'),
    path('editevent/<id>',views.editevent, name='editevent'),
    path('deleteevent/<id>',views.deleteevent, name='deleteevent'),
    path('eventsignup/<id>',views.event_signup, name='event_signup'),
    path('eventcalendar', views.event_calendar.as_view(), name='event_calendar'),
]