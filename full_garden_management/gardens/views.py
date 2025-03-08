from django.shortcuts import render
from django.http import HttpResponse
from .models import Plant

def home(request):
    plants = Plant.objects.all()
    return render(request, 'gardens/home.html', {'plants': plants})
