#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Búsqueda en Lista
Programa que implementa varias funciones para trabajar con una lista de números:
- Buscar un número en la lista
- Encontrar números mayores a un umbral
- Calcular el promedio
- Ordenar la lista
"""

# Lista de números para trabajar
NUMEROS = [12, 45, 78, 23, 56, 89, 34, 67]


def buscar_numero(numero, lista=NUMEROS):
    """
    Devuelve el índice del número en la lista, o -1 si no existe.
    
    Args:
        numero: El número a buscar
        lista: La lista donde buscar (por defecto NUMEROS)
    
    Returns:
        int: El índice del número o -1 si no se encontró
    """
    try:
        indice = lista.index(numero)
        return indice
    except ValueError:
        return -1


def numeros_mayores(umbral, lista=NUMEROS):
    """
    Devuelve una nueva lista con todos los números mayores que el umbral.
    Implementa dos formas: comprensión de listas y bucle for.
    
    Args:
        umbral: El valor de referencia
        lista: La lista a procesar (por defecto NUMEROS)
    
    Returns:
        list: Lista con números mayores al umbral
    """
    # Opción 1: Comprensión de listas (más eficiente)
    resultado = [numero for numero in lista if numero > umbral]
    
    # Opción 2: Bucle for (comentado, pero disponible)
    # resultado = []
    # for numero in lista:
    #     if numero > umbral:
    #         resultado.append(numero)
    
    return resultado


def promedio_lista(lista=NUMEROS):
    """
    Calcula y devuelve el promedio de todos los elementos.
    Usa sum() y len() para simplificar el cálculo.
    
    Args:
        lista: La lista de números (por defecto NUMEROS)
    
    Returns:
        float: El promedio de los números
    """
    if not lista:
        return 0
    
    total = sum(lista)
    cantidad = len(lista)
    promedio = total / cantidad
    
    return promedio


def ordenar_lista(lista=NUMEROS):
    """
    Ordena los números de menor a mayor y devuelve la lista ordenada.
    Usa sorted() para no modificar la lista original.
    
    Args:
        lista: La lista a ordenar (por defecto NUMEROS)
    
    Returns:
        list: Nueva lista ordenada de menor a mayor
    """
    # Opción 1: Usar sorted() - retorna una nueva lista sin modificar la original
    lista_ordenada = sorted(lista)
    
    # Opción 2: Usar .sort() - modifica la lista original (comentado)
    # lista.sort()
    # lista_ordenada = lista
    
    return lista_ordenada


def mostrar_lista(lista=NUMEROS):
    """
    Muestra la lista actual de números de forma legible.
    """
    print(f"\nLista actual: {lista}")


def mostrar_menu():
    """
    Muestra el menú principal de opciones.
    """
    print("\n" + "="*60)
    print("          BÚSQUEDA Y ANÁLISIS EN LISTA")
    print("="*60)
    print(f"Lista de trabajo: {NUMEROS}")
    print("="*60)
    print("1. Buscar número en la lista")
    print("2. Números mayores a un umbral")
    print("3. Calcular promedio de la lista")
    print("4. Ordenar la lista")
    print("5. Mostrar lista actual")
    print("6. Salir")
    print("="*60)


def opcion_buscar():
    """
    Opción 1: Busca un número en la lista.
    """
    print("\n--- BUSCAR NÚMERO ---")
    try:
        numero = int(input("Ingresa el número a buscar: "))
        indice = buscar_numero(numero)
        
        if indice != -1:
            print(f"✓ El número {numero} se encontró en el índice {indice}")
            print(f"  Posición: {indice + 1} (contando desde 1)")
        else:
            print(f"❌ El número {numero} NO se encuentra en la lista")
    except ValueError:
        print("Error: Ingresa un número válido.")


def opcion_mayores():
    """
    Opción 2: Encuentra números mayores a un umbral.
    """
    print("\n--- NÚMEROS MAYORES A UN UMBRAL ---")
    try:
        umbral = int(input("Ingresa el umbral: "))
        resultado = numeros_mayores(umbral)
        
        if resultado:
            print(f"✓ Números mayores a {umbral}: {resultado}")
            print(f"  Cantidad encontrada: {len(resultado)}")
        else:
            print(f"❌ No hay números mayores a {umbral}")
    except ValueError:
        print("Error: Ingresa un número válido.")


def opcion_promedio():
    """
    Opción 3: Calcula el promedio de la lista.
    """
    print("\n--- CALCULAR PROMEDIO ---")
    promedio = promedio_lista()
    suma = sum(NUMEROS)
    
    print(f"Lista: {NUMEROS}")
    print(f"Cantidad de números: {len(NUMEROS)}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio:.2f}")


def opcion_ordenar():
    """
    Opción 4: Ordena la lista de menor a mayor.
    """
    print("\n--- ORDENAR LISTA ---")
    lista_ordenada = ordenar_lista()
    
    print(f"Lista original:  {NUMEROS}")
    print(f"Lista ordenada:  {lista_ordenada}")
    print("(De menor a mayor)")


def main():
    """
    Función principal que controla el flujo del programa.
    """
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            opcion_buscar()
        elif opcion == "2":
            opcion_mayores()
        elif opcion == "3":
            opcion_promedio()
        elif opcion == "4":
            opcion_ordenar()
        elif opcion == "5":
            mostrar_lista()
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("Error: Selecciona una opción válida (1-6).")


if __name__ == "__main__":
    main()
