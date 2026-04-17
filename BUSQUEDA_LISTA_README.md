# Búsqueda en Lista

Un programa Python que implementa funciones para buscar, filtrar, calcular y ordenar elementos en una lista de números.

## Lista de trabajo

```python
[12, 45, 78, 23, 56, 89, 34, 67]
```

## Características

- ✅ **Buscar número**: Encuentra el índice de un número en la lista
- ✅ **Números mayores**: Filtra números según un umbral especificado
- ✅ **Calcular promedio**: Obtiene el promedio de todos los elementos
- ✅ **Ordenar lista**: Ordena los números de menor a mayor
- ✅ **Menú interactivo**: Accede fácilmente a todas las funciones

## Requisitos

- Python 3.6 o superior

## Cómo usar

### Ejecutar el programa

```bash
python busqueda_lista.py
```

### Opciones del menú

**1. Buscar número en la lista**
- Solicita un número
- Usa `.index()` para encontrarlo
- Devuelve el índice o -1 si no existe
- Muestra tanto el índice como la posición (contando desde 1)

**2. Números mayores a un umbral**
- Solicita un valor de umbral
- Usa comprensión de listas para filtrar
- Devuelve una nueva lista con números > umbral
- Muestra la cantidad de coincidencias

**3. Calcular promedio**
- Usa `sum()` para la suma total
- Usa `len()` para contar elementos
- Devuelve promedio = suma / cantidad
- Muestra desglose completo

**4. Ordenar lista**
- Usa `sorted()` para crear lista ordenada
- No modifica la lista original
- Ordena de menor a mayor
- Muestra lista original y ordenada

**5. Mostrar lista actual**
- Visualiza la lista de números

**6. Salir**
- Cierra el programa

## Funciones implementadas

### `buscar_numero(numero)`

```python
buscar_numero(45)  # Devuelve: 1
buscar_numero(99)  # Devuelve: -1
```

Busca un número en la lista y devuelve su índice.

### `numeros_mayores(umbral)`

```python
numeros_mayores(50)  # Devuelve: [78, 56, 89, 67]
numeros_mayores(80)  # Devuelve: [89]
```

Filtra números mayores que el umbral usando comprensión de listas.

### `promedio_lista()`

```python
promedio_lista()  # Devuelve: 50.5
```

Calcula el promedio: suma total / cantidad de elementos.

### `ordenar_lista()`

```python
ordenar_lista()  # Devuelve: [12, 23, 34, 45, 56, 67, 78, 89]
```

Ordena los números de menor a mayor usando `sorted()`.

## Ejemplo de uso

```
==================================================
          BÚSQUEDA Y ANÁLISIS EN LISTA
==================================================
Lista de trabajo: [12, 45, 78, 23, 56, 89, 34, 67]
==================================================
1. Buscar número en la lista
2. Números mayores a un umbral
3. Calcular promedio de la lista
4. Ordenar la lista
5. Mostrar lista actual
6. Salir

Selecciona una opción (1-6): 1

--- BUSCAR NÚMERO ---
Ingresa el número a buscar: 56
✓ El número 56 se encontró en el índice 4
  Posición: 5 (contando desde 1)
```

## Validaciones

El programa incluye validaciones para:
- Entrada numérica válida
- Manejo de números no encontrados
- Listas vacías o inválidas
- Mensajes claros de error

## Conceptos de Python utilizados

- **Listas**: Estructura de datos principal
- **`.index()`**: Búsqueda de elementos
- **Comprensión de listas**: Filtrado eficiente `[x for x in lista if x > umbral]`
- **`sum()`**: Suma de elementos
- **`len()`**: Contar elementos
- **`sorted()`**: Ordenamiento sin modificar original
- **Funciones**: Modularización del código
- **Manejo de excepciones**: Try/except para errores
- **Menú interactivo**: Flujo de control con while y if/elif

## Salida de ejemplo

```
--- CALCULAR PROMEDIO ---
Lista: [12, 45, 78, 23, 56, 89, 34, 67]
Cantidad de números: 8
Suma total: 404
Promedio: 50.50
```

```
--- ORDENAR LISTA ---
Lista original:  [12, 45, 78, 23, 56, 89, 34, 67]
Lista ordenada:  [12, 23, 34, 45, 56, 67, 78, 89]
(De menor a mayor)
```

## Proyectos futuros

Posibles mejoras:
- Agregar números a la lista
- Eliminar números de la lista
- Buscar números en rango
- Calcular estadísticas adicionales (mediana, desviación estándar)
- Guardar la lista en archivo
- Trabajar con múltiples listas
