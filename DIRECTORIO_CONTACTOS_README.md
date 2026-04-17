# Directorio de Contactos

Un programa Python interactivo para gestionar un directorio de contactos usando diccionarios anidados.

## Características

- ✅ **Agregar contacto**: Añade nuevos contactos con email, teléfono y ciudad
- ✅ **Ver todos los contactos**: Visualiza todos los contactos guardados
- ✅ **Buscar por nombre**: Busca un contacto específico por nombre (flexible, sin distinción de mayúsculas)
- ✅ **Actualizar teléfono**: Modifica el teléfono de un contacto existente
- ✅ **Eliminar contacto**: Remueve un contacto del directorio

## Requisitos

- Python 3.6 o superior

## Cómo usar

### Ejecutar el programa

```bash
python directorio_contactos.py
```

### Opciones del menú

**1. Agregar contacto**
- Solicita el nombre del contacto
- Pide el email (con validación)
- Solicita el teléfono
- Pide la ciudad
- Agrega el contacto al diccionario

**2. Ver todos los contactos**
- Muestra todos los contactos guardados
- Presenta para cada uno:
  - Nombre
  - Email
  - Teléfono
  - Ciudad
- Indica el total de contactos

**3. Buscar por nombre**
- Pide el nombre del contacto
- Usa `.get()` para acceso seguro
- Muestra todos los datos del contacto encontrado
- Manejo flexible de búsqueda (no distingue mayúsculas)

**4. Actualizar teléfono**
- Busca el contacto por nombre
- Solicita el nuevo teléfono
- Accede al diccionario anidado y actualiza el campo

**5. Eliminar contacto**
- Pide el nombre del contacto
- Usa `.pop()` para eliminar la entrada completa
- Muestra los datos eliminados

**6. Salir**
- Cierra el programa

## Estructura de datos

El directorio usa un diccionario de diccionarios:

```python
directorio = {
    "nombre_contacto": {
        "email": "email@domain.com",
        "teléfono": "555-1234",
        "ciudad": "Madrid"
    },
    "otro_contacto": {
        "email": "otro@domain.com",
        "teléfono": "555-5678",
        "ciudad": "Barcelona"
    }
}
```

## Ejemplo de uso

```
==================================================
    DIRECTORIO DE CONTACTOS
==================================================
1. Agregar contacto
2. Ver todos los contactos
3. Buscar por nombre
4. Actualizar teléfono
5. Eliminar contacto
6. Salir

Selecciona una opción (1-6): 1

--- AGREGAR CONTACTO ---
Nombre del contacto: Ana López
Email: ana@email.com
Teléfono: 555-9999
Ciudad: Valencia
✓ Contacto 'Ana López' agregado exitosamente.
```

## Validaciones

El programa incluye validaciones para:
- Nombres no vacíos
- Emails válidos (contienen @)
- Teléfonos no vacíos
- Ciudades no vacías
- No permitir contactos duplicados
- Búsqueda flexible de contactos

## Conceptos de Python utilizados

- **Diccionarios anidados**: Estructura principal del directorio
- **Método `.items()`**: Iteración sobre pares clave-valor
- **Método `.get()`**: Acceso seguro a diccionarios
- **Método `.pop()`**: Eliminación segura de entradas
- **Bucles y condicionales**: Control de flujo
- **Funciones**: Modularización del código
- **Validación de entrada**: Manejo robusto de datos usuario

## Datos iniciales

El programa carga con dos contactos de ejemplo:
- Juan Pérez (juan@email.com, 555-1234, Madrid)
- María García (maria@email.com, 555-5678, Barcelona)

Puedes agregar, modificar o eliminar contactos según necesites.

## Proyectos futuros

Posibles mejoras:
- Guardar el directorio en archivo (JSON)
- Cargar directorio desde archivo al iniciar
- Buscar por email o teléfono
- Importar contactos desde CSV
- Sincronizar con servicios en la nube
- Crear copias de seguridad
