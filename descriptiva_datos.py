#! /usr/bin/env python3

from lib2to3.pytree import convert
import statistics
import csv

def convertir_csv_en_lista_de_float(archivo_csv):
  lista = []
  with open(archivo_csv, newline='') as Archivo:  
      reader = csv.reader(Archivo)
      for fila in reader:
          for elemento in fila:
            nuevo_elemento = float(elemento)
            lista.append(nuevo_elemento)
  return lista

def descriptiva_datos(lista):
  cuatro_decimales = 10/3

  media = statistics.mean(lista)
  mediana = statistics.median(lista)
  moda = statistics.mode(lista)
  varianza = statistics.variance(lista)
  desviacion_estandar = statistics.stdev(lista)
  rango =  max(lista) - min(lista)
  
  print(f"La Media es: {media}")
  print(f"La Mediana es: {mediana}")
  print(f"La Moda es: {moda}")
  print(f"La Varianza es: {varianza}")
  print(f"La Desviacion Estandar es: {desviacion_estandar}")
  print(f"Y el Rango es: {rango}")

if __name__ == '__main__':
  Archivo = "muestra.csv"
  lista = convertir_csv_en_lista_de_float(Archivo)
  descriptiva_datos(lista)
