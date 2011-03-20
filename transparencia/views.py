from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from transparencia.models import Etiqueta, Personaje, Cargo, Promesa
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

def index(request, template_name='index.html'):
    promesas = Promesa.objects.all()[:10]

    context = {
        'promesas': promesas, 
    }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request),
    )

def etiqueta(request, slug, template_name='etiqueta.html'):
    etiqueta = get_object_or_404(Etiqueta, texto=slug)
    promesas = [promesaetiqueta.promesa for \
        promesaetiqueta in etiqueta.promesaetiqueta_set.all()]
    
    for promesa in promesas:
        promesa.cargos = [promesacargo.cargo for promesacargo in promesa.promesacargo_set.all()]

    scorecard = crear_scorecard(promesas)

    context = {
        'id': etiqueta.id,
        'titulo': etiqueta,
        'etiquetas': [etiqueta,],
        'descripcion': etiqueta.descripcion,
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
    personaje.cargos = personaje.cargo_set.all()
    try:
        personaje.cargoactual = personaje.cargos.get(actual=True)
    except Cargo.DoesNotExist:
        pass

    promesas = []
    for cargo in personaje.cargos:
        promesas += [promesacargo.promesa for \
            promesacargo in cargo.promesacargo_set.all()]

    for promesa in promesas:
        promesa.cargos = [promesacargo.cargo for promesacargo in promesa.promesacargo_set.all()]

    scorecard = crear_scorecard(promesas)

    context = {
        'id': personaje.id,
        'titulo': personaje.nombre,
        'etiquetas': [personaje.nombre,],
        'descripcion': personaje.descripcion,
        'image': personaje.image,
        'personaje': personaje,
        'promesas': promesas,
        'scorecard': scorecard,
    }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request),
    )


def promesa(request, slug, template_name='promesa.html'):
    promesa = get_object_or_404(Promesa, slug=slug)
    promesa.diferencia = promesa.arriba - promesa.abajo
    promesa.cargos = [promesacargo.cargo for promesacargo in promesa.promesacargo_set.all()]
    etiquetas = [promesaetiqueta.etiqueta for \
        promesaetiqueta in promesa.promesaetiqueta_set.all()]

    context = {
        'id': promesa.id,
        'titulo': promesa.titulo,
        'etiquetas': etiquetas,
        'descripcion': promesa.descripcion,
        'promesa': promesa,
        'etiquetas': etiquetas,
    }
    return render_to_response(
        template_name,
        context,
        context_instance = RequestContext(request),
    )


def desarrolladores(request):
    return HttpResponse("yo")

def sobre(request):
    return HttpResponse("yo")

def patrocinadores(request):
    return HttpResponse("yo")

def contactenos(request):
    return HttpResponse("yo")
