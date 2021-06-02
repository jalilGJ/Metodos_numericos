# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 22:46:41 2021

@author: ASUS
"""

import numpy as np # LIBRERIA PARA LOS CALCULOS

fx = lambda x: np.exp(-x) - x #FUNCION FX EN FORMA NUMERICA EN LAMBDA
gx = lambda x: np.exp(-x)

a = 0 # INTERVALO DE BUSQUEDA ENTRE 0 Y 1
b = 1 # INTERVALO DE BUSQUEDA ENTRE 0 Y 1
tolera  = 0.001 #ERROR
iteramax = 15  # ITERACION MAXIMA

#METODO DE APROXIMACION SUCESIVA (PUNTO FIJO)
i = 1 # ITERACION 
b = gx(a) #NUEVO VALOR A EVALUAR, SERA EL OTRO EXTREMO DEL INTERVALO
tramo = abs(b-a) #IDENTIFICA QUE TAN GRANDE ES EL ERROR
while not(tramo<=tolera or i>=iteramax ):# EVALUA EL TRAMO HASTA QUE SEA MENOR O IGUAL A TOLERANCIA MAXIMA
    a = b
    b = gx(a)
    tramo = abs(b-a) #ACTUALIZAR TRAMO 
    i = i + 1 # CUNETA EL NUMERO DE ITERACIONES/CUANDO EL METODO ES CONVERGENTE
result_final = b

# VALIDAR EL RESULTADO SI CONVERGE
if (i>=iteramax ):# SI LAS ITERACIONES SUPERAN EL NUMERO MAXIMO
    result_final = np.nan # NO FUE UN NUMERO ACEPTABLE

# SALIDA
print("Resultado final")
print (result_final)
print("Margen de error:")
print(tramo)
print("Iteraciones:")
print(i)
