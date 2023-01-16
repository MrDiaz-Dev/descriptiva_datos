#!/usr/bin/env python3

#Carlos Bermudez 29668441 - Simulacion y modelos

from random import random 
import statistics as st
import csv
from collections import Counter

def simulacion_datos(file):
    with open(file, 'r') as f:
        
        lista = []
        alturas = []
        lector = csv.reader(f)
        # omite el encabezado

        for fila in lector:
            lista.append(list(map(float, fila)))

        for x in lista:
            alturas += x

        print()
        print(f"Numero de Datos: {len(alturas)}")
        num_datos = len(alturas)

        cou = Counter(alturas)

        print()

        print("Los Datos: ")
        datos = []
        for val in cou:
            datos.append(val)
            print(f"    {val}    ", end="-")
        print()

        print("Repeticion de los Datos: ")
        for val in cou:
            frec = (cou[val])
            print(f"     {frec}     ", end="-")
        print()

        print("Frecuencia de los Datos: ")
        frecuencias = []
        for val in cou:
            frec = ((cou[val])/(num_datos))
            frecuencias.append(frec)
            print(f"    {frec}    ", end="-")
        print()

        print("Promedio de la frecuencia de los Datos: ")
        for val in cou:
            frec = ((cou[val])*(10))
            print(f"    {frec}%    ", end="-")
        print()

        print("Frecuencia Acumulada de los Datos: ")
        frecuencias_acumuladas = []
        frec_acum = 0
        for i in frecuencias:
            frec_acum = frec_acum + i
            frecuencias_acumuladas.append(frec_acum)
            print(f"    {frec_acum}    ", end="-")
        print()
        
        print("Promedio de la frecuencia Acumulada de los Datos: ")
        frec_acum = 0
        for i in frecuencias:
            frec_acum = frec_acum + i
            print(f"    {(frec_acum)*100}%    ", end="-")
        print()
        print()

        contador = datos.copy()
        for a in range(len(contador)):
            contador[a] = 0

        num_iteraciones= 500
        for i in range(num_iteraciones):
            r=random()
            c=0
            #print(f"Numero random: {r}")
            for x in frecuencias_acumuladas: 
                if r <= x:
                    #print(f"Dato: {datos[c]}") 
                    #print(c)
                    contador[c] += 1
                    break
                c=c+1

        print("Simulacion de la variable alearia unas 500 iteraciones: ")
        for cont in range(len(contador)):
            ite = ((contador[cont])/(num_iteraciones))
            print(f"    {ite}    ", end="-")
        print()

        print("Promedio de la simulacion de la variable alearia unas 500 iteraciones: ")
        for cont in range(len(contador)):
            ite = ((contador[cont])/(num_iteraciones))
            print(f"    {(ite)*100}%    ", end="-")
        print()

        #<> 
        print()

if __name__ == "__main__":
    file = './csvVertical.csv'
    simulacion_datos(file)
