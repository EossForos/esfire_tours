from django.contrib import admin
from .models import Anon, Plase, Gallery

class PlaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'post_title', 'is_published',)
admin.site.register(Plase, PlaseAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'is_published')
admin.site.register(Gallery, GalleryAdmin)


class AnonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'date_posted')
    list_display_links = ('id', 'title')
    list_filter = (['title'])
    list_editable = (['date_posted'])
    search_fields = ('title', 'description')
    list_per_page = 25

admin.site.register(Anon, AnonAdmin)