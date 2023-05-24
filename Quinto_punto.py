'''
Desarrollar un programa que sume los elementos de una fila dada de una matriz.

'''
from Funciones_matrices import *
# Importación de las funciones: creacionMatriz e imprimirMatriz

def sumaFilas(matriz:list):
    """Función que realiza la suma de los elementos de una fila elegida por el usuario de una matriz recibida como parámetro 
    Args:
        matriz (list): Primer parámetro.
            Primer matriz.

    """
    # Ingreso de la fila a a la cual se desea que se sumen sus elementos 
    fila = int(input("\nIngrese el número de la fila a la cual desea sumar sus elementos: "))
    resultado: float = 0 
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # Ciclo for que realiza la suma de los elementos de una fila 
            if i == fila:
                # Condicional que verifica que la fila de iteración sea igual a la fila ingresada por el usuario
                resultado += matriz[i][j]

    print("\nEl resultado de la suma de los elementos de la fila "+str(fila)+" es: "+str(resultado))

if __name__ == "__main__":
    # Ingreso del tamaño de la matriz
    c = int(input("Ingrese el número de columnas de la matriz: "))
    f = int(input("Ingrese el número de filas de la matriz: "))
    # Creación de la matriz haciendo uso de la función creaciónMatriz y envío de los parámetros f,c y ""
    matriz = creacionMatriz(f,c,"")
    # Impresión de la matriz haciendo uso de la función imprimirMatriz y envío de los parámetros matriz y ""
    imprimirMatriz(matriz,"")
    # Uso de la función sumaFilas y envío del parámetro matriz
    sumaFilas(matriz)