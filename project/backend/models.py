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



