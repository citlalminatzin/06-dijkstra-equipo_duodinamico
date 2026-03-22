#!/usr/bin/env python
"""
models.py

(Por favor modifica o elimina este comentario) 
Es recomendable que escribas unas cuantas líneas
explicando el propósito de cada código. Te propongo
que utilices este archivo para que escribas las
funciones principales que vayas a reutilizar en
tus otras prácticas
"""

import numpy as np


def matriz_ejercicio_1():
    """
    Matriz del Ejercicio 1 de la práctica.
    Gráfica dirigida de 4 nodos.
    """
    MD = np.zeros((4, 4))
    MD[0, 1] = 9
    MD[3, 2] = 2
    MD[0, 3] = 6
    MD[1, 3] = 1
    MD[2, 1] = 3
    return MD


def matriz_ejercicio_1():
    MD = np.zeros((4, 4))
    MD[0, 1] = 9
    MD[3, 2] = 2
    MD[0, 3] = 6
    MD[1, 3] = 1
    MD[2, 1] = 3
    return MD

def matriz_ejercicio_3a():
    n = 8
    M1 = np.zeros((n, n))

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
    return M1

def matriz_ejercicio_3b():
    n = 4
    M2 = np.zeros((n, n))

    M2[0,1] = 9
    M2[3,2] = 2
    M2[0,3] = 6
    M2[1,3] = 1
    M2[2,1] = 3
    return M2

def matriz_ejercicio_3c():
    n = 4
    M3 = np.zeros((n, n))

    M3[0,1] = 4
    M3[0,2] = 8
    M3[0,3] = 16
    M3[1,2] = 5
    M3[1,3] = 11
    M3[2,3] = 6
    return M3