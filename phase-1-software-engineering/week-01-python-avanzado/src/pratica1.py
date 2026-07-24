"""
Instrucciones:

Escribe una función llamada cuenta_atras(n) que reciba un número entero.

Usa un bucle while para que mientras n > 0, devuelva el valor utilizando yield n y luego decremente n en 1.

Asigna la función a una variable (por ejemplo, gen = cuenta_atras(3)) y observa que no se ejecuta ningún print ni cálculo inmediato.

Llama manualmente a next(gen) tres veces seguidas e imprime el resultado. ¿Qué sucede en la cuarta llamada?
"""



##----------------------------------------------SOLUCION----------------------------------------------
"""


def cuenta_atras(n):
    while n > 0:
        yield n
        n=n-1# en python no se debe dejar una operacion matematica suelta ejemplo: n-1

    

gen= cuenta_atras(3)
print(next(gen))
print(next(gen))
print(next(gen))
# EL generador soloss tiene 3, que pasa si pedimos un 4?
print(next(gen)) # nos da este error StopIteration


"""



"""
Práctica 2: Filtrar un archivo de texto gigante línea por línea (Eficiencia de memoria)
Objetivo: Simular el procesamiento de un archivo grande sin saturar la memoria RAM, aplicando una tubería (pipeline) básica de filtrado.

Instrucciones:

Crea un archivo de texto temporal en tu entorno (o imagina un log con líneas de texto, algunas que contengan la palabra "ERROR" y otras "INFO").

Escribe una función generadora llamada leer_log(fichero) que abra el archivo y utilice un bucle for para hacer yield linea.rstrip() de cada línea.

Escribe un segundo generador llamado solo_errores(lineas) que reciba el generador anterior, filtre únicamente las líneas que contengan la palabra "ERROR" y haga yield de ellas.

Conecta ambos generadores e imprímelos usando un bucle for final.
"""

##----------------------------------------------SOLUCION----------------------------------------------
"""

#En Python, la sentencia with se conoce como un gestor de contextos (context manager). Su trabajo principal es manejar recursos externos (como archivos, conexiones a bases de datos o sockets de red) asegurándose de que siempre se cierren y se liberen de forma correcta, sin importar si ocurre un error durante el proceso.
# 1. Creamos el archivo de log temporal de prueba
# 1. Creamos el archivo de log temporal de prueba
with open("log_enorme.txt", "w", encoding="utf-8") as f:
    f.write("INFO: El sistema inició correctamente.\n")
    f.write("ERROR: Conexión fallida con la base de datos.\n")
    f.write("INFO: Usuario autenticado con éxito.\n")
    f.write("ERROR: Tiempo de espera agotado (timeout).\n")
    f.write("INFO: Cerrando sesión de rutina.\n")


def leer_log(fichero):
    with open(fichero, encoding="utf-8") as f:
        for lineas in f:
            yield lineas.rstrip()


def solo_errores(lineas):
    for linea in lineas:
        if "ERROR" in linea:
            yield linea

def solo_info(lineas):
    for linea in lineas:
        if "INFO" in linea:
            yield linea

if __name__=="__main__":
    archivo_logs="log_enorme.txt"

    generador_lectura=leer_log(archivo_logs)
    generador_filtro=solo_errores(generador_lectura)
    generador_info=solo_info(generador_lectura)

    
     
    for info in generador_info:
        print(info)
"""

"""
Práctica 3: Generador infinito de IDs únicos (Secuencias infinitas)
Objetivo: Aprovechar que un generador puede ser infinito de forma segura gracias a la evaluación perezosa (lazy evaluation).

Instrucciones:

Diseña una función generadora llamada generador_ids(prefijo="USER").

Inicializa un contador en 0 y crea un bucle while True (infinito).

Incrementa el contador en cada vuelta y utiliza yield para devolver un texto formateado, por ejemplo: f"{prefijo}-{contador:04d}" (para que los números tengan ceros a la izquierda, como USER-0001).

Llama al generador e imprime los primeros 5 IDs utilizando un bucle for con un rango o llamando a next() de forma controlada.

"""

def  generador_ids(prefijo="USER"):
    contador=0
    while True:
        yield f"{prefijo}-{contador:04d}"
        contador= contador +1

generar=generador_ids()


for _ in range(1000000):
    print(next(generar))

