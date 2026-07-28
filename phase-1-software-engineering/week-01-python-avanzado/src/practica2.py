"""


with open("test.txt","w",encoding="utf-8") as f:
    f.write("INFO: El sistema inició correctamente.\n")
    f.write("ERROR: El sistema inició mal.\n")
    f.write("ERROR: El sistema FALLO.\n")
    f.write("INFO: El sistema inició correctamente.\n")
    f.write("INFO: El sistema inició correctamente.\n")

def generador_lectura(fichero):
    with open(fichero,encoding="utf-8") as f:
        for lineas in f:
            yield lineas

def generador_filtrar(lineas):
    for linea in lineas:
        if "ERROR" in linea:
            yield linea


if __name__=="__main__":
    archivo="test.txt"

    generador=generador_lectura(archivo)
    filtro=generador_filtrar(generador)

    print("----------------------Detectando errores----------------------")
    for error in filtro:
        print(error)

"""

"""
Práctica 4: Expresión generadora vs. Comprensión de lista (Optimización)
Objetivo: Comparar la sintaxis y el uso de una expresión generadora frente a una lista tradicional al pasarlas como argumento único a una función como sum().

Instrucciones:

Define una lista de números enteros: nums = [1, 2, 3, 4, 5].

Calcula la suma de sus cuadrados usando una comprensión de lista (utilizando corchetes [...] dentro de sum()).

Calcula exactamente lo mismo usando una expresión generadora (cambiando los corchetes por paréntesis (...) o simplemente omitiéndolos si van dentro del argumento único de la función, ej: sum(x*x for x in nums)).

Comprueba que el resultado numérico es idéntico (55), pero recuerda que la segunda opción procesa los datos bajo demanda sin construir una lista gigante en la memoria RAM.


"""

##----------------------------------------------SOLUCION----------------------------------------------

nums=[1,2,3,4,5]
total=sum(nums)
cantidad_elementos=len(nums)
promedio=total/cantidad_elementos
sumas_cuadrados=sum([x*x for x in nums])
print(f" el total es: {total} y la lista tiene {cantidad_elementos} elementos y el promedio es: {promedio} y la suma de sus cuadrados es: {sumas_cuadrados}")



def generador_suma_cuadrados(lista):
    yield sum([y*y for y in lista])


lista=generador_suma_cuadrados([1,2,3,4,5])
print(next(lista))

#se concluye que para la mnipulacion de grandes cantidades de datos, es recomendado usar generadores que listas.