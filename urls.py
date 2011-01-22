from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from transparencia.views import index, etiqueta, promesa, personaje

# TEMP
from transparencia.views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^etiqueta/(?P<slug>[-\w]+)/$', etiqueta, name='etiqueta'),
    url(r'^promesa/(?P<slug>[-\w]+)/$', promesa, name='promesa'),
    url(r'^personaje/(?P<slug>[-\w]+)/$', personaje, name='personaje'),
    (r'^api/', include('api.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    # TEMPORARY
    url(r'^desarrolladores$', desarrolladores, name='desarrolladores'),
    url(r'^sobre$', sobre, name='sobre'),
    url(r'^patrocinadores$', patrocinadores, name='patrocinadores'),
    url(r'^contactenos$', contactenos, name='contactenos'),

)

import settings 

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 
            'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    )
