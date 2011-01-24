from django.conf.urls.defaults import *

urlpatterns = patterns('api.views',
    # GET API
    url(r'^buscar_tags.json$', 'buscar_tags'),
    url(r'^buscar_promesas/$', 'buscar_promesas'),
)
