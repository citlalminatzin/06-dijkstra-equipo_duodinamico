[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vT72CUxW)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23225300)
# Práctica 6

`data/distances.csv` contiene la lista de adyacencias de la gráfica dirigida del ejercicio 4.

## Integrantes

- García Chalche Julio César 
- Rodríguez Rodríguez Diego 


## Uso e instalación
Para poder ejecutar el código, primero debes instalar los siguientes archivos:
- `models.py`: Aquí encontrarás el algoritmo de Dijkstra.
- `main.py`: Contiene el código para graficar cada uno de los tres ejercicios
- `data.py`: Tal vez aquí puedes leer el csv para a partir crear una matriz de adyacencia




## Ejercicio 1
Programa una función que reciba la matriz de pesos de una gráfica y el nodo inicial y que 
aplique el algoritmo de Dijkstra. Tu función debe regresar una lista con las distancias de las
rutas y el origen de la arista con la que terminó la ruta.


## Ejercicio 2
Ahora, usando las listas generadas por tu función del algoritmo de Dijkstra, programa 
una función que encuentre el camino óptimo entre dos vértices.


## Ejercicio 3
Prueba tus funciones con las siguientes matrices de pesos, empezando siempre en el nodo 
0.
Nota : Donde encuentres un cero quiere decir que no existe una arista entre dichos vertices.


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
