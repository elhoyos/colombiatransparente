from django.http import HttpResponse

try: 
    import simplejson as json
except ImportError: 
    import json


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
        cargos = 


