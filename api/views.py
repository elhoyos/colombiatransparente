from django.db.models import F
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt

from transparencia.models import Cargo, Personaje, Etiqueta, Promesa

try: 
    import simplejson as json
except ImportError: 
    import json

from markdown import markdown

TIPO_TAGS = {
    Cargo: 0,
    Etiqueta: 1,
}

def JSONResponse(data, dump=True):
    return HttpResponse(
        json.dumps(data) if dump else data,
        mimetype='application/json',
    )

@csrf_exempt
def markdown_preview(request):
    processed = ''
    if request.method == 'POST':
        processed = markdown(escape(request.POST.get('data')), ['footnotes',])
    return HttpResponse(processed)

def buscar_tags(request):
    if request.is_ajax() and 'q' in request.GET:
        q = request.GET['q']

        #Encontrar todos los personajes que contienen el term
        cargos = list(Cargo.objects.filter(titulo__icontains=q))
        for personaje in Personaje.objects.filter(nombre__icontains=q):
            cargos += personaje.cargo_set.all()
        
        cargos = set(cargos)

        tags = []
        for cargo in cargos:
            tags.append({
                'tipo': 0,
                'id': cargo.pk,
                'value': cargo.__unicode__(),
            })

        # Encontrar etiquetas que contienen el term
        etiquetas = Etiqueta.objects.filter(texto__icontains=q)
        for etiqueta in etiquetas:
            tags.append({
                'tipo': 1,
                'id': etiqueta.pk,
                'value': etiqueta.texto,
                })

        return JSONResponse(tags)

def buscar_promesas(request):
    # 1. Poner la interseccion de terminos al principio
    # 2. Tener en cuenta relevancia

    if request.is_ajax() and 'q' in request.GET:
        q = json.loads(request.GET['q'])

        promesas = []
        for tag in q:
            if tag['tipo'] == TIPO_TAGS[Cargo]:
                try:
                    cargo = Cargo.objects.get(pk=tag['id'])
                except Cargo.DoesNotExist:
                    continue
                promesas += [promesacargo.promesa for \
                    promesacargo in cargo.promesacargo_set.all()]
            elif tag['tipo'] == TIPO_TAGS[Etiqueta]:
                try:
                    etiqueta = Etiqueta.objects.get(pk=tag['id'])
                except Etiqueta.DoesNotExist:
                    continue
                promesas += [promesaetiqueta.promesa for \
                    promesaetiqueta in etiqueta.promesaetiqueta_set.all()]

        for promesa in promesas:
            promesa.cargos = [promesacargo.cargo for \
                promesacargo in promesa.promesacargo_set.all()]

        promesas = set(promesas)
        
        t = get_template('includes/lista_promesas.html')
        html = t.render(Context({'promesas': promesas}))
        
        return HttpResponse(html)


# registra un evento like/unlike del boton 'like' de facebook en una 
# promesa
# siempre retornara cero
def registrar_evento_likebtn(request):
    if request.is_ajax(): 
        if 'id' not in request.POST or \
           'type' not in request.POST or \
           'like' not in request.POST:
            return JSONResponse(0)
            
        id = request.POST['id']
        elementtype = request.POST['type']
        like = request.POST['like']
        
        import sys
        sys.stderr.write(like)
        
        if elementtype == '0': 
            try:
                promesa = Promesa.objects.get(id=id)
            except DoesNotExist:
                return JSONResponse(0)

            if like == 'true':
                promesa.arriba = F('arriba') + 1
            else:
                promesa.abajo = F('abajo') + 1

            promesa.save()

            return JSONResponse(0)
            
        return JSONResponse(0)
