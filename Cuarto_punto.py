'''
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

'''
from Funciones_matrices import *
# Importación de las funciones: creacionMatriz e imprimirMatriz

def sumaColumnas(matriz:list):
    """Función que realiza la suma de los elementos de una columna elegida por el usuario de una matriz recibida como parámetro 
    Args:
        matriz (list): Primer parámetro.
            Primer matriz.

    """
    # Ingreso de la columna a la cual se desea que se sumen sus elementos 
    columna = int(input("\nIngrese el número de la columna a la cual quiere sumar sus elementos: "))
    resultado: float = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # Ciclo for que realiza la suma de los elementos de una columna 
            if j == columna:
                # Condicional que verifica que la columna de iteración sea igual a la columna ingresada por el usuario
                resultado += matriz[i][j]
    
    # Impresión del resultado de la suma de los elementos de una columna elegida por el usuario 
    print("\nEl resultado de la suma de los elementos de la columna "+str(columna)+" es: "+str(resultado))

if __name__ == "__main__":
    # Ingreso del tamaño de la matriz
    c = int(input("Ingrese el número de columnas de la matriz: "))
    f = int(input("Ingrese el número de filas de la matriz: "))
    # Creación de la matriz haciendo uso de la función creaciónMatriz y envío de los parámetros f,c y ""
    matriz = creacionMatriz(f,c,"")
    # Impresión de la matriz haciendo uso de la función imprimirMatriz y envío de los parámetros matriz y ""
    imprimirMatriz(matriz,"")
    # Uso de la función sumaColumnas y envío del parámetro matriz
    sumaColumnas(matriz)
