from django.http import HttpResponse
from django.template import Template, Context

def familia(request):
    #Abro el documento que contiene al template
    template_ext = open("/home/sebx3/Documentos/CURSO_CODER_PYTHON/python/desafio_mvt/mi_desafiomvt/mi_desafiomvt/templates/familia.html")
    #Cargo el documento en una variable de tipo "Template"
    template = Template(template_ext.read())
    #Cierro el documento
    template_ext.close()
    #Creo el contexto
    contexto = Context()
    #Renderizo template
    documento = template.render(contexto)
    return HttpResponse(documento)