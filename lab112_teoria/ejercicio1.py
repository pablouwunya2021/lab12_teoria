

def ordenar_diccionarios(lista, key):

    return sorted(lista, key=lambda x: x[key])


# Ejemplo de uso
if __name__ == "__main__":
    # Lista original de diccionarios
    D = [
        {'make': 'Nokia', 'model': 216, 'color': 'Black'},
        {'make': 'Apple', 'model': 2, 'color': 'Silver'},
        {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]
    
    print("Lista original:")
    for item in D:
        print(item)
    
    # Ordenar por 'model'
    D_ordenado = ordenar_diccionarios(D, 'model')
    
    print("\nLista ordenada por 'model':")
    for item in D_ordenado:
        print(item)
    
    # Otros ejemplos
    print("\nLista ordenada por 'make':")
    D_ordenado_make = ordenar_diccionarios(D, 'make')
    for item in D_ordenado_make:
        print(item)
    
    print("\nLista ordenada por 'color':")
    D_ordenado_color = ordenar_diccionarios(D, 'color')
    for item in D_ordenado_color:
        print(item)
