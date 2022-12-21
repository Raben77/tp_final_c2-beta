from django.http import HttpResponse

def home(request): # pagina principal
    return HttpResponse("hola probando home")

def noticias(request):
    return HttpResponse("pagina de noticias")