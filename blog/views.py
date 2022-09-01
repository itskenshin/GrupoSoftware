from django.shortcuts import render
# from django.contrib.auth.models import User

# Esto hasta lo puedo quitar porque no estoy haciendo nada
from blog.models import *

# Create your views here.

# Le puedo cambiar el nombre a Main o algo asi
def blog(request):
    # posts = Post.objects.all() Esto era una tabla de la BD
    return render(request, "blog/blog-main.html")