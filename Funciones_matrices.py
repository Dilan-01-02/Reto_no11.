def creacionMatriz(filas:list, columnas:list, n) -> list:
    """Función que crea una matriz recibiendo como parámetros el número de filas, el número de columnas y un identificadror n
    Args:
        filas (int): Primer parámetro.
            Número de filas de la matriz.
        Columnas (int): Segundo parámtro.
            Número de columnas de la matriz.
        n : tercer parámetro
            Identificador de la matriz.

    Returns:
        list: matriz
    """
    fila =[]
    matriz = []
    print("\nELEMENTOS MATRIZ "+str(n))
    for i in range (filas):
        for j in range(columnas):
            # Ciclo for que crea la matriz insertando un número y agregandolo al final de la lista fila para agregarla al final de la lista matriz
            num = int(input("Ingrese elemento ["+str(i+1)+","+str(j+1)+"]: "))
            fila.append(num)
        matriz.append(fila)
        fila = []
    return matriz

def imprimirMatriz(matriz:list,n):
    """Función que imprime una matriz recibida coma parámtro su identificadror n también recibido como parámtro
    Args:
        matriz (list): Primer parámetro.
            Primer matriz.
        n : Segundo parámetro
            Identificador de la matriz.

    Returns:
        list: matriz
    """
    print("\nMATRIZ "+str(n))
    # Ciclo for que recorre las filas de la matriz e imprime cada una 
    for i in range(len(matriz)): print(matriz[i])