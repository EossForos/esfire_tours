from django.shortcuts import render
from .models import Anon, Plase, Gallery

def home(request):
    gallerys = Gallery.objects.all()
    plases = Plase.objects.all()
    anons = Anon.objects.all()
    context = {
        'plases': plases,
        'anons': anons,
        'gallerys': gallerys,
    }
    return render(request, 'general/home.html', context)
