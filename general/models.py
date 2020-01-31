from django.db import models
from datetime import datetime
from PIL import Image

class Plase(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='photo_main_pics')
    title = models.CharField(max_length=200)
    post_title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 306 or img.width > 306:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Gallery(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __getitem__(self, item):
        return self.photo

class Anon(models.Model):
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title