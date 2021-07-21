from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    post_title=models.CharField(max_length=100)
    post_content=models.TextField()
    pub_date=models.DateTimeField()
    author_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post_title}--{self.pub_date}--{self.author_id}"


class Event(models.Model):
    event_title=models.CharField(max_length=100)
    event_description=models.TextField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def __str__(self):
        return f"{self.event_title}--{self.event_description}--{self.start_time}--{self.start_time}"

    # def check_overlap(self, original_start, original_end, new_start, new_end):
    #     overlap=False
    #     if new_start==original_end or new_end==original_start:
    #         overlap=False
    #     elif(new_start>=original_start and new_start<=original_end) or (new_end>=original_start and new_end<=original_end):
    #         overlap=True
    #     elif new_start<=original_start and new_end>=original_end:
    #         overlap=True

