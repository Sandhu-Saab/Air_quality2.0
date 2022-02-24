from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#from . models import Contect

# Create your views here.


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')
