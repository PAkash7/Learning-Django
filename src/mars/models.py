from django.db import models
from django.utils import timezone

class MarsStatus(models.Model):
    human_status = models.CharField(max_length=100)
    water_status = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    moisture_status = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Mars Status at {self.timestamp}"

from django.contrib.auth.models import User

class Discovery(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

