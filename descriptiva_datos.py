#! /usr/bin/env python3

# Proyecto 1 de Simulacion y modelos por Gabriel Diaz y Maria Fernanda Lopez

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

def descriptiva_datos():
  Archivo = "muestra.csv"
  lista = convertir_csv_en_lista_de_float(Archivo)

  resultados = []

  media = statistics.mean(lista)
  resultados.append(media)
  mediana = statistics.median(lista)
  resultados.append(mediana)
  moda = statistics.mode(lista)
  resultados.append(moda)
  varianza = statistics.variance(lista)
  resultados.append(varianza)
  desviacion_estandar = statistics.stdev(lista)
  resultados.append(desviacion_estandar)
  rango =  max(lista) - min(lista)
  resultados.append(rango)
  
  print(f"La Media es: {media}")
  print(f"La Mediana es: {mediana}")
  print(f"La Moda es: {moda}")
  print(f"La Varianza es: {varianza}")
  print(f"La Desviacion Estandar es: {desviacion_estandar}")
  print(f"Y el Rango es: {rango}")

  retorno = [lista, resultados]

  return retorno
  
if __name__ == '__main__':
  descriptiva_datos()