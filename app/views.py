# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import central, inventario, NE, resumen_x_modelo, cluster, casos

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

def domain(request):

    nes=inventario.objects.all().order_by('-casos')
    total = inventario.objects.count()
    rxm = resumen_x_modelo.objects.all()
    clus = cluster.objects.count()
    cas = casos.objects.count()
    return render(request, "domain.html", {"nes":nes, "total":total, "rxm":rxm, "cluster":clus,"casos":cas} )

def maps(request):
    #nes = central.objects.all().exclude(localizacion='')
    nes = central.objects.raw("SELECT c.id, (c.nombre||' br '||string_agg(ne.clli, ', ')) as nombre, c.localizacion as nes FROM public.app_central c inner join public.app_ne ne on ne.central_id = c.id where c.localizacion <> '' group by c.id,c.nombre,c.localizacion");
    return render(request, "maps.html", {'nes':nes})

def moreinfo(request,id):
    ne=inventario.objects.get(id=id)
    return render(request,"moreinfo.html",{'ne':ne})

def inventory(request,id):
    return render(request,"inventory.html")

def SRs(request,id):
    return render(request,"SRs.html")