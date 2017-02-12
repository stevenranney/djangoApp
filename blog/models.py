from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    color = ColorField(default = '#8B4513')
    text = models.TextField()
    movement_date = models.DateTimeField(blank = True, null = True)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

