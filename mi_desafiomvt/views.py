from django.http import HttpResponse
from django.template import Template, Context, loader

def familia(request):
    #Abro el documento que contiene al template
    template_ext = loader.get_template('familia.html')
    #Renderizo template
    documento = template_ext.render()
    return HttpResponse(documento)