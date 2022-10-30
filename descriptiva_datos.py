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

def descriptiva_datos(lista):

  resultados = []

  media = statistics.mean(lista)
  mediana = statistics.median(lista)
  moda = statistics.mode(lista)
  varianza = statistics.variance(lista)
  desviacion_estandar = statistics.stdev(lista)
  rango =  max(lista) - min(lista)

  resultados.append(media)
  resultados.append(mediana)
  resultados.append(moda)
  resultados.append(varianza)
  resultados.append(desviacion_estandar)
  resultados.append(rango)
  
  return resultados

def imprimir_descriptiva(lista):

  print("\n----------------------------------------DESCRIPTIVA----------------------------------------\n")

  print(f"La Media es: {lista[0]}")
  print(f"La Mediana es: {lista[1]}")
  print(f"La Moda es: {lista[2]}")
  print(f"La Varianza es: {lista[3]}")
  print(f"La Desviacion Estandar es: {lista[4]}")
  print(f"Y el Rango es: {lista[5]}")
  
  print("\n---------------------------------------FIN DECRIPTIVA--------------------------------------\n")
  
if __name__ == '__main__':
  lista = convertir_csv_en_lista_de_float("./muestra.csv")
  descriptiva = descriptiva_datos(lista)
  imprimir_descriptiva(descriptiva)