from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    # blank=False, null=False mean is Notnull
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(max_length=1000, blank=False, null=False)
    time_create = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self): # Save a Post Like a TitleName
        return self.title