def area_rectangulo(b,h):
    resultado= b*h
    return resultado

area= area_rectangulo(15,10)
print(area)


import math

def area_circulo(radio):
    resultado= (radio**2)* math.pi
    return resultado
radio=int(input("ingrese radio: "))
print(f"el area del circulo es:",(area_circulo(radio)))


def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
 
print( relacion(5, 10) )
print( relacion(10, 5) )
print( relacion(5, 5) )


def intermedio(a,b):
    resultado= (a+b)/2
    return resultado
punto_intermedio= intermedio(-12,24)
print(punto_intermedio)


def recortar(a,b,c):
    return max(min(a,c), b)

recorte= recortar(15, 0, 10)
print(recorte)



numeros=[6,9,5,8,2,3,7,4]
def separar (*args):
    lista= sorted(*args)
    pares=[]
    impares=[]
    for arg in lista:
        if arg %2==0:
            pares.append(arg)
        else:
            impares.append(arg)
    return pares, impares

pares, impares= separar(numeros)
print(pares)
print(impares)