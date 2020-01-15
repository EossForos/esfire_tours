from django.shortcuts import render
from .models import Anon

def home(request):
    anons = Anon.objects.all()
    context = {
        'anons': anons
    }
    return render(request, 'general/home.html', context)
