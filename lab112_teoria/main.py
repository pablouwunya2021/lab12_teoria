

print("="*70)
print(" LABORATORIO NO. 12 - FUNCIONES LAMBDA EN PYTHON")
print(" Universidad del Valle de Guatemala")
print("="*70)

# Ejercicio 1
print("\n" + "="*70)
print("EJERCICIO 1: Ordenar lista de diccionarios")
print("="*70)

from ejercicio1 import ordenar_diccionarios

D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

print("\nLista original:")
for item in D:
    print(f"  {item}")

D_ordenado = ordenar_diccionarios(D, 'model')
print("\nLista ordenada por 'model':")
for item in D_ordenado:
    print(f"  {item}")

# Ejercicio 2
print("\n" + "="*70)
print("EJERCICIO 2: Potencia n-ésima")
print("="*70)

from ejercicio2 import potencia_nesima

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

print(f"\nLista original: {lista_original}")
print(f"Potencia n = {n}")

resultado = potencia_nesima(lista_original, n)
print(f"Resultado: {resultado}")

# Ejercicio 3
print("\n" + "="*70)
print("EJERCICIO 3: Matriz transpuesta")
print("="*70)

from ejercicio3 import transpuesta

X = [
    [1, 2, 3, 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]
]

print("\nMatriz original X:")
for fila in X:
    print(f"  {fila}")

Y = transpuesta(X)
print("\nMatriz transpuesta Y:")
for fila in Y:
    print(f"  {fila}")

# Ejercicio 4
print("\n" + "="*70)
print("EJERCICIO 4: Eliminar elementos de lista")
print("="*70)

from ejercicio4 import eliminar_elementos

lista_colores = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
borrar = ['amarillo', 'café', 'blanco']

print(f"\nLista original: {lista_colores}")
print(f"Elementos a borrar: {borrar}")

resultado = eliminar_elementos(lista_colores, borrar)
print(f"Lista resultante: {resultado}")

print("\n" + "="*70)
print(" FIN DEL LABORATORIO")
print("="*70)
