#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Directorio de Contactos
Programa para gestionar un directorio de contactos usando diccionarios anidados.
Estructura: {nombre: {email, teléfono, ciudad}}
"""

def agregar_contacto(directorio):
    """
    Solicita los datos del contacto y lo agrega al directorio.
    """
    print("\n--- AGREGAR CONTACTO ---")
    nombre = input("Nombre del contacto: ").strip()
    
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return
    
    if nombre.lower() in [c.lower() for c in directorio.keys()]:
        print(f"Error: El contacto '{nombre}' ya existe en el directorio.")
        return
    
    email = input("Email: ").strip()
    if not email or "@" not in email:
        print("Error: Ingresa un email válido.")
        return
    
    telefono = input("Teléfono: ").strip()
    if not telefono:
        print("Error: El teléfono no puede estar vacío.")
        return
    
    ciudad = input("Ciudad: ").strip()
    if not ciudad:
        print("Error: La ciudad no puede estar vacía.")
        return
    
    # Crear entrada en el diccionario principal
    directorio[nombre] = {
        "email": email,
        "teléfono": telefono,
        "ciudad": ciudad
    }
    print(f"✓ Contacto '{nombre}' agregado exitosamente.")


def ver_todos_contactos(directorio):
    """
    Muestra todos los contactos del directorio con sus datos.
    """
    print("\n--- DIRECTORIO DE CONTACTOS ---")
    
    if not directorio:
        print("El directorio está vacío.")
        return
    
    print(f"\nTotal de contactos: {len(directorio)}\n")
    print("=" * 80)
    
    for nombre, datos in directorio.items():
        print(f"\nNombre: {nombre}")
        print(f"  Email:     {datos['email']}")
        print(f"  Teléfono:  {datos['teléfono']}")
        print(f"  Ciudad:    {datos['ciudad']}")
        print("-" * 80)


def buscar_contacto(directorio):
    """
    Busca un contacto por nombre y muestra sus datos.
    Usa .get() para evitar errores si no existe.
    """
    print("\n--- BUSCAR CONTACTO ---")
    nombre = input("Nombre del contacto a buscar: ").strip()
    
    # Buscar de forma flexible (sin distinción de mayúsculas/minúsculas)
    contacto_encontrado = None
    nombre_clave = None
    
    for clave in directorio.keys():
        if clave.lower() == nombre.lower():
            contacto_encontrado = directorio.get(clave)
            nombre_clave = clave
            break
    
    if contacto_encontrado:
        print(f"\n✓ Contacto encontrado:\n")
        print(f"Nombre:    {nombre_clave}")
        print(f"Email:     {contacto_encontrado['email']}")
        print(f"Teléfono:  {contacto_encontrado['teléfono']}")
        print(f"Ciudad:    {contacto_encontrado['ciudad']}")
    else:
        print(f"❌ No se encontró el contacto '{nombre}' en el directorio.")


def actualizar_telefono(directorio):
    """
    Busca un contacto por nombre y actualiza su teléfono.
    """
    print("\n--- ACTUALIZAR TELÉFONO ---")
    nombre = input("Nombre del contacto: ").strip()
    
    # Buscar de forma flexible
    nombre_clave = None
    for clave in directorio.keys():
        if clave.lower() == nombre.lower():
            nombre_clave = clave
            break
    
    if nombre_clave:
        nuevo_telefono = input("Nuevo teléfono: ").strip()
        if not nuevo_telefono:
            print("Error: El teléfono no puede estar vacío.")
            return
        
        directorio[nombre_clave]["teléfono"] = nuevo_telefono
        print(f"✓ Teléfono de '{nombre_clave}' actualizado a: {nuevo_telefono}")
    else:
        print(f"❌ No se encontró el contacto '{nombre}'.")


def eliminar_contacto(directorio):
    """
    Busca un contacto por nombre y lo elimina del directorio.
    Usa .pop() para remover la entrada completa.
    """
    print("\n--- ELIMINAR CONTACTO ---")
    nombre = input("Nombre del contacto a eliminar: ").strip()
    
    # Buscar de forma flexible
    nombre_clave = None
    for clave in directorio.keys():
        if clave.lower() == nombre.lower():
            nombre_clave = clave
            break
    
    if nombre_clave:
        contacto_eliminado = directorio.pop(nombre_clave)
        print(f"✓ Contacto '{nombre_clave}' eliminado del directorio.")
        print(f"   Datos: {contacto_eliminado}")
    else:
        print(f"❌ No se encontró el contacto '{nombre}'.")


def mostrar_menu():
    """
    Muestra el menú principal de opciones.
    """
    print("\n" + "="*50)
    print("    DIRECTORIO DE CONTACTOS")
    print("="*50)
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar por nombre")
    print("4. Actualizar teléfono")
    print("5. Eliminar contacto")
    print("6. Salir")
    print("="*50)


def main():
    """
    Función principal que controla el flujo del programa.
    """
    # Diccionario de diccionarios para almacenar contactos
    directorio = {}
    
    # Agregar algunos contactos de ejemplo
    directorio["Juan Pérez"] = {
        "email": "juan@email.com",
        "teléfono": "555-1234",
        "ciudad": "Madrid"
    }
    directorio["María García"] = {
        "email": "maria@email.com",
        "teléfono": "555-5678",
        "ciudad": "Barcelona"
    }
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            agregar_contacto(directorio)
        elif opcion == "2":
            ver_todos_contactos(directorio)
        elif opcion == "3":
            buscar_contacto(directorio)
        elif opcion == "4":
            actualizar_telefono(directorio)
        elif opcion == "5":
            eliminar_contacto(directorio)
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("Error: Selecciona una opción válida (1-6).")


if __name__ == "__main__":
    main()
