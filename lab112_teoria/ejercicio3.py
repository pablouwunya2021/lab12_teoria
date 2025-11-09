

def transpuesta(matriz):
 
    # Usamos zip con * para desempaquetar las filas y combinarlas en columnas
    # map con lambda convierte las tuplas resultantes en listas
    return list(map(lambda columna: list(columna), zip(*matriz)))


# Ejemplo de uso
if __name__ == "__main__":
    # Matriz original
    X = [
        [1, 2, 3, 1],
        [4, 5, 6, 0],
        [7, 8, 9, -1]
    ]
    
    print("Matriz original X:")
    for fila in X:
        print(fila)
    
    # Calcular transpuesta
    Y = transpuesta(X)
    
    print("\nMatriz transpuesta Y:")
    for fila in Y:
        print(fila)
    
    # Otro ejemplo con matriz cuadrada
    print("\n" + "="*40)
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("\nMatriz cuadrada A:")
    for fila in A:
        print(fila)
    
    B = transpuesta(A)
    print("\nMatriz transpuesta B:")
    for fila in B:
        print(fila)
    
    # Verificar que la transpuesta de la transpuesta es la original
    print("\n" + "="*40)
    print("\nVerificación: Transpuesta de la transpuesta")
    C = transpuesta(Y)
    print("¿Es igual a la original?", C == X)
    for fila in C:
        print(fila)
