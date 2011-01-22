from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from transparencia.models import Etiqueta
from transparencia.models import ESTATUS_OPCIONES 


def etiqueta(request, slug, template_name='etiqueta.html'):
    etiqueta = get_object_or_404(Etiqueta, texto=slug)
    promesas = [promesaetiqueta.promesa for \
        promesaetiqueta in etiqueta.promesaetiqueta_set.all()]
    
    for promesa in promesas:
        promesa.personajes = [promesacargo.cargo for promesacargo in promesa.promesacargo_set.all()]

    scorecard_total = []
    scorecard_percent = []
    promesas_total = len(promesas)

    if promesas:
        for i in range(len(ESTATUS_OPCIONES)):
            scorecard_total.append(0)

        for promesa in promesas:
            scorecard_total[promesa.estatus] += 1

        for i in range(len(scorecard_total)):
            scorecard_percent.append((1.0 * scorecard_total[i] / promesas_total) * 100)

    scorecard = zip(scorecard_total, scorecard_percent)

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


def promesa(request, slug, template_name='promesa.html'):
    return HttpResponse("yo")

def personaje(request, slug, template_name='personaje.html'):
    return HttpResponse("yo")
