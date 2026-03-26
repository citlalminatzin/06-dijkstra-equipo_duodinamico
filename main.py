#!/usr/bin/env python

import matplotlib.pyplot as plt
from numpy import zeros
from math import inf
from models import matriz_ejercicio_1
import networkx as nx
# para el ejercicio 3
from models import (
    matriz_ejercicio_1,
    matriz_ejercicio_3a,
    matriz_ejercicio_3b,
    matriz_ejercicio_3c
)

def dijkstra(M, origin):

    """ M: matriz de pesos, origin: nodo inicial
    regresa una lista de tuplas: (distancia_minima, predecesor """

    n = len(M)

    #Paso 1: inicializamos distancias y predecesores
    distancias = [inf] * n
    predecesores = [None] * n
    permanentes = [False] * n

    distancias[origin] = 0

    #repetimos hasta revisar todos los nodos
    for _ in range(n):
        # Paso 2 y 5: escoger el nodo no permanente
        # con menor distancia conocida
        nodo_actual = None
        mejor_distancia = inf

        for i in range(n):
            if not permanentes[i] and distancias[i] < mejor_distancia:
                mejor_distancia = distancias[i]
                nodo_actual = i

        #Si ya no hay nodos alcanzables, terminamos
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


def ejercicio_3a():
    M1 = matriz_ejercicio_3a()
    n = len(M1)
    distancias = [dijkstra(M1, i) for i in range(n)]
    return distancias

def ejercicio_3b():
    M2 = matriz_ejercicio_3b()
    n = len(M2)
    distancias = [dijkstra(M2, i) for i in range(n)]
    return distancias

def ejercicio_3c():
    M3 = matriz_ejercicio_3c()
    n = len(M3)
    distancias = [dijkstra(M3, i) for i in range(n)]
    return distancias

#Implementando la grafica y usamos networkx (Funcion para graficar)

def graficar_grafo(M, dirigido=True, titulo="Grafo", camino=None):

    """ Aqui dibuja un grafo a partir de una matriz de adyacencia.
    Si camino se proporciona, resalta ese camino.    """

    if dirigido:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    n = len(M)

    for i in range(n):
        G.add_node(i)

    for i in range(n):
        for j in range(n):
            if M[i][j] != 0:
                G.add_edge(i, j, weight=M[i][j])

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))

    nx.draw_networkx_nodes(G, pos, node_size=1800)
    nx.draw_networkx_labels(G, pos)

    nx.draw_networkx_edges(G, pos, arrows=dirigido)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if camino and len(camino) > 1:
        aristas_camino = [(camino[i], camino[i + 1]) for i in range(len(camino) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=aristas_camino, width=3, arrows=dirigido )

    plt.title(titulo)
    plt.axis("off")
    plt.show()


######### Comenzamos con la ejecucion ############

if __name__ == "__main__":

#Ejerciio 1 
    resultado = ejercicio_1()

    print("Resultado de Dijkstra desde el nodo 0:")
    for nodo, (distancia, predecesor) in enumerate(resultado):
        print(f"Nodo {nodo}: distancia = {distancia}, predecesor = {predecesor}")
    
    MD = matriz_ejercicio_1()
    graficar_grafo(MD, dirigido=True, titulo="Ejercicio 1")

#Ejercicio 2
    camino, distancia = ejercicio_2()

    print("\nEjercicio 2:")
    print(f"Camino óptimo: {camino}")
    print(f"Distancia mínima: {distancia}")

    #Grafica 
    graficar_grafo(MD, dirigido=True, titulo="Ejercicio 2 - Camino óptimo", camino=camino)
    

 # Ejercicio 3a
    print("\nEjercicio 3a:")
    resultado_3a = ejercicio_3a()
    for i, fila in enumerate(resultado_3a):
        print(f"Desde el nodo {i}: {fila}")

    #Grafica 
    M1 = matriz_ejercicio_3a()
    graficar_grafo(M1, dirigido=False, titulo="Ejercicio 3a")

# Ejercicio 3b
    print("\nEjercicio 3b:")
    resultado_3b = ejercicio_3b()
    for i, fila in enumerate(resultado_3b):
        print(f"Desde el nodo {i}: {fila}")

    #Grafica 
     M2 = matriz_ejercicio_3b()
    graficar_grafo(M2, dirigido=True, titulo="Ejercicio 3b")

    # Ejercicio 3c
    print("\nEjercicio 3c:")
    resultado_3c = ejercicio_3c()
    for i, fila in enumerate(resultado_3c):
        print(f"Desde el nodo {i}: {fila}")
    
    #Grafica 
    M3 = matriz_ejercicio_3c()
    graficar_grafo(M3, dirigido=True, titulo="Ejercicio 3c")


    


    

