from django.contrib import admin
from .models import Banco, BancoPais, Cuenta, Tarjeta

# Register your models here.
class BancoAdmin(admin.ModelAdmin):
    list_display = ('id_banco', 'nombre', 'create', 'update')
    search_fields = ('nombre',)
    list_filter = ('create', 'update')


class BancoPaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'banco', 'pais', 'create', 'update')
    list_filter = ('banco', 'pais')


class CuentaAdmin(admin.ModelAdmin):
    list_display = ('id_cuenta', 'usuario', 'banco', 'saldo', 'tipo', 'moneda', 'fecha_creacion', 'create', 'update')
    list_filter = ('tipo', 'banco', 'moneda', 'create', 'update')


class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('id_tarjeta', 'cuenta', 'banco', 'numero', 'marca', 'fecha_expiracion', 'limite_credito', 'create', 'update')
    list_filter = ('banco', 'marca', 'fecha_expiracion', 'create', 'update')



admin.site.register(Banco, BancoAdmin)
admin.site.register(BancoPais, BancoPaisAdmin)
admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Tarjeta, TarjetaAdmin)
