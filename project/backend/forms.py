from django.forms import ModelForm, DateInput
from backend.models import Event, Post

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['post_title', 'post_content', 'pub_date', 'author_id']

class EventForm(ModelForm):
    class Meta:
        model=Event
        widgets={
            'start_time':DateInput(format='%Y-%m-%dT%H:%M',  attrs={'placeholder':'Select a date', 'type':'datetime-local'}),
            'end_time':DateInput(format='%Y-%m-%dT%H:%M',  attrs={'placeholder':'Select a date', 'type':'datetime-local'}),
        }
        fields = '__all__'