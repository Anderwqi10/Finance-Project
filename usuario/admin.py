from django.contrib import admin
from .models import Usuario, Moneda, Pais
# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'rol')

class MonedaAdmin(admin.ModelAdmin):
    list_display = ('id_moneda', 'nombre')

class PaisAdmin(admin.ModelAdmin):
    list_display = ('id_pais', 'nombre', 'moneda__nombre')
   

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Moneda, MonedaAdmin)
admin.site.register(Pais, PaisAdmin)