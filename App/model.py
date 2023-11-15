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

import math as mat
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

def newCatalog():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    # TODO: Inicializar las estructuras de datos
    catalog = {"earthquackes": None,"date_tree": None,"significant": None,"magnitude": None,"depth": None,"years": None}
    
    catalog["earthquackes"]=lt.newList("ARRAY_LIST", cmpfunction=comparafechas)
    catalog["date_tree"]=om.newMap(omaptype="RBT", cmpfunction=comparafechas)
    catalog["significant"]=om.newMap(omaptype="RBT")

    catalog["magnitude"]=om.newMap(omaptype="RBT")
    catalog["depth"]=om.newMap(omaptype="RBT")

    catalog['years']=mp.newMap(101, maptype="PROBING", loadfactor=0.5)
    return catalog


def comparafechas(fecha1, fecha2, reverse=False):
    """
    Compara dos fechas
    """
    if (fecha1==fecha2):
        return 0
    elif (fecha1<fecha2) and not reverse:
        
        return -1
    
    else:
        return 1
    
def add_earthquake(catalogo, terremoto):
    """
    adicionar un terremoto al arbol
    """
    terremoto['felt']="Unknown" if terremoto['felt']=='' else terremoto['felt']
    terremoto['cdi']="Unknown" if terremoto['cdi']=='' else terremoto['cdi']
    terremoto['mmi']="Unknown" if terremoto['mmi'] =='' else terremoto['mmi']
    
    
    terremoto['tsunami']=False if terremoto['tsunami']== '0' else terremoto['tsunami']
    terremoto['tsunami']= True if terremoto['tsunami']=='1' else terremoto['tsunami']
    terremoto['gap']=0.000 if terremoto['gap']=='' else terremoto['gap']
    terremoto['nst']=1 if terremoto['nst']=='' else terremoto['nst']
    
    lt.addLast(catalogo['earthquackes'], terremoto)

    terremoto['mag']=float(terremoto['mag'])
    
    terremoto['depth']=float(terremoto['depth'])
    
    terremoto['sig']=float(terremoto['sig'])
    
    
    terremoto['gap']=float(terremoto['gap'])
    terremoto['lat']=float(terremoto['lat'])
    
    terremoto['long']=float(terremoto['long'])

    terremoto['time']=dt.datetime.strptime(terremoto['time'], "%Y-%m-%dT%H:%M:%S.%fZ")

    anio = terremoto['time'].year
    # req 1 tree dates
    actualizarr(catalogo["date_tree"],
                         terremoto['time'], terremoto)
    actualizarr(catalogo['significant'],
                         terremoto['sig'], terremoto)
    actualizarr(catalogo['depth'],
                         terremoto['depth'], terremoto)
    actualizarr(catalogo['magnitude'], terremoto['mag'], terremoto)
    actualizar(catalogo['years'], anio, terremoto)

    return catalogo
# Funciones de consulta


def actualizarr(mapa, llave, data):

    entrada=om.get(mapa, llave)
    if entrada is None:

        datonuevo = lt.newList()
        lt.addLast(datonuevo, data)
        
        
        om.put(mapa, llave, datonuevo)
    else:
        fechaentry =me.getValue(entrada)
        lt.addLast(fechaentry, data)

    return mapa

def actualizar(map, llave, data):

    entrada=mp.get(map, llave)
    
    if entrada is None:
        
        
        datonuevo= lt.newList()
        
        lt.addLast(datonuevo, data)
        
        
        mp.put(map, llave, datonuevo)
    else:
        
        fechaentry=me.getValue(entrada)
        lt.addLast(fechaentry, data)
    return map


def primeroultimomapa(map, llaves, filter_data=None, size=3):
    """
    Retorna los n primeros y últimos elemento de la lista
    """
    primero= []
    ultimo=[]
    
    if lt.size(llaves) < size * 2:
        
        for lave in lt.iterator(llaves):
            
            
            elemento = primeroultimo(me.getValue(mp.get(map, lave)), filter_data, size)
            primero.append(elemento)
            
            
    else:
        for i in range(1, size + 1):
            
            
            primeroo= primeroultimo(me.getValue(mp.get(
                
                map, lt.getElement(llaves, i))), filter_data, size)
            primero.append(primeroo)
            
            
            ultimoo =primeroultimo(me.getValue(mp.get(map, lt.getElement(llaves, lt.size(llaves) - i + 1))), filter_data, size)
            ultimo.insert(0, ultimoo)

    return primero + ultimo

def primeroultimo(data_structs, filter_data=None, size=3):
    """
    Retorna los n primeros y últimos elemento de la lista
    """
    primero =[]
    
    ultimo = []

    if lt.size(data_structs) <size * 2:
        
        for i in range(1, lt.size(data_structs) + 1):
            
            elementoo = datosfiltrados(lt.getElement(data_structs, i), filter_data)
            
            primero.append(elementoo)
    else:
        
        for i in range(1, size + 1):
            
            primeroo = datosfiltrados(lt.getElement(data_structs, i), filter_data)
            
            
            primero.append(primeroo)
           
            ultimoo = datosfiltrados(lt.getElement(data_structs, lt.size(data_structs) - i + 1), filter_data)
            ultimo.insert(0, ultimoo)

    return primero + ultimo


def datosfiltrados(data, atributos):
    """
    Retorna un diccionario con los atributos de un dato
    """
    if not atributos:
        
        return data

    datosfiltrados ={}
    
    for lave in atributos:
        
        datosfiltrados[lave] =   data[lave]
        
    return datosfiltrados

def sort(data_structs,criterio):
    """
    Función encargada de ordenar la lista con los datos
    """
    
    return merg.sort(data_structs,criterio)


def req_1(data_structs, anio_inicial,anio_final):
    """
    Función que soluciona el requerimiento 1
    """
    todos =mp.newMap()
    arbolfecha=data_structs['date_tree']

    fechain=dt.datetime.strptime(anio_inicial, "%Y-%m-%dT%H:%M")
    
    fechafi=dt.datetime.strptime(anio_final, "%Y-%m-%dT%H:%M")


    eventosterre=om.keys(arbolfecha, fechain, fechafi)
    
    eventosterre=sort(eventosterre, composed_sort([comparaval]))
    
    
    

    for i in lt.iterator(eventosterre):
        
        eventos= om.get(arbolfecha, i)
        
        
        eventoos= me.getValue(eventos)
        
        eventoss= lt.newList()
        
        
        for j in lt.iterator(eventoos):
            if j:
                
                
                lt.addLast(eventoss, j)
                
        eventoss= sort(eventoss, composed_sort([comparamagnitud]))
        
        mp.put(todos,i,eventoss)
        
    total=lt.size(eventosterre)

    return total, todos, eventoss

def comparamagnitud(magnitud1,magnitud2):

    if (magnitud1['mag']==magnitud2['mag']):
        
        return 0
    
    elif (magnitud1['mag']<magnitud2['mag']):
        
        return -1
    else:
        return 1
    
def comparaval(val1,val2):
    
    if (val1==val2) :
        
        return 0
    
    elif (val1<val2):
        
        
        return -1
    
    else:
        
        return 1
    
def composed_sort(listacomp):
    """
    Función para comparar dos elementos por varios criterios
    """
    
    
    def cmp(dato1, dato2):
        
        for cmp_function in listacomp:
            
            resultado = cmp_function(dato1, dato2)
            
            if resultado != 0:
                
                
                return resultado > 0
            
        return False
    return cmp

def req_2(data_structs, magnitudmin,magnitudmax):
    """
    Función que soluciona el requerimiento 2
    """
    todos=mp.newMap()
    dato=data_structs["magnitude"]
    
    valores=om.keys(dato, magnitudmin, magnitudmax)
    
    valores=sort(valores, composed_sort([comparaval]))
    
    

    for i in lt.iterator(valores):
    
        eventosentry=om.get(dato, i)
        eventoos=me.getValue(eventosentry)

        elememnto= lt.newList()
        
        for j in lt.iterator(eventoos):
            if j:
                
                lt.addLast(elememnto, j)
                
                
        mp.put(todos,i,elememnto)
    return todos,valores


def req_3(data_structs,magnitudmin,profundidadmax):
    """
    Función que soluciona el requerimiento 3
    """
    
    todos =mp.newMap()

    arbolmagnitudes=data_structs["magnitude"]
    
    
    maxmagnitud=om.maxKey(arbolmagnitudes)
    
    arbolfechas=data_structs['date_tree']

    valoresllave=om.keys(arbolmagnitudes, magnitudmin, maxmagnitud)
    
    
    total= lt.size(valoresllave)
    
    
    fechaslave = lt.newList('ARRAY_LIST')
    
    for i in lt.iterator(valoresllave) :
        eventosentry=om.get(arbolmagnitudes, i)
        #print(i)
        
        eventoos=me.getValue(eventosentry)
        
        for j in lt.iterator(eventoos):
            #print(j)
            if j:
                
                if float(j['depth'])<=profundidadmax:
                    
                    
                    lt.addLast(fechaslave,j['time'])

    fechaslave= sort(fechaslave, composed_sort([comparaval]))
    fechaslave=lt.subList(fechaslave, 1, 10)

    for i in lt.iterator(fechaslave):
        #print(i)
        
        
        eventosentry=om.get(arbolfechas, i)
        

        eventoos=me.getValue(eventosentry)
        elementoo= lt.newList()
        
        for j in lt.iterator(eventoos):
            
            if j:
                
                lt.addLast(elementoo, j)
        mp.put(todos, i, elementoo)
    return total, todos, fechaslave



def req_4(data_structs,significanciamin,azitumalmax):
    """
    Función que soluciona el requerimiento 4
    """
    todos = mp.newMap()

    
    
    arbolsig=data_structs["significant"]
    
    maxsig=om.maxKey(arbolsig)
    arbolfechas=data_structs['date_tree']

    valorllaves= om.keys(arbolsig, significanciamin, maxsig)
    
    
    total = lt.size(valorllaves)
    llavefecha = lt.newList('ARRAY_LIST')
    for i in lt.iterator(valorllaves):
        
        
        eventosentry=om.get(arbolsig, i)
        eventoos=me.getValue(eventosentry)
        
        for j in lt.iterator(eventoos):
            
            if j:
                
                if float(j['gap'])<=azitumalmax:
                    
                    lt.addLast(llavefecha, j['time'])

    llavefecha=sort(llavefecha, composed_sort([comparaval]))
    
    
    llavefecha=lt.subList(llavefecha, 1, 15)

    for i in lt.iterator(llavefecha):
        #print(i)
        elementp = lt.newList()
        eventosentry=om.get(arbolfechas, i)
        
        
        eventoos=me.getValue(eventosentry)
        
        for j in lt.iterator(eventoos):
            
            
            if j:
                
                
                lt.addLast(elementp, j)
        mp.put(todos, i, elementp)


    return total, todos, llavefecha



def req_5(data_structs,profundidadmin, minestaciones):
    """
    Función que soluciona el requerimiento 5
    """
    todos= mp.newMap()
    
    
    arbolfechas=data_structs['date_tree']
    
    arbolprofundidadess=data_structs["depth"]
    llavefecha = lt.newList('ARRAY_LIST')
    
    profmax=om.maxKey(arbolprofundidadess)
    

    
    valorllaves = om.keys(arbolprofundidadess,profundidadmin,profmax)
    
    
    total = lt.size(valorllaves)
    
    for i in lt.iterator(valorllaves):
        
        eventosentry=om.get(arbolprofundidadess, i)
        
        
        eventos=me.getValue(eventosentry)
        
        
        for j in lt.iterator(eventos):
            if j:
                if float(j['nst'])>=minestaciones:
                    lt.addLast(llavefecha, j['time'])


    llavefecha=sort(llavefecha,composed_sort([comparaval]))
    
    
    llavefecha=lt.subList(llavefecha, 1, 20)
    for j in lt.iterator(llavefecha):
        
        
        eventosentry= om.get(arbolfechas , j)

        eventos =me.getValue(eventosentry)
        elemento=lt.newList()
        for i in lt.iterator(eventos):
            if i:
                
                
                lt.addLast(elemento , i)
        mp.put(todos, j, elemento)

    return total, todos, llavefecha




def req_6(data_structs,aniorelevante,latreferencia,longreferencia ,radioarea, neventos):
    eventoos = mp.newMap()
    
    significante=req6dos(data_structs,aniorelevante, latreferencia,longreferencia, radioarea)

    efecha = data_structs['date_tree']
    

    for i in range(neventos):
        cielo= om.ceiling(efecha, significante['time'])
        piso=om.floor(efecha, significante['time'])
        
        
        minimoo=min( cielo , piso )
        
        
        eventosentry = om.get(efecha , minimoo)
        
        eventoo = me.getValue( eventosentry)
        mp.remove(efecha, minimoo)



        mp.put(eventoos,minimoo,eventoo)

    eventosfecha=mp.keySet(eventoos)
    eventosfecha=sort(eventosfecha, composed_sort([comparafechas]))

    return significante,eventoos,eventosfecha


def req6dos(data_structs,aniorelevante, latreferencia,longreferencia, radioarea):
    listaa=lt.newList()
    
    anio=data_structs['years']
    
    en =mp.get(anio , aniorelevante)
    
    
    eventoos =me.getValue(en)
    
    

    for i in lt.iterator(eventoos) :
        
        if i:
            
            if radiofuncion(float(latreferencia), float(longreferencia), float(i['lat']), float(i['long']), radioarea):
                
                lt.addLast(listaa, i)

    listaa = sort(listaa, composed_sort([comparasign]))

    return lt.firstElement(listaa)

def radiofuncion(latitud1, longitud1,latitud2, longitud2,radio) :
    
    latitud1= mat.radians(latitud1)
    
    
    longitud1= mat.radians(longitud1)
    
    latitud2= mat.radians(latitud2)
    
    longitud2= mat.radians(longitud2)
    

    return 2 * mat.asin(mat.sqrt(mat.sin((latitud2 - latitud1) / 2) ** 2 + mat.cos(latitud1) * mat.sin(latitud2) * mat.cos((longitud2 - longitud1) / 2) ** 2)) * 6371 <= radio


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

def comparasign(signi1, signi2):
    """
    Compara dos significancias minim as
    """

    if (signi1['sig']==signi2['sig']):
        
        return 0
    
    elif (signi1['sig']> signi2['sig']):
        return 1
    
    else:
        
        return -1


