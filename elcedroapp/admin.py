from django.contrib import admin
from elcedroapp.models import Pedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion','numero','cantidad_bidones')
    search_fields = ('nombre',)

admin.site.register(Pedido, PedidoAdmin)