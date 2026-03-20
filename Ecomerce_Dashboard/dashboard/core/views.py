from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1> bienvenido al dashboard </h1><p> tu centro de control del e comerce </p>")

def about(request):
    return HttpResponse("<h1> Sobre nosotros</h1><p>Somos un sistema de gestion de e-comerce</p>")

def contact(request):
    return HttpResponse("<h1>Contacto</h1><p> email: info@dashboard.com</p>")

