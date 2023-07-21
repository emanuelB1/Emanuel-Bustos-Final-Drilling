from django.test import TestCase
from django.urls import reverse

from .models import Laboratorio

class LaboratorioModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear datos de prueba para el modelo Laboratorio
        Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Ciudad 1', pais='País 1')
        Laboratorio.objects.create(nombre='Laboratorio 2', ciudad='Ciudad 2', pais='País 2')

    def test_datos_de_prueba(self):
        # Verificar los datos 
        laboratorio_1 = Laboratorio.objects.get(nombre='Laboratorio 1')
        laboratorio_2 = Laboratorio.objects.get(nombre='Laboratorio 2')
        self.assertEqual(laboratorio_1.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio_2.ciudad, 'Ciudad 2')

    def test_url_laboratorio(self):
        """
        Verificar que la URL de laboratorio devuelve una respuesta HTTP 200, en este caso mi es mi pagina principal del proyecto:
        path('', views.mostrar, name='mostrar'), por lo tanto no viene nada despues del localhost.
        por esto puse el nombre de la url, puesto que de otra forma me arrojaba error ya que no acepta; '', '/' ni tampoco '//'.
        """
        url = reverse('mostrar')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_pagina_laboratorio(self):
        # Verificar que la página de laboratorio usa la plantilla correcta y tiene el contenido esperado
        url = reverse('mostrar')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'mostrar.html')
        self.assertContains(response, 'Laboratorio 1')
        self.assertContains(response, 'Laboratorio 2')

