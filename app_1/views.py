from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from app_1.models import Familiares

def listar_familia(request):
    #cargo template desde app_1
    plantilla=loader.get_template("mi_familia.html")
    #instanciar y consultamos todos los objetos agregados en la BD
    lista_familia = Familiares.objects.all()
    #retorno renderizo, establezco mi vista .html y envio diccionario con el objeto que contiene todos los datos de la BD. 
    return render(request,"mi_familia.html",{"lista_familia":lista_familia})