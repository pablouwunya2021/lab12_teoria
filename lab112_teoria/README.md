# Laboratorio No. 12 - Funciones Lambda en Python

**Universidad del Valle de Guatemala**  
**Facultad de Ingeniería**  
**Ingeniería en Ciencia de la Computación y Tecnologías de la Información**

## Descripción

Este laboratorio contiene 4 ejercicios que demuestran el uso de funciones lambda en Python para operaciones con listas, diccionarios y matrices.

## Estructura del Proyecto

```
.
├── README.md
├── ejercicio1.py    # Ordenar lista de diccionarios
├── ejercicio2.py    # Calcular potencia n-ésima
├── ejercicio3.py    # Calcular matriz transpuesta
└── ejercicio4.py    # Eliminar elementos de una lista
```

## Ejercicios

### Ejercicio 1 (25%) - Ordenar Lista de Diccionarios

**Descripción:** Ordena una lista de diccionarios con respecto a un key indicado usando funciones lambda.

**Uso:**
```python
python ejercicio1.py
```

**Ejemplo:**
```python
D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Ordenar por 'model'
resultado = ordenar_diccionarios(D, 'model')
# Salida: [{'make': 'Apple', 'model': 2, ...}, {'make': 'Samsung', 'model': 7, ...}, ...]
```

**Lambda utilizada:** `lambda x: x[key]`

---

### Ejercicio 2 (25%) - Potencia N-ésima

**Descripción:** Calcula la potencia n-ésima de cada elemento en una lista de enteros usando funciones lambda.

**Uso:**
```python
python ejercicio2.py
```

**Ejemplo:**
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

resultado = potencia_nesima(lista, n)
# Salida: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

**Lambda utilizada:** `lambda x: x**n`

---

### Ejercicio 3 (25%) - Matriz Transpuesta

**Descripción:** Calcula la matriz transpuesta X^T usando funciones lambda.

**Uso:**
```python
python ejercicio3.py
```

**Ejemplo:**
```python
X = [
    [1, 2, 3, 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]
]

Y = transpuesta(X)
# Salida:
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9],
#  [1, 0, -1]]
```

**Lambda utilizada:** `lambda columna: list(columna)`

---

### Ejercicio 4 (25%) - Eliminar Elementos

**Descripción:** Elimina elementos indicados de una lista usando funciones lambda.

**Uso:**
```python
python ejercicio4.py
```

**Ejemplo:**
```python
lista_original = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
elementos_a_borrar = ['amarillo', 'café', 'blanco']

resultado = eliminar_elementos(lista_original, elementos_a_borrar)
# Salida: ['rojo', 'verde', 'azul', 'gris', 'negro']
```

**Lambda utilizada:** `lambda x: x not in elementos_a_borrar`

---

## Requisitos

- Python 3.6 o superior

## Instrucciones de Ejecución

1. Clonar el repositorio
2. Ejecutar cada ejercicio individualmente:
   ```bash
   python ejercicio1.py
   python ejercicio2.py
   python ejercicio3.py
   python ejercicio4.py
   ```

## Video de Demostración

[Insertar aquí el enlace al video de YouTube no listado mostrando la ejecución de todos los programas]

## Conceptos Clave

### Funciones Lambda
Las funciones lambda son funciones anónimas de una sola línea en Python:
```python
lambda argumentos: expresión
```

### Funciones Utilizadas

1. **`sorted()`** - Ordena iterables
2. **`map()`** - Aplica una función a cada elemento
3. **`filter()`** - Filtra elementos según una condición
4. **`zip()`** - Combina múltiples iterables

## Autor

Pablo CABRERA
Universidad del Valle de Guatemala



---

## Notas Adicionales

- Todos los ejercicios están implementados usando funciones lambda como se solicitó
- Cada archivo incluye múltiples ejemplos de prueba
- El código está documentado con docstrings
- Se incluyen casos de prueba adicionales para validar el funcionamiento
