from django.contrib import admin
from .models import Anon, Plase, Gallery

# admin.site.register(Anon)
# admin.site.register(Plase)
# admin.site.register(Gallery)


class PlaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'post_title', 'is_published',)
admin.site.register(Plase, PlaseAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'is_published')
admin.site.register(Gallery, GalleryAdmin)


class AnonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'date')
    list_display_links = ('id', 'title')
    list_filter = (['title'])
    search_fields = ('title', 'description')
    list_per_page = 25

admin.site.register(Anon, AnonAdmin)