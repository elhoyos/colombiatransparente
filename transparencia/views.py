from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from transparencia.models import Etiqueta
from transparencia.models import ESTATUS_OPCIONES 

def crear_scorecard(promesas):
    if not promesas:
        empty_scorecard = []
        for i in range(len(ESTATUS_OPCIONES)):
            empty_scorecard.append((0, 0))
        return empty_scorecard

    scorecard_total = []
    scorecard_percent = []
    promesas_total = len(promesas)

    for i in range(len(ESTATUS_OPCIONES)):
        scorecard_total.append(0)

    for promesa in promesas:
        scorecard_total[promesa.estatus] += 1

    for i in range(len(scorecard_total)):
        scorecard_percent.append((1.0 * scorecard_total[i] / promesas_total) * 100)

    return zip(scorecard_total, scorecard_percent)

def index(request):
    return HttpResponse("yo")


def etiqueta(request, slug, template_name='etiqueta.html'):
    etiqueta = get_object_or_404(Etiqueta, texto=slug)
    promesas = [promesaetiqueta.promesa for \
        promesaetiqueta in etiqueta.promesaetiqueta_set.all()]
    
    for promesa in promesas:
        promesa.cargos = [promesacargo.cargo for promesacargo in promesa.promesacargo_set.all()]

    scorecard = crear_scorecard(promesas)

    context = {
        'etiqueta': etiqueta,
        'promesas': promesas,
        'scorecard': scorecard,
    }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request),
    )


def personaje(request, slug, template_name='personaje.html'):
    personaje = get_object_or_404(Personaje, slug=slug)
    promesas = [promesacargo.promesa for \
        promesacargo in personaje.promesacargo_set.all()]
    #cargos = personaje.cargos_set.all()

    context = {
       # 'etiqueta': etiqueta,
        #'promesas': promesas,
        #'scorecard': scorecard,
    }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request),
    )

    return HttpResponse("yo")


def promesa(request, slug, template_name='promesa.html'):
    return HttpResponse("yo")


# TEMP

def desarrolladores(request):
    return HttpResponse("yo")

def sobre(request):
    return HttpResponse("yo")

def patrocinadores(request):
    return HttpResponse("yo")

def contactenos(request):
    return HttpResponse("yo")
