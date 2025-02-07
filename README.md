# Agenda de Contactos

## Descripción

**Agenda de Contactos** es una aplicación simple desarrollada en Python que permite gestionar una lista de contactos de manera local. Cada contacto se almacena como un archivo `.txt` en una carpeta dedicada, lo que facilita la organización y recuperación de la información.

El programa está diseñado para ser intuitivo y fácil de usar, ofreciendo un menú interactivo con opciones básicas para administrar los contactos. Aunque todavía está en desarrollo, ya incluye funcionalidades clave como agregar contactos y validar si un contacto ya existe.

## Características actuales

- **Agregar contactos**: Los usuarios pueden ingresar el nombre, teléfono y ocupación de un contacto. La información se guarda en un archivo `.txt` dentro de la carpeta `Contactos/`.
- **Validación de contactos existentes**: Antes de crear un nuevo contacto, el programa verifica si ya existe un archivo con ese nombre para evitar duplicados.
- **Menú interactivo**: Un menú principal permite a los usuarios seleccionar entre varias opciones (agregar, editar, ver, buscar y eliminar contactos).
- **Creación automática de directorios**: Si la carpeta `Contactos/` no existe, el programa la crea automáticamente.

## Funcionalidades en desarrollo

Aunque el programa ya tiene una base sólida, aún hay funcionalidades que se están trabajando para mejorar la experiencia del usuario. Estas incluyen:

- **Editar contactos**: Permitir a los usuarios modificar la información de un contacto existente.
- **Ver contactos**: Mostrar la información completa de un contacto específico.
- **Buscar contactos**: Encontrar un contacto por su nombre y mostrar sus detalles.
- **Eliminar contactos**: Dar la opción de eliminar un contacto de la agenda.

## Requisitos

Para ejecutar este programa, necesitarás:

- Python 3.x instalado en tu sistema.
- Permisos de escritura en el directorio donde se almacenarán los contactos.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Lstrappare/Agenda-de-Contacto-Py.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd agenda-contactos
   ```
3. Ejecuta el programa:
   ```bash
   python main.py
   ```

## Estructura del proyecto

- **`main.py`**: Archivo principal que contiene la lógica del programa.
- **`Contactos/`**: Carpeta donde se almacenan los archivos de los contactos.
- **Clase `Contacto`**: Define la estructura de un contacto con atributos como nombre, teléfono y ocupación.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar en este proyecto, no dudes en abrir un issue o enviar un pull request. Algunas ideas para contribuir incluyen:

- Implementar las funcionalidades pendientes (editar, ver, buscar y eliminar contactos).
- Mejorar la interfaz de usuario.
- Agregar validaciones adicionales para manejar errores.
- Crear pruebas unitarias para garantizar la estabilidad del código.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE). Esto significa que puedes usar, modificar y distribuir el código libremente, siempre que incluyas la licencia original.

---

### Notas adicionales

Este programa está diseñado como un ejercicio práctico para aprender conceptos básicos de programación en Python, como manejo de archivos, creación de clases y uso de funciones. A medida que avances en el desarrollo, podrás agregar más características avanzadas, como una interfaz gráfica o una base de datos para almacenar los contactos.

---
