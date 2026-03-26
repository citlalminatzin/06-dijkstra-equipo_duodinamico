[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vT72CUxW)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23225300)
# Práctica 6

En esta práctica se trabaja con el algoritmo de Dijkstra, cuyo objetivo es encontrar los caminos más cortos en un grafo ponderado. A lo largo de los ejercicios, se implementa el algoritmo en Python y se aplica a distintas matrices de adyacencia que representan grafos dirigidos y no dirigidos.

Se parte de la construcción de una función general que recibe una matriz de pesos y un nodo inicial, y devuelve las distancias mínimas hacia todos los demás nodos junto con sus predecesores y posteriormente se utiliza esta información para reconstruir el camino óptimo entre dos vértices específicos.

Además, se extiende el análisis a múltiples grafos, calculando los caminos mínimos desde todos los nodos, lo cual nos permitirá comprender el comportamiento del algoritmo en diferentes estructuras. Finalmente, se incorporan herramientas como networkx y matplotlib para visualizar las gráficas, facilitando la interpretación de los resultados obtenidos.

## Integrantes

- García Chalche Julio César 
- Rodríguez Rodríguez Diego 


## Uso e instalación

El codigo al arancar arrojar la solucion de todos los incisos:

Considerar tener instalado: Matplotlib, numpy and natworkx matplotlib


## Ejercicio 1
Planteamiento: 

    Programa una función que reciba la matriz de pesos de una gráfica y el nodo inicial y que 
    aplique el algoritmo de Dijkstra. Tu función debe regresar una lista con las distancias de las
    rutas y el origen de la arista con la que terminó la ruta.

Para resolver el Ejercicio 1, se implementó el algoritmo de Dijkstra, el cual permite encontrar las distancias mínimas desde un nodo origen hacia todos los demás nodos en un grafo ponderado.

El problema se modeló mediante una matriz de adyacencia, donde cada posición $(i, j)$ representa el peso de la arista del nodo $i$ al nodo $j$. En esta práctica, se consideró que un valor de 0 indica que no existe conexión directa entre los nodos.

La matriz utilizada fue la siguiente:

| Origen | Destino | Peso |
| :--- | :--- | :---: |
| Nodo 0 | Nodo 1 | 9 |
| Nodo 0 | Nodo 3 | 6 |
| Nodo 1 | Nodo 3 | 1 |
| Nodo 2 | Nodo 1 | 3 |
| Nodo 3 | Nodo 2 | 2 |

El algoritmo de Dijkstra se desarrolló siguiendo estos pasos:

Inicialización
1.- Se asigna distancia 0 al nodo origen (nodo 0).

+ A los demás nodos se les asigna una distancia infinita.
+ Se crea una lista de predecesores para reconstruir caminos.

2.- Selección del nodo

+ Se selecciona el nodo no visitado con la menor distancia conocida.
+ Actualización de distancias
+ Se revisan los vecinos del nodo actual.
+ Si se encuentra un camino más corto, se actualiza la distancia y el predecesor.

3.- Marcado como permanente

+ El nodo se marca como visitado (permanente).

4.- Repetición

+ Se repiten los pasos anteriores hasta procesar todos los nodos. 

Aplicando el algoritmo desde el nodo 0, se obtuvieron las siguientes distancias mínimas:

| Nodo | Distancia | Predecesor |
| :--- | :---: | :--- |
| **0** | 0.0 | *None* |
| **1** | 9.0 | 0 |
| **2** | 8.0 | 3 |
| **3** | 6.0 | 0 |

<h3 align="center">Gráfica del ejercicio 1</h3>

<p align="center">
  <img src="media/ejercicio1pic.png" width="400">
</p>


## Ejercicio 2
    Ahora, usando las listas generadas por tu función del algoritmo de Dijkstra, programa 
    una función que encuentre el camino óptimo entre dos vértices.

En este ejercicio se buscó determinar el camino más corto entre dos vértices específicos, utilizando como base los resultados obtenidos en el Ejercicio 1 mediante el algoritmo de Dijkstra.

A diferencia del ejercicio anterior, donde solo se calculaban las distancias mínimas, en este caso también se reconstruyó el camino completo que conecta el nodo origen con el nodo destino.

Para lograr esto, se aprovechó la lista de predecesores generada por el algoritmo de Dijkstra. Esta lista indica, para cada nodo, cuál fue el nodo anterior en el camino óptimo.

**El procedimiento seguido fue el siguiente:**

1.- Se ejecutó el algoritmo de Dijkstra tomando como nodo origen el nodo 0.

2.- Se obtuvo la lista de distancias mínimas y predecesores.

3.- Para reconstruir el camino hacia el nodo destino (nodo 2), se siguió este proceso:
+ Se inicia desde el nodo destino.
+ Se consulta su predecesor.
+ Se continúa retrocediendo hasta llegar al nodo origen.

4.- Finalmente, se invierte el orden de los nodos obtenidos para representar correctamente el camino desde el origen hasta el destino.

El camino óptimo encontrado desde el nodo 0 hasta el nodo 2 fue:

Camino óptimo: [0, 3, 2]
Distancia mínima: 8.0

<h3 align="center">Gráfica del ejercicio 2</h3>
<p align="center">
  <img src="media/ejercicio2pic.png" width="400">
</p>



## Ejercicio 3
    Prueba tus funciones con las siguientes matrices de pesos, empezando siempre en el nodo 0.
    Nota : Donde encuentres un cero quiere decir que no existe una arista entre dichos vertices.

En este ejercicio se aplicó el algoritmo de Dijkstra a diferentes grafos representados mediante matrices de adyacencia. A diferencia de los ejercicios anteriores, donde se analizaba un solo nodo origen, en este caso se ejecutó el algoritmo desde cada uno de los nodos del grafo, con el objetivo de obtener las distancias mínimas entre todos los pares de vértices.

Se trabajó con tres matrices distintas:

**M1 (Ejercicio 3a): grafo no dirigido con 8 nodos**

**M2 (Ejercicio 3b): grafo dirigido con 4 nodos**

**M3 (Ejercicio 3c): grafo dirigido con 4 nodos**


Cada matriz representa un grafo con distintas estructuras y conexiones, lo que permite analizar el comportamiento del algoritmo en diferentes escenarios.

**Para cada una de las matrices, se siguió el siguiente procedimiento:**

1.- Se tomó la matriz de adyacencia correspondiente.

2.- Se ejecutó el algoritmo de Dijkstra desde cada nodo del grafo.

3.- Se almacenaron los resultados en una lista, donde cada elemento representa las distancias mínimas desde un nodo específico hacia todos los demás.

4.- Se analizaron los resultados obtenidos para identificar la conectividad y accesibilidad entre los nodos.

Este proceso se implementó mediante un ciclo que recorre todos los nodos y aplica el algoritmo de forma repetida.

Ejercicio 3a (Grafo no dirigido)

+ Desde cualquier nodo es posible llegar a todos los demás.
+ Todas las distancias son finitas.
+ Esto indica que el grafo es conexo.

Ejemplo (desde nodo 0): Nodo 0 → [0, 3, 4, 2, 7, 6, 6, 10]

<h3 align="center">Gráfica del ejercicio 3a </h3>
<p align="center">
  <img src="media/ejercicio3a.png" width="400">
</p>

Ejercicio 3b (Grafo dirigido)

+ Existen nodos que no son alcanzables desde otros.
+ Aparecen valores inf, lo que indica que no hay camino entre ciertos nodos.
+ Esto refleja la naturaleza dirigida del grafo.

Ejemplo: Desde nodo 1 → algunos nodos tienen distancia infinita 

<h3 align="center">Gráfica del ejercicio 3b </h3>
<p align="center">
  <img src="media/ejercicio3b.png" width="400">
</p>


Ejercicio 3c (Grafo dirigido acíclico)

+ Las conexiones solo van en un sentido (hacia adelante).
+ Algunos nodos no pueden regresar a otros.
+ Se observan múltiples valores.

Ejemplo: Desde nodo 3 → no se puede llegar a ningún otro nodo

<h3 align="center">Gráfica del ejercicio 3c </h3>
<p align="center">
  <img src="media/ejercicio3c.png" width="400">
</p>



## Ejercicio 4
Encuentra la distancia mínima para el siguiente ejemplo , y organice el diagrama para tenerlo en Python.
(Screenshot_20260322_151336_Drive.jpg)

ETAPA 1

|Estados finales|Estados Iniciales (EI)|$F_1$|Qué estado inicial minimiza $F_1$?|
|------|--------|--------|-------|
|2|1|9|1|
|3|1|7|1|
|4|1|3|1|
|5|1|2|1|

ETAPA 2
|Estados finales|EI (2)|EI (3)|EI (4)|EI (5)|$F_2$|¿Qué estado inicial minimiza $F_2$?|
|---------------|------|------|------|------|-----|-----------------------------------|
|6              |1+4   | 7+2  |      |      |   5 |                                 2|
|7              |      |      |      | 2+11 |   13|5|
|8              | 9+1  |      |  3+11| 2+7  |    9|5|



ETAPA 3

|Estados finales|EI (6)|EI (7)|EI (8)|$F_3$|¿Qué estado inicial minimiza $F_3$?|
|---------------|------|------|------|-----|-----------------------------------|
|9              |5+6   | 13+4 |      |  11 |                                 6 |
|10             |5+5   | 13+4 |  9+5 |   10|6|
|11             |      |      | 2+7  |   15|8|

ETAPA 4

|Estados finales|EI (9)|EI (10)|EI (11)|$F_4$|¿Qué estado inicial minimiza $F_4$?|
|---------------|------|------|------|-----|-----------------------------------|
|12             |11+4  |10+6  |15+6  |  15 |                                 9 |



LA DISTANCIA MÍNIMA ESTÁ DADA POR EL SIGUIENTE CAMINO:
|ETAPA 1|ETAPA 2|ETAPA 3|ETAPA 4|
|-------|-------|-------|-------|
|(12)----(9)| (9)----(6)|(6)----(2)|(2)----(1) |







## Conclusión

¿Te gustó la programación dinámica? ¿Sientes que te será útil? ¿Se te hace una buena estrategia para la resolución de problemas?
