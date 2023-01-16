#! /usr/bin/env python3

# Proyecto 2 de Simulacion y modelos por Gabriel Diaz

import csv

from collections import Counter
from random import random

def convertir_csv_en_lista_de_float(archivo_csv):
  lista = []
  with open(archivo_csv, newline='') as Archivo:  
      reader = csv.reader(Archivo)
      for elemento in reader:
        nuevo_elemento = float(elemento[0])
        lista.append(nuevo_elemento) 
  return lista

def tabular(z):
  datos = convertir_csv_en_lista_de_float('./csvVertical.csv')
  datosContados = Counter(datos)
  datosPorcentaje = {}

  for clave in datosContados:
    n = datosContados[clave] / len(datos)
    n = round(n, 2)
    datosPorcentaje[clave] = n
  
  acumumulada = {}
  anterior = 0
  for i in datosPorcentaje:
    n = datosPorcentaje[i] + anterior
    n = round(n, 2)
    acumumulada[i] = n
    anterior = n

  simulacion = {}
  for clave in acumumulada:
    simulacion[clave] = 0

  for i in range(z):
    r = random()
    for clave in acumumulada:
      if r < acumumulada[clave]:
        simulacion[clave] = simulacion[clave] + 1
        break
  
  for clave in simulacion:
    simulacion[clave] = round(simulacion[clave] / z, 2)

  print('----------------------------------')
  print('DATOS CONTADOS:')
  for clave in datosContados:
    print(clave, ' ---> ', datosContados[clave])

  print('----------------------------------')
  print('DATOS PORCENTAJE:')
  for clave in datosPorcentaje:
    print(clave, ' ---> ', round(datosPorcentaje[clave]*100, 2), '%')

  print('----------------------------------')
  print('DATOS PORCENTAJE ACUMULADO:')
  for clave in acumumulada:
    print(clave, ' ---> ', round(acumumulada[clave]*100, 2), '%')

  print('----------------------------------')
  print('SIMULACION CON VARIABLE ALEATORIA EN ', z , ' ITERACIONES:')
  for clave in acumumulada:
    print(clave, ' ---> ', round(simulacion[clave]*100, 2), '%')
  

tabular(10000)