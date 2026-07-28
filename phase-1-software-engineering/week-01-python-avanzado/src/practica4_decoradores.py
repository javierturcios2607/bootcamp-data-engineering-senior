"""



def suma(a,b):
    print(a+b)

def ejecutar_operacion(operacion, a, b):
    operacion(a, b)


mi_operacion=suma# puedo asignarle una funcion a una variable
mi_operacion(10,20)

ejecutar_operacion(mi_operacion, 10, 20)

# a(b)--> c decorador


def funcion_a(funcion_b): #funcion b = saludar()

    def funcion_c(*args ,**kwargs):
        print('Antes de la ejecucion')
        resultado=funcion_b(*args ,**kwargs)
        print("Despues de la ejecucion")

        return resultado

    return funcion_c



@funcion_a
def saludar():
    print("Hola desde una funcion")

saludar()

@funcion_a
def suma(a, b):
    return a+b

print(suma(1,2))

#------------------refactorizando------------------------

def mi_decorador(funcion): #funcion b = saludar()

    def wrapper(*args ,**kwargs):
        return funcion(*args ,**kwargs)

    return wrapper

# calulemos cuanto le toma a una funcion completar su ejecucion

import time

 
def calcular_tiempo_a(funcion_b):

    def wrapper_c(*args, **kwargs):
        inicio= time.time()
        resultado= funcion_b(*args, **kwargs)
        fin=time
        print("Tiempo total: ", time.time()-inicio)

        return resultado
    return wrapper_c



@calcular_tiempo_a
def suma(a,b):
    return a+b


print(suma(3,2))

"""



"""


def mi_decorador_a(funcion_b):

    def wrapper(*args, **kwargs):
        print("antes de transformar la funcion")
        return funcion_b(*args, **kwargs)
    return wrapper

@mi_decorador_a
def resta(a,b):
    return a-b

print(resta(3,2))
"""



def funcion_a(funcion_b):
    def wrapper_c(*args, **kwargs):
        print("transformando funcion")
        return funcion_b(*args, **kwargs)        
    return wrapper_c



@funcion_a
def funcionb(mensaje):
    print("hola mundo")

funcionb("hola")