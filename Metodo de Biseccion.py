from math import cos


def funcion(x):#Funcion 
    return cos(x)-x

print ("Este programa encuentra una raíz, por el método de bisección")
print("Introdusca los valores del INTERVALO")
print ("Introduzca el valor de A:")
a1=float(input())
print ("introduzca el valor de B:")
b1=float(input())
print ("Introduzca el valor de Error:")
error1=float(input()) 

  
def biseccion (a,b,error):#Metodo de biseccion
    
    m1=a#
    m=b;#
    K=0;#iteracion contador
    if(funcion(a)*funcion(b)>0):#control,comparar y saber si poseen el mismo signo
        print("la funcion no cambia de signo")#si no se cumple la condicion
    
        
    while(abs(m1-m)>error):#
        m1=m;
        m=(a+b)/2;
        if(funcion(a)*funcion(m)<0):
            b=m;    
        if(funcion(m)*funcion(b)<0):
            a=m;
            print("el intervalo es[",a,",",b,"]")
            K=K+1;
  
    
    print("Aproximacion:""x",K,"=",m," ")#resultado final
    
biseccion(a1,b1,error1)# 

   
