'''
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

'''
from Funciones_matrices import *
# Importación de las funciones: creacionMatriz e imprimirMatriz

def transponerMatriz(matriz:list) -> list:
    """Función que construye la matriz transpuesta de una matriz recibida como parámetro.
    Args:
        matriz (list): Primer parámetro.
            Primer matriz.

    Returns:
        list: matrizT
    """
    fila = []
    matrizT = []

    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            # Ciclo for que construye una matriz de ceros "matrizT" con un tamaño de columnas igual al número de filas de la matriz recibida y el tamaño de filas igual al número de columnas de la matriz recibida
            fila.append(0)
        matrizT.append(fila)
        fila = []
    
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            # Función for que guarda el elmento de la fila "j" y columna "i" de la matriz recibida en la posición de la fila "i" columna "j" de la matrizT 
            matrizT[i][j] = matriz[j][i]

    return matrizT


if __name__ == "__main__":
    # Ingreso del tamaño de la matriz
    c = int(input("Ingrese el número de columnas de la matriz: "))
    f = int(input("Ingrese el número de filas de la matriz: "))
    # Creación de la matriz usando la función creacionMatriz y envío de los argumentos f,c y "ORIGINAL"
    matrizOriginal = creacionMatriz(f,c,"ORIGINAL")
    # Creación de la matriz transpuesta haciendo uso de la función transponerMatriz y envío como parámetro la función original
    matrizTranspuesta = transponerMatriz(matrizOriginal)
    # Impresión de la matriz original haciendo uso de la función imprimirMatriz y envío de los parámetros matrizOriginal y "ORIGINAL"
    imprimirMatriz(matrizOriginal,"ORIGINAL")
    # Impresión de la matriz transpuesta haciendo uso de la función imprimirMatriz y envío de los parámetros matrizTranspuesta y "TRANSPUESTA"
    imprimirMatriz(matrizTranspuesta,"TRANSPUESTA")