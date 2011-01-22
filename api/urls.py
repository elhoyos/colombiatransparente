from django.conf.urls.defaults import *

urlpatterns = patterns('api.views',
    # GET API
    url(r'^buscar_tag.json$', 'buscar_tag'),
    url(r'^buscar_promesa.json$', 'buscar_promesa'),
)
