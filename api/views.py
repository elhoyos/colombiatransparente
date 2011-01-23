from django.http import HttpResponse

from transparencia.models import Cargo, Personaje, Etiqueta

try: 
    import simplejson as json
except ImportError: 
    import json

"""
TIPO_TAGS = {
    Cargo: 0,
    Etiqueta: 1,
}
"""

# JSON helper functions
def JSONResponse(data, dump=True):
    return HttpResponse(
        json.dumps(data) if dump else data,
        mimetype='application/json',
    )

def buscar_tags(request):
    if request.is_ajax() and 'q' in request.GET:
        q = request.GET['q']

        #Encontrar todos los personajes que contienen el term
        cargos = list(Cargo.objects.filter(titulo__icontains=q))
        for personaje in Personaje.objects.filter(nombre__icontains=q):
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
    #if request.is_ajax() and 'q' in request.GET:
    if 'q' in request.GET:
        q = request.GET['q']
        data = {}
        return JSONResponse(data)
