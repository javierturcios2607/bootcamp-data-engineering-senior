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