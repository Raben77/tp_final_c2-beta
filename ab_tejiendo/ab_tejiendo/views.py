from django.http import HttpResponse

def home(request): # pagina principal
    return HttpResponse("hola probando home")
    