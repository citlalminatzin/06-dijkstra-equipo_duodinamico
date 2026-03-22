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