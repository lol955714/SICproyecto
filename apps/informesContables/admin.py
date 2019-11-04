from django.contrib import admin
from apps.informesContables.models import *

admin.site.register(Empresa)
admin.site.register(Categoría)
admin.site.register(Factura)
admin.site.register(Insumo)
admin.site.register(Producto)
admin.site.register(LineaDeVenta)
admin.site.register(CategoriaCuentas)
admin.site.register(Cuenta)
admin.site.register(RegistroDebe)
admin.site.register(RegistroHaber)
admin.site.register(Transaccion)

