from django.contrib import admin
from .models import Anon, Plase, Gallery



@admin.register(Plase)
class PlaseAdmin(admin.ModelAdmin):
    """Интересные места"""
    list_display = ('id', 'title', 'post_title', 'image', 'is_published',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """Фотогалерея"""
    list_display = ('id', 'photo', 'is_published')


@admin.register(Anon)
class AnonAdmin(admin.ModelAdmin):
    """Анонсы туров"""
    list_display = ('id', 'title', 'is_published', 'date')
    list_display_links = ('id', 'title')
    list_filter = (['title'])
    search_fields = ('title', 'description')
    list_per_page = 25
