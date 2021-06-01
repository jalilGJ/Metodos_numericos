# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np #LIBRERIA PARA PODER HACER LOS CALCULOS
import sympy as sym#LIBRERIA PARA DARLE FORMA ALGEBRAICA AL POLINOMIO

# INGRESO , DATOS A UTILIZAR EN EL PROGRAMA EN FORMA DE VECTOR
xi = np.array([0, 0.2, 0.3, 0.4])
fi = np.array([1, 1.6, 1.7, 2.0])

#PROCEDIMIENTO 
n = len(xi)#ELEMENTOS DEL VECTOR
x = sym.Symbol('x')
polinomio = 0#SE GUARDAN LOS TERMINOS DEL POLINOMIO
divisorL = np.zeros(n, dtype = float)#EL DIVISOR NOS MUESTRA LOS RESULTADOS CON EL METODO DE NUMPY
for i in range(0,n,1):
    
    # TERMINOS DE LAGRANGE
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador# DEACUERDO A LA FORMULA DE LAGRANGE

    polinomio = polinomio + terminoLi*fi[i]# TERMINOS SE GUARDAN EN LA VARIABLE ASIGNADA
    divisorL[i] = denominador

# SIMPLIFICA EL POLINOMIO
polisimple = polinomio.expand()

# EVALUACION NUMERICA
px = sym.lambdify(x,polisimple)

print('Valores de fi: ',fi)
print('Divisores en L(i): ',divisorL)
print()
print('Polinomio de Lagrange, expresiones:')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(polisimple)