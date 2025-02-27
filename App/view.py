﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
import datetime as dt

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    return controller.new_controller()
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    pass


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def tabular(cosas, titulos='', len=0, col=[]):
    """
    Dependiendo si es lista o diccionario la función 
    llamará a los métodos de tabulate para imprimir elements 
    """

    cols = []
    
    
    if len > 0:
        
        cols = [8 for _ in range(len)]
    if col:
        cols = col
    if type(cosas) is list:
        print(tabulate(cosas, headers=(titulos or 'keys'),
              tablefmt='grid', maxcolwidths=cols or None))
    if type(cosas) is dict:
        print(tabulate([[i, j] for i, j in cosas.items()], headers=(
            titulos or cosas.keys()), tablefmt="grid", maxcolwidths=cols or None))


def Subtabla(diccionario):
    
    
    return tabulate([diccionario.keys(), diccionario.values()], tablefmt='grid')


def Subtabular(cosas):
    respuesta = ""
    
    
    for cosa in cosas:
        
        respuesta += Subtabla(cosa) + "\n"
        
    return respuesta

def tablagrande(criterios, eventos):
    
    
    return list(map(lambda event: {criterios: event[0][criterios] if len(event) > 0 else "",'events': len(event),'details': Subtabular(eventos)}, eventos))
    
def load_data(control):
    """
    Carga los datos
    """
    
    datos = controller.load_data(control, "small")
    
    tabular(datos)


def fechas(fechain, fechafi):
    fechain = dt.datetime.strptime(fechain, "%Y-%m-%dT%H:%M")
    
    
    fechafi = dt.datetime.strptime(fechafi, "%Y-%m-%dT%H:%M")

    return fechain, fechafi



def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print("="*10+" Req No. 1 Inputs " + "="*10 )
 
    anio_inicial = input('Ingrese la fecha inicial del intervalo o (en formato "%Y-%m-%dT%H:%M")\n->')
    anio_final= (input('Ingrese la fecha final del intervalo o (en formato "%Y-%m-%dT%H:%M")\n->'))
    
    
    total, eventos = controller.req_1(control, anio_inicial, anio_final)
    
    print("El total de eventos encontrados fue de: ", total)
    
    eventoretorna = tablagrande('time', eventos)
    
    
    tabular(eventoretorna)



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print("="*10+" Req No. 2 Inputs " + "="*10 )

    magnitudmin = int(input('Ingrese el límite inferior de la magnitud (float) \n->'))
    magnitudmax = input('Ingrese el límite superior de la magnitud (float) \n->')
    
    eventos = controller.req_2(control, magnitudmin, magnitudmax)
    
    
    eventoretorna = tablagrande('mag', eventos)
    
    tabular(eventoretorna)

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print("="*10+" Requerimiento No. 3 Inputs-> José Gabriel Bernal Cárdenas jg.bernalc1@uniandes.edu.co, 202213421" + "="*10 )
    magnitudmin = input('Digite el mínimo de magnitud para revisar entre los eventos\n->')
    profundidadmax = input('Digite el máximo de magnitud para revisar entre los eventos \n->')
    
    
    total, eventos = controller.req_3(control, magnitudmin, profundidadmax)
    
    print("El total de eventos encontrados fue de : ", total)
    
    eventoretorna = tablagrande('time', eventos)
    
    
    tabular(eventoretorna)
    
    
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print("="*10+" Requerimiento No. 4 Inputs-> Juan Camilo Gómez Uribe j.gomezu@uniandes.edu.co, 202220238" + "="*10 )
    significanciamin = input('Digite el mínimo de significancia (sig) para revisar entre los eventos\n->')
    azitumalmax = input('Digite la máxima distancia azimutal (gap) para revisar entre los eventos \n->')
    
    
    total, eventos = controller.req_4(control, significanciamin, azitumalmax)
    
    print("El total de eventos encontrados fue de : ", total)
    
    
    eventoretorna = tablagrande('time', eventos)
    
    tabular(eventoretorna)

    

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print("="*10+" Requerimiento No. 5 Inputs-> Frank Yasser Ramírez Marín fy.ramirez@uniandes.edu.co, 202215747 " + "="*10 )
    profundidadmin = input('Digite el mínimo de profundidad (depth) para revisar entre los eventos\n->')
    minestaciones = input('Digite la cantidad mínima de esttaciones que detectan el evento (nst) para revisar entre los eventos \n->')
    total, eventoss = controller.req_5(control, profundidadmin, minestaciones)
    
    print("Total de eventos encontrados: ", total)
    eventoretorna = tablagrande('time', eventoss)
    tabular(eventoretorna)


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print("="*10+" Req No. 6 Inputs " + "="*10 )
    aniorelevante = input('Digite el año relevante (en formato “%Y”) \n->')
    latreferencia = input('Digite la latitud de referencia para el área de eventos (lat) \n->')
    longreferencia = input('Digite la longitud de referencia para el área de eventos (long) \n->')
    radioarea = input('Digite el radio (km) del área circundante (float) \n->')
    neventos = input('Digite el número de N eventos de mágnitud más cercana a revisar \n->')
    
    eventos, eventoo = controller.req_6(control, aniorelevante, latreferencia, longreferencia, radioarea, neventos)
    
    eventoretorna = tablagrande('time', eventos)
    
    print(Subtabular(eventoo))
    
    tabular(eventoretorna)


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print("="*10+" Req No. 7 Inputs " + "="*10 )
    aniorelevante = input('Digite el año relevante (en formato “%Y”) \n->')
    regionasociada = input('Digite el título de la región asociada (title) \n->')
    propiedad = input('Digite la propiedad de conteo (magnitud, profundidad o significancia)  \n->')
    radioarea = input('Digite el radio (km) del área circundante (float) \n->')
    casillas = input('Digite el número de segmentos o casillas (bins) en los que se divide el histograma \n->')



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción por favor \n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
                    
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
