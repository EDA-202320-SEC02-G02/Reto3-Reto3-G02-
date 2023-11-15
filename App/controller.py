﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import csv
import time
import model
import tracemalloc
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
assert cf
import csv
csv.field_size_limit(2147483647)
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    return {'model': model.newCatalog()}


# Funciones de ordenamiento
def load_data(control , filename):
    """
    Carga los datos del reto
    """
    catalog = control['model']
    eathquaks= cf.data_dir + 'earthquakes/temblores-utf8-' + filename + '.csv'
    input_file =csv.DictReader(open(eathquaks, encoding="utf-8"),delimiter=",")

    for terremoto in input_file:
        model.add_earthquake(catalog, terremoto)

    return model.primeroultimo(catalog['earthquackes'], filter_data=[
        'time',
        'lat',
        'long',
        'depth',
        'mag',
        'sig',
        'nst',
        'gap',
        'title',
        'felt',
        'cdi',
        'mmi',
        'tsunami'
    ], size=5)



def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control,anioincial, aniofinal):
    """
    Retorna el resultado del requerimiento 1
    """
    
    
    total, eventos, keyeventss = model.req_1(control['model'], anioincial, aniofinal)
    eventos= model.primeroultimomapa(eventos, keyeventss, filter_data=[
        'time',
        'mag',
        'lat',
        'long',
        'depth',
        'sig',
        'gap',
        'nst',
        'title',
        'cdi',
        'mmi',
        'magType',
        'type',
        'code',
    ])
    return total, eventos



def req_2(control, magnitudmin,magnitudmax):
    """
    Retorna el resultado del requerimiento 2
    """
    eventos, valores =model.req_2(control['model'],magnitudmin, magnitudmax)

    return model.primeroultimomapa(eventos, valores , filter_data=[
        'time',
        'mag',
        'lat',
        'long',
        'depth',
        'sig',
        'gap',
        'nst',
        'title',
        'cdi',
        'mmi',
        'magType',
        'type',
        'code'
    ])


def req_3(control, magnitudmin,profundidadmax):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    total, eventos, keyeventss=model.req_3(control['model'], magnitudmin, profundidadmax)
    
    eventos = model.primeroultimomapa(eventos, keyeventss, filter_data=[
        'time',
        'mag',
        'lat',
        'long',
        'depth',
        'sig',
        'gap',
        'nst',
        'title',
        'cdi',
        'mmi',
        'magType',
        'type',
        'code',
    ])
    return total, eventos




def req_4(control,significanciamin,azitumalmax):
    """
    Retorna el resultado del requerimiento 4
    """
    
    total, eventos, keyeventss= model.req_4(control['model'], significanciamin, azitumalmax)
    
    eventos = model.primeroultimomapa(eventos, keyeventss, filter_data=[
        'time',
        'mag',
        'lat',
        'long',
        'depth',
        'sig',
        'gap',
        'nst',
        'title',
        'cdi',
        'mmi',
        'magType',
        'type',
        'code',
    ])
    return total, eventos



def req_5(control,profundidadmin,minestaciones):
    """
    Retorna el resultado del requerimiento 5
    """
    
    total, eventos, keyeventss = model.req_5(control['model'], profundidadmin, minestaciones)
    
    eventos = model.primeroultimo(eventos, keyeventss, filter_data=[
        'time',
        'mag',
        'lat',
        'long',
        'depth',
        'sig',
        'gap',
        'nst',
        'title',
        'cdi',
        'mmi',
        'magType',
        'type',
        'code',
    ])
    return total, eventos




def req_6(control, aniorelevante, latreferencia, longreferencia, radioarea, neventos):
    """
    Retorna el resultado del requerimiento 6
    """
    eventoo, eventos, fechas = model.req_6(
        control['model'], aniorelevante, latreferencia, longreferencia, radioarea, neventos)
    return model.primeroultimomapa(eventos, fechas, filter_data=[
        'time',
        'mag',
        'lat',
        'long',
        'depth',
        'sig',
        'gap',
        'nst',
        'title',
        'cdi',
        'mmi',
        'magType',
        'type',
        'code'
    ]), model.datosfiltrados(eventoo, [
        'time',
        'mag',
        'lat',
        'long',
        'depth',
        'sig',
        'gap',
        'nst',
        'title',
        'cdi',
        'mmi',
        'magType',
        'type',
        'code'
    ])


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
