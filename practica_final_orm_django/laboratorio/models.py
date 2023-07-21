from django.db import models
import datetime
# Create your models here.


annos_choices = []
for r in range(2015, (datetime.datetime.now().year+1)):
    annos_choices.append((r,r))


def anno_actual():
    return datetime.date.today().year



class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
    

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255, blank=True)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.IntegerField(choices=annos_choices, default=anno_actual)
    p_costo = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    p_venta = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.nombre