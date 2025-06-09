from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Bienvenidos a mi app hecha en Django!"}
    return render(request, "myapp/index.html", context)
def contenido(request):
    context = {"llamada": "Este es el contenido de la app"}
    return render(request, "myapp/contenido.html", context)