from django.shortcuts import render
from django.urls import path, include

# Create your views here.

def main(request):

    salida = {
        'owner': 'Isael Diroche D.',
    }

    return render(request, 'Home/index.html', salida)