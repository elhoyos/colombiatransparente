from django import template

from ..transparencia.models import ESTATUS_OPCIONES

register = template.Library()

@register.filter
def estatus(value):
    try:
        estatus = ESTATUS_OPCIONES[value][1]
    except IndexError:
        estatus = "Estatus fuera de rango"
    return estatus
