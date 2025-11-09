

def eliminar_elementos(lista_original, elementos_a_borrar):
 
    # Usamos filter con lambda para mantener solo los elementos que NO están en la lista de borrado
    return list(filter(lambda x: x not in elementos_a_borrar, lista_original))


# Ejemplo de uso
if __name__ == "__main__":
    # Listas originales
    lista_colores = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
    borrar = ['amarillo', 'café', 'blanco']
    
    print(f"Lista original: {lista_colores}")
    print(f"Elementos a borrar: {borrar}")
    
    # Eliminar elementos
    resultado = eliminar_elementos(lista_colores, borrar)
    
    print(f"\nLista resultante: {resultado}")
    
    # Otros ejemplos
    print("\n" + "="*60)
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    borrar_numeros = [2, 4, 6, 8]
    
    print(f"\nLista de números: {numeros}")
    print(f"Números a borrar: {borrar_numeros}")
    resultado_numeros = eliminar_elementos(numeros, borrar_numeros)
    print(f"Resultado: {resultado_numeros}")
    
    # Ejemplo cuando ningún elemento coincide
    print("\n" + "="*60)
    frutas = ['manzana', 'pera', 'uva', 'sandía']
    borrar_frutas = ['naranja', 'limón']
    
    print(f"\nLista de frutas: {frutas}")
    print(f"Frutas a borrar: {borrar_frutas}")
    resultado_frutas = eliminar_elementos(frutas, borrar_frutas)
    print(f"Resultado (nada se eliminó): {resultado_frutas}")
    
    # Ejemplo cuando se eliminan todos los elementos
    print("\n" + "="*60)
    letras = ['a', 'b', 'c']
    borrar_letras = ['a', 'b', 'c', 'd']
    
    print(f"\nLista de letras: {letras}")
    print(f"Letras a borrar: {borrar_letras}")
    resultado_letras = eliminar_elementos(letras, borrar_letras)
    print(f"Resultado (todo eliminado): {resultado_letras}")
