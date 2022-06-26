from django.shortcuts import render
from .models import Individual

# Create your views here.

def index(request):

    inds = Individual.objects.all()

    return render(request, 'index.html', {'inds' : inds})