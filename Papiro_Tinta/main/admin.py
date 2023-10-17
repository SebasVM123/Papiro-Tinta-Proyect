from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(cliente)
admin.site.register(tarjeta)
admin.site.register(categoria)
admin.site.register(cliente_tarjeta)
admin.site.register(cliente_categoria)
