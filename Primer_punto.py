'''
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

'''
from Funciones_matrices import *
# Importación de las funciones: creacionMatriz e imprimirMatriz

def sumaMatrices(matriz1:list,matriz2:list) -> list:
    """Función que calcula la suma de dos matrices recibidas como parámetros.

    Args:
        matriz1 (list): Primer parámetro.
            Primer matriz.
        matriz2 (list): Segundo parámetro.
            Segundo arreglo.

    Returns:
        list: resultado
    """
    fila = []
    resultado = []
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            # Ciclo for que recorre cada elemento de ambas matrices y suma cada uno
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)
        fila = []
    return resultado

def restaMatrices(matriz1:list,matriz2:list) -> list:
    """Función que calcula la suma de dos matrices recibidas como parámetros.
    Args:
        matriz1 (list): Primer parámetro.
            Primer matriz.
        matriz2 (list): Segundo parámetro.
            Segundo arreglo.

    Returns:
        list: resultado
    """
    fila = []
    resultado = []
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            # Ciclo for que recorre cada elemento de ambas matrices y resta cada uno
            suma = matriz1[i][j] - matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)
        fila = []
    return resultado
    
if __name__ == "__main__":
    opcion: int = 0
    bandera: bool = True
    # Ingreso del tamaño de las matrices
    filas = int(input("Ingrese el número de filas de las matrices: "))
    columnas = int(input("Ingrese el número de columnas de las matrices: "))
    # Creación de la matriz 1 haciendo uso de la función creacionMatriz y envio de los parámetros filas, columnas y 1
    matriz1 = creacionMatriz(filas, columnas, 1)
    # Creación de la matriz 2 haciendo uso de la función creacionMatriz y envio de los parámetros filas, columnas y 2
    matriz2 = creacionMatriz(filas, columnas, 2)
    while bandera or opcion != 3:
        # Ciclo while que muestra un menú de sumar o restar matrices para que el usuario elija que opción desea ejecutar  
        bandera = False
        print("\nELIJA LA OPCIÓN QUE DESEA EJECUTAR")
        # Mostrando las opciones de sumar o restar matrices y salir 
        opcion = int(input("\n1. SUMAR LAS MATRICES \n2. RESTAR LAS MATRICES \n3. SALIR\n"))
        match opcion:
            # Condicional match que ejecuta el caso elegido por el usuario
            case 1:
                suma = sumaMatrices(matriz1, matriz2)
                print("\nEl resultado de la suma de matrices es: ")
                imprimirMatriz(suma,"SUMADA")
            case 2: 
                resta = restaMatrices(matriz1, matriz2)
                print("\nEl resultado de la resta de matrices es: ")
                imprimirMatriz(resta,"RESTADA")
            case 3:
                print("\nHasta luego")
            case _:
                print("\nLa opción ingresada no es válida")