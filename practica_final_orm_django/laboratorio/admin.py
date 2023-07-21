
from django.contrib import admin
from .models import DirectorGeneral, Laboratorio, Producto
# Register your models here.


class LaboratorioAdmin(admin.ModelAdmin):
    fields = ['nombre', 'ciudad', 'pais']
    list_display = ('id', 'nombre')
    list_display_links = ['nombre']
    ordering = ('id',)

class DirectorGeneralAdmin(admin.ModelAdmin):
    fields = ['nombre', 'laboratorio']
    list_display = ('id', 'nombre', 'laboratorio')
    list_display_links = ['nombre', 'laboratorio']
    ordering = ('nombre',)
    


class ProductoAdmin(admin.ModelAdmin):
    fields = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_display_links = ['nombre', 'laboratorio']
    list_filter = ('nombre', 'laboratorio',)
    ordering = ('nombre', 'laboratorio',)
    list_per_page = 3
  




admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Producto, ProductoAdmin)


