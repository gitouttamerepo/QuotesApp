from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

quotes = [
    {
        'author': 'Carl Jung',
        'content': 'To be or not to be ...',
        'description': 'Honestly this quotes goes hard fr fr ong',
        'extraction': 'The Stoic Reader'
    }
]

def home(request):
    context = {
        'quotes': quotes
    }
    return render(request, 'quote/home.html', context)

def about(request):
    return render(request, 'quote/about.html')