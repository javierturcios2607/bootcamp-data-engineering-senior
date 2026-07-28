
import time

ruta_config="phase-1-software-engineering/week-01-python-avanzado/data/raw/practica.csv"

def cronometro_a(funcion_b):

    def wrapper_c(*args, **kwargs):
        inicio=time.time()

        resultado=funcion_b(*args, **kwargs)

        fin=time

        return f"el tiempo que tomo la funcion es:{time.time()-inicio}"
    return wrapper_c




@cronometro_a
def leer_transacciones(fichero):
    with open(fichero,"r", encoding="utf-8") as f:
        next(f)# salta el encabezado
        for lineas in f:
            yield lineas.rstrip()


if __name__=="__main__":

    archivo=ruta_config
    generador_lectura=leer_transacciones(archivo)

    print("Leyendo data")
    


## aprendi a usar documentos en otra ruta y a poder pedirle al generador linea por linea del archivo sin saturar la RAM





