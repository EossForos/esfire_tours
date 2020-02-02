from django.db import models
from datetime import datetime
from PIL import Image

class Plase(models.Model):
    """Интерестные места"""
    image = models.ImageField("Изображение", default='default.jpg', upload_to='img/photo_main_pics')
    title = models.CharField("Заголовок", max_length=200)
    post_title = models.CharField("Пост-заголовок", max_length=200)
    description = models.TextField("Содержание", blank=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Интерестное место"
        verbose_name_plural = "Интерестные места"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 306 or img.width > 306:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Gallery(models.Model):
    """Галлерея"""
    photo = models.ImageField("Изображение", default='default.jpg', upload_to='img/gallery_pics')
    is_published = models.BooleanField("Опубликовано", default=True)

    def __del__(self):
        return self.photo

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"



class Anon(models.Model):
    """Анонсы Туров"""
    photo_main = models.ImageField("Изображение", default='default.jpg', upload_to='img/anons')
    title = models.CharField("Заголовок", max_length=200)
    date = models.CharField("Дата тура", max_length=200)
    description = models.TextField("Содержание", blank=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Анонс"
        verbose_name_plural = "Анонсы"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo_main.path)
        if img.height > 306 or img.width > 306:
            output_size = (700, 500)
            img.thumbnail(output_size)
            img.save(self.photo_main.path)

