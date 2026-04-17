#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestor de Compras
Programa para gestionar una lista de artículos de compra con opciones para:
- Agregar artículos
- Ver lista de compras
- Calcular total
- Eliminar artículos
"""

def agregar_articulo(lista_compras):
    """
    Solicita al usuario los datos del producto y lo agrega a la lista.
    """
    print("\n--- AGREGAR ARTÍCULO ---")
    producto = input("Nombre del producto: ").strip()
    
    if not producto:
        print("Error: El nombre del producto no puede estar vacío.")
        return
    
    try:
        precio = float(input("Precio unitario: $"))
        cantidad = int(input("Cantidad: "))
        
        if precio < 0 or cantidad < 0:
            print("Error: El precio y cantidad no pueden ser negativos.")
            return
        
        # Crear diccionario del artículo
        articulo = {
            "producto": producto,
            "precio": precio,
            "cantidad": cantidad
        }
        
        # Agregar a la lista
        lista_compras.append(articulo)
        print(f"✓ '{producto}' agregado a la lista de compras.")
    
    except ValueError:
        print("Error: Ingresa valores válidos (número para precio y cantidad).")


def ver_lista_compras(lista_compras):
    """
    Muestra todos los artículos en la lista de compras con su precio y cantidad.
    """
    print("\n--- LISTA DE COMPRAS ---")
    
    if not lista_compras:
        print("La lista de compras está vacía.")
        return
    
    print(f"{'Producto':<30} {'Precio':>10} {'Cantidad':>10} {'Subtotal':>12}")
    print("-" * 65)
    
    for articulo in lista_compras:
        subtotal = articulo["precio"] * articulo["cantidad"]
        print(f"{articulo['producto']:<30} ${articulo['precio']:>9.2f} {articulo['cantidad']:>10} ${subtotal:>11.2f}")
    
    print("-" * 65)


def calcular_total(lista_compras):
    """
    Calcula y muestra el total de la lista de compras.
    """
    print("\n--- CALCULAR TOTAL ---")
    
    if not lista_compras:
        print("La lista de compras está vacía. Total: $0.00")
        return
    
    total = 0
    
    for articulo in lista_compras:
        subtotal = articulo["precio"] * articulo["cantidad"]
        total += subtotal
        print(f"{articulo['producto']}: ${subtotal:.2f}")
    
    print("-" * 40)
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("-" * 40)


def eliminar_articulo(lista_compras):
    """
    Solicita el nombre del producto a eliminar y lo remueve de la lista.
    """
    print("\n--- ELIMINAR ARTÍCULO ---")
    
    if not lista_compras:
        print("La lista de compras está vacía.")
        return
    
    producto_a_eliminar = input("Nombre del producto a eliminar: ").strip()
    
    # Buscar y eliminar el artículo
    articulo_encontrado = None
    for articulo in lista_compras:
        if articulo["producto"].lower() == producto_a_eliminar.lower():
            articulo_encontrado = articulo
            lista_compras.remove(articulo)
            print(f"✓ '{articulo['producto']}' eliminado de la lista.")
            break
    
    if articulo_encontrado is None:
        print(f"Error: No se encontró '{producto_a_eliminar}' en la lista.")


def mostrar_menu():
    """
    Muestra el menú principal de opciones.
    """
    print("\n" + "="*50)
    print("       GESTOR DE COMPRAS")
    print("="*50)
    print("1. Agregar artículo")
    print("2. Ver lista de compras")
    print("3. Calcular total")
    print("4. Eliminar artículo")
    print("5. Salir")
    print("="*50)


def main():
    """
    Función principal que controla el flujo del programa.
    """
    lista_compras = []
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_articulo(lista_compras)
        elif opcion == "2":
            ver_lista_compras(lista_compras)
        elif opcion == "3":
            calcular_total(lista_compras)
        elif opcion == "4":
            eliminar_articulo(lista_compras)
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("Error: Selecciona una opción válida (1-5).")


if __name__ == "__main__":
    main()
