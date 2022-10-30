#! /usr/bin/env python3

# Modulo de Test para el Proyecto 1 de Simulacion y modelos por Gabriel Diaz y Maria Fernanda Lopez 

import re
from tkinter import N
import unittest as test
import descriptiva_datos as desc
import csv


class test_descriptiva(test.TestCase):

  entradas = []
  resultados_esperados = []

  with open("./test_entradas.csv", newline='') as Archivo:  
      reader = csv.reader(Archivo)
      for fila in reader: 
        intro = [] 
        for elemento in fila:
          nuevo_elemento = float(elemento)
          intro.append(nuevo_elemento) 
        entradas.append(intro)

  with open("./test_salidas.csv", newline='') as Archivo:
      reader = csv.reader(Archivo)
      for fila in reader: 
        resultados = [] 
        for elemento in fila:
          nuevo_elemento = float(elemento)
          resultados.append(nuevo_elemento) 
        resultados_esperados.append(resultados)

  def test_media(self):
    n = 0
    for entrada in self.entradas:
      print("comparando resultados...")
      resultados_optenidos = desc.descriptiva_datos(entrada)
      m = 0
      for resultado_optenido in resultados_optenidos:
        self.assertAlmostEqual(resultado_optenido, self.resultados_esperados[n][m],3,"EL RESULTADO NO ES EL ESPERADO")
        m = m + 1
      n = n + 1
      print("listo, sin problemas")
    
if __name__ == '__main__':
  test.main()