from django.http import HttpResponse
from django.template import Template, Context

def pag_principal(request): # pagina principal

    doc_externo=open("E:/Proyecto_info/Proyecto_final_c2/ab_tejiendo/ab_tejiendo/plantillas/home.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    home1=plt.render(ctx)


    return HttpResponse(home1)

def pag_noticias(request):
    return HttpResponse("pagina de noticias")