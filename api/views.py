from django.http import HttpResponse

from transparencia.models import Cargo, Personaje, Etiqueta

try: 
    import simplejson as json
except ImportError: 
    import json

TIPO_TAGS = (
    (0, Cargo),
    (1, Etiqueta),
)

# JSON helper functions
def JSONResponse(data, dump=True):
    return HttpResponse(
        json.dumps(data) if dump else data,
        mimetype='application/json',
    )

def buscar_tag(request):
    if 'term' in request.GET:
        term = request.GET['term']

        #Encontrar todos los personajes que empiezan con el term
        cargos = list(Cargo.objects.filter(titulo__istartswith=term))
        for personaje in Personaje.objects.filter(nombre__istartswith=term):
            cargos += personaje.cargo_set.all()
        
        # Quitar repeticiones
        cargos = set(cargos)

        tags = []
        for cargo in cargos:
            tags.append({
                'tipo': 0,
                'id': cargo.pk,
                'value': cargo.__unicode__(),
            })

        # Encontrar etiquetas que empiezan con el term
        etiquetas = Etiqueta.objects.filter(texto__istartswith=term)
        for etiqueta in etiquetas:
            tags.append({
                'tipo': 1,
                'id': etiqueta.pk,
                'value': etiqueta.texto,
                })

        return JSONResponse(tags)


def buscar_promesa(request):
    return HttpResponse("yo")
