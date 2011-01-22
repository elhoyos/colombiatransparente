from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from transparencia.views import etiqueta, promesa, personaje

urlpatterns = patterns('',
    url(r'^etiqueta/(?P<slug>[-\w]+)/$', etiqueta, name='etiqueta'),
    url(r'^promesa/(?P<slug>[-\w]+)/$', promesa, name='promesa'),
    url(r'^personaje/(?P<slug>[-\w]+)/$', personaje, name='personaje'),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

import settings 

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 
            'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    )
