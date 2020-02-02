from django.shortcuts import render
from .models import Anon, Plase, Gallery
from django.views.generic.base import View
from django.views.generic import ListView

def home(request):
    gallerys = Gallery.objects.all()
    plases = Plase.objects.all()
    anons = Anon.objects.all()
    context = {
        'plases': plases,
        'anons': anons,
        'gallerys': gallerys,
    }
    return render(request, 'general/base.html', context)

# class AnonsView(ListView):
#     """Список Анонсов"""
#     model = Anon
#     queryset = Anon.objects.filter()
#     #slug_field = "url"
#     #template_name = "include/anons/html"






