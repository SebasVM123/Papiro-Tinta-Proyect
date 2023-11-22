from main.models import *


def crear_registros():

    cliente.objects.create(nombre='juan camilo',
                           apellido='gomez',
                           )