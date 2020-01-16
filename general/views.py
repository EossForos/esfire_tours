from django.shortcuts import render
from .models import Anon, Plase

def home(request):
    plases = Plase.objects.all()
    anons = Anon.objects.all()
    context = {
        'plases': plases,
        'anons': anons,
    }
    return render(request, 'general/home.html', context)
