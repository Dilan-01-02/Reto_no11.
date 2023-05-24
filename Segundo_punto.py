'''
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
'''
from Funciones_matrices import *
# Importación de las funciones: creacionMatriz e imprimirMatriz

def multiplicacionMatrices(matriz1:list,matriz2:list) -> list:
    """Función que calcula la maultiplicación de dos matrices recibidas como parámetros. 

    Args:
        matriz1 (list): Primer parámetro.
            Primer matriz.
        matriz2 (list): Segundo parámetro.
            Segundo arreglo.

    Returns:
        list: matriz3
    """
    fila = []
    matriz3 = []
    
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            # Ciclo for que crea una matriz de ceros matriz3
            fila.append(0)
        matriz3.append(fila)
        fila = [] 

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz1[0])):
                # Ciclo for que multiplica el elemento de la fila "i" columna "k" de la matriz1 con el elemento de la fila "k" columna "j" de la matriz2 y el resultado lo suma con el aonseguido en la iteración anterior  
                matriz3[i][j] += matriz1[i][k] * matriz2[k][j]  
                
    return matriz3

if __name__ == "__main__":
    filas = []
    columnas = [] 
    for i in range(2):
        # Ciclo for que recibe el número de filas y columas de una matriz y lo guarda en una lista
        c = int(input("Ingrese el número de columnas de la matriz "+str(i+1)+" : "))
        f = int(input("Ingrese el número de filas de la matriz "+str(i+1)+" : "))
        filas.append(f)
        columnas.append(c)

    if columnas[0] == filas[1]:
        # Condicional que verifica que el número de columnas de la matriz1 sea igual al número de filas de la matriz2 para que se puedan multiplicar
        # Creación de la matriz1 haciendo uso de la función creacionMatriz y envío de los parámetros filas[0], columnas[0] y 1
        matriz1 = creacionMatriz(filas[0],columnas[0],1)
        # Creación de la matriz2 haciendo uso de la función creacionMatriz y envío de los parámetros filas[0], columnas[0] y 2
        matriz2 = creacionMatriz(filas[1],columnas[1],2)
        # Uso de la función multiplicacionMatrices y envío de los parámetros matriz1 y matriz2
        resultado = multiplicacionMatrices(matriz1,matriz2)
        print("\nLA MATRIZ RESULTANTE ES")
        # Impresión del resultado haciendo uso de la función imprimirMatriz y envío de los parámetros resultado y "MULTIPLICADA"
        imprimirMatriz(resultado,"MULTIPLICADA")
    else:
        # Impresión de mensaje que indica la imposibilidad de multiplicar las matrices debido a que el número de columnas de la primera es distindo al número de filas de la segunda.
        print("No se puede realizar la multiplicación de matrices, ya que el número de columnas de la primera matriz es distinto al número de filas de la segunda matriz")