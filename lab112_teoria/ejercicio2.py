
def potencia_nesima(lista, n):

    return list(map(lambda x: x**n, lista))


# Ejemplo de uso
if __name__ == "__main__":
    # Lista original
    lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"Lista original: {lista_original}")
    
    # Calcular potencia n=3
    n = 3
    resultado = potencia_nesima(lista_original, n)
    print(f"\nPotencia {n}: {resultado}")
    
    # Otros ejemplos
    print(f"\nPotencia 2: {potencia_nesima(lista_original, 2)}")
    print(f"Potencia 4: {potencia_nesima(lista_original, 4)}")
    print(f"Potencia 1: {potencia_nesima(lista_original, 1)}")
    
    # Ejemplo con otra lista
    otra_lista = [2, 4, 6, 8, 10]
    print(f"\nOtra lista: {otra_lista}")
    print(f"Potencia 3: {potencia_nesima(otra_lista, 3)}")
