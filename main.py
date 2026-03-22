#!/usr/bin/env python

import matplotlib.pyplot as plt
from numpy import zeros
from math import inf
from models import matriz_ejercicio_1

def dijkstra(M, origin):

    """
    M: matriz de pesos, origin: nodo inicial
    Regresa una lista de tuplas: (distancia_minima, predecesor 
    """

    n = len(M)

    # Paso 1: inicializar distancias y predecesores
    distancias = [inf] * n
    predecesores = [None] * n
    permanentes = [False] * n

    distancias[origin] = 0

    # Repetimos hasta revisar todos los nodos
    for _ in range(n):
        # Paso 2 y 5: escoger el nodo no permanente
        # con menor distancia conocida
        nodo_actual = None
        mejor_distancia = inf

        for i in range(n):
            if not permanentes[i] and distancias[i] < mejor_distancia:
                mejor_distancia = distancias[i]
                nodo_actual = i

        # Si ya no hay nodos alcanzables, terminamos
        if nodo_actual is None:
            break

        # Marcar como permanente
        permanentes[nodo_actual] = True

        # Paso 3 y 4: revisar vecinos y reetiquetar
        for vecino in range(n):
            peso = M[nodo_actual][vecino]

            # En esta práctica, peso 0 significa que no hay arista
            if peso != 0 and not permanentes[vecino]:
                nueva_distancia = distancias[nodo_actual] + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual

    # Regresar lista de (distancia, predecesor)
    resultado = []
    for i in range(n):
        if distancias[i] == inf:
            resultado.append((inf, None))
        else:
            resultado.append((float(distancias[i]), predecesores[i]))

    return resultado


def minimal_distance(M, origin, destination):
    """
    Devuelve solo la distancia mínima entre origin y destination.
    """
    resultado = dijkstra(M, origin)
    return resultado[destination][0]


def ejercicio_1():
    """
    Regresa las distancias mínimas del primer vértice a todos los demás.
    """
    MD = matriz_ejercicio_1()
    return dijkstra(MD, 0)


if __name__ == "__main__":
    resultado = ejercicio_1()

    print("Resultado de Dijkstra desde el nodo 0:")
    for nodo, (distancia, predecesor) in enumerate(resultado):
        print(f"Nodo {nodo}: distancia = {distancia}, predecesor = {predecesor}")

# Ejercicio 2
def optimal_path(M, origin, destination):
    """
    Regresa el camino óptimo y la distancia mínima
    entre origin y destination.
    """
    resultado = dijkstra(M, origin)
    distancia = resultado[destination][0]

    if distancia == inf:
        return [], inf

    camino = []
    actual = destination

    while actual is not None:
        camino.append(actual)

        if actual == origin:
            break

        actual = resultado[actual][1]

    if camino[-1] != origin:
        return [], inf

    camino.reverse()
    return camino, distancia


def ejercicio_2():
    """
    Encuentra el camino óptimo del nodo 0 al nodo 2
    usando la misma matriz del ejercicio 1.
    """
    MD = matriz_ejercicio_1()
    return optimal_path(MD, 0, 2)

# Ejercicio 2
    camino, distancia = ejercicio_2()

    print("\nEjercicio 2:")
    print(f"Camino óptimo: {camino}")
    print(f"Distancia mínima: {distancia}")
    

"""

def ejercicio_3a():
    """
    Regresa las distancias mínimas de todos
    los vértices entre sí
    """
    n = 8
    M1 = zeros((n,n))

    M1[0,1] = M1[1,0] = 3
    M1[1,2] = M1[2,1] = 1
    M1[0,3] = M1[3,0] = 2
    M1[3,2] = M1[2,3] = 3
    M1[1,4] = M1[4,1] = 4
    M1[2,5] = M1[5,2] = 2
    M1[2,6] = M1[6,2] = 2
    M1[3,6] = M1[6,3] = 4
    M1[4,7] = M1[7,4] = 6
    M1[5,7] = M1[7,5] = 4
    M1[5,6] = M1[6,5] = 3
    M1[6,7] = M1[7,6] = 5
    
    distancias = [dijkstra(M1, i) for i in range(n)]
    return distancias

def ejercicio_3b():
    n = 4
    M2 = zeros((n,n))

    M2[0,1] = 9
    M2[3,2] = 2
    M2[0,3] = 6
    M2[1,3] = 1
    M2[2,1] = 3

    distancias = [dijkstra(M2, i) for i in range(n)]
    return distancias
    
def ejercicio_3c():
    n = 4
    M3 = zeros((n,n))

    M3[0,1] = 4
    M3[0,2] = 8
    M3[0,3] = 16
    M3[1,2] = 5
    M3[1,3] = 11
    M3[2,3] = 6

    distancias = [dijkstra(M3, i) for i in range(n)]
    return distancias

def ejercicio_4():
    ...

def main():
    ...
"""

if __name__ == "__main__":
    main()
