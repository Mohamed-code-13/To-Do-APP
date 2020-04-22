from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    objects = None
    text = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
