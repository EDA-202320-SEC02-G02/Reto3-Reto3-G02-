"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
import datetime as dt
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {"informacion": mp.newMap(1),
                    "tiempo": om.newMap(),
                    "año_mes": om.newMap(),
                    "magnitud": om.newMap(),
                    "profundidad":om.newMap()}
    return data_structs


# Funciones para agregar informacion al modelo

def cargainfo(catalog:dict, filas:list, columnas:list, keys:list, actual: int):
    
    temblor = {} 
    for i in range(len(columnas)):
        temblor[keys[i]] = filas[columnas[i]]
    
    momento= dt.datetime.strptime('%Y-%m-%dT%H:%M',temblor['time'])
    temblor['time'] = momento
    
    mp.put(catalog['informacion'], actual, temblor)
    
def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(data_structs['temblores'], data)
    fechas(data_structs['Fechas'], data)
    


def fechas(map, data):
    fecha = data['time']
    fechacorta = fecha[:19]
    fechareal = fechacorta.replace("/", "-", 2)
    fechatemblor = dt.datetime.strptime(fechareal, '%Y-%m-%d %H:%M:%S')
    entrada = om.get(map, fechatemblor.date())
    if entrada is None:
        entradaa = nuevafecha(data)
        om.put(map, fechatemblor.date(), entradaa)
    else:
        entradaa = me.getValue(entrada)
    fechaa(entradaa, data)
    return map
# Funciones para creacion de datos
def nuevafecha(data):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entradaa = lt.newList('SINGLE_LINKED', comparacionfechas)
    return entradaa

def comparacionfechas(fecha1, fecha2):
    """
    Compara dos fechas
    """
    if (fecha1 == fecha2):
        return 0
    elif (fecha1 < fecha2):
        return 1
    else:
        return -1
def fechaa(datentry, data):
    lst = datentry
    lt.addLast(lst, data)
    
def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, anio_inicial,anio_final):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    fechain = dt.datetime.strptime(anio_inicial, '%Y/%m/%d')
    
    fechafi = dt.datetime.strptime(anio_final, '%Y/%m/%d')
    lst = om.values(data_structs['Fechas'], fechafi.date(), fechain.date())
    
    terremotos = 0
    
    listaterremotos = lt.newList(datastructure="ARRAY_LIST")
    
    for fechas in lt.iterator(lst):
        #print(fechas)
        
        terremotos += lt.size(fechas)
        
        for temblor in lt.iterator(fechas):
            #print(temblor)
            lt.addLast(listaterremotos, temblor)
            #print(listaterremotos)
    return terremotos, listaterremotos


def req_2(data_structs, magnitudmin,magnitudmax):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    lst = om.values(data_structs['magnitud'], magnitudmin,magnitudmax)
    
    terremotos = 0
    
    listaterremotos = lt.newList(datastructure="ARRAY_LIST")
    
    for fechas in lt.iterator(lst):
        #print(fechas)
        
        terremotos += lt.size(fechas)
        
        for temblor in lt.iterator(fechas):
            #print(temblor)
            lt.addLast(listaterremotos, temblor)
            #print(listaterremotos)
    return terremotos, listaterremotos


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
