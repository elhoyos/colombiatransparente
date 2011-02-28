from django.conf.urls.defaults import *

urlpatterns = patterns('api.views',
    url(r'^markdown/preview/$', 'markdown_preview'),
    url(r'^buscar_tags.json$', 'buscar_tags'),
    url(r'^buscar_promesas/$', 'buscar_promesas'),
)
