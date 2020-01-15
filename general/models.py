from django.db import models
from datetime import datetime

class Anon(models.Model):
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title