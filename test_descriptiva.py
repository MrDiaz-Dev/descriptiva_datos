#! /usr/bin/env python3

# Modulo de Test para el Proyecto 1 de Simulacion y modelos por Gabriel Diaz y Maria Fernanda Lopez 

from tkinter import N
import unittest as test
import descriptiva_datos as desc


class test_descriptiva(test.TestCase):

  resultados = desc.descriptiva_datos()

  def test_media(self):
    mediaOptenida = self.resultados[1][0]
    numeros = 0
    for numero in self.resultados[0]:
      numeros = numeros + numero
    mediaEsperada =  numeros / len(self.resultados[0])
    self.assertEqual(mediaEsperada,mediaOptenida,"LAS MEDIAS SON DISTINTAS A LO ESPERADO")
    
  def test_mediana(self):
    medianaOptenida = self.resultados[1][1]
    resultados_ordenados = sorted(self.resultados[0])
    medianaEsperada = None
    if len(resultados_ordenados) % 2 == 0:
      aux = (resultados_ordenados[int(len(resultados_ordenados) / 2)] - resultados_ordenados[int(len(resultados_ordenados) / 2 - 1)]) / 2
      medianaEsperada = resultados_ordenados[int(len(resultados_ordenados) / 2 - 1)] + aux
    else:
      medianaEsperada = resultados_ordenados[(int(len(resultados_ordenados)) - 1) / 2 + 1]
    self.assertEqual(medianaEsperada,medianaOptenida,"LAS MEDIANAS SON DISTINTAS A LO ESPERADO")
    
if __name__ == '__main__':
  test.main()