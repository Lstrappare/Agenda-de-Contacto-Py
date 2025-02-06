import os
CARPETA = 'Contactos/' # Directorio donde se almacenarán los contactos
EXTENSION = '.txt' # Extensión de los archivos 

# Informacion del contacto
class Contacto:
  def __init__(self, nombre, telefono, ocupacion):
    self.nombre = nombre
    self.telefono = telefono
    self.ocupacion = ocupacion


def main():
  """Aplicación de agenda de contactos"""

  # Validación del directorio de contactos
  crear_directorio()
  
  # Mostrar el menú principal
  mostrar_menu()

  # Solicitar al usuario que seleccione una opción
  pregunta = True
  while pregunta:
    opcion = input('\r\nSeleccione una de las opciones: ') # Str para validar respuestas y evitar el colapso del programa
    if opcion == '1':
      agregar_contacto()
      pregunta = False
    elif opcion == '2':
      print('\r\nEditar contacto')
      pregunta = False
    elif opcion == '3':
      print('\r\nVer contacto')
      pregunta = False
    elif opcion == '4':
      print('\r\nBuscar contacto')
      pregunta = False
    elif opcion == '5':
      print('\r\nEliminar contacto')
      pregunta = False
    else:
      print('\r\nOpción no válida, intente de nuevo')

def agregar_contacto():
  """Agrega un contacto a la agenda"""
  print('\r\nIngresa los datos del contacto para agregarlo a la agenda:\r\n')
  # Registrar el nombre del contacto
  nombre_contactacto = input('Nombre del contacto: ')
  # Validar si el contacto ya existe
  existe = os.path.isfile(CARPETA + nombre_contactacto + EXTENSION)
  if not existe:
    # Crear el archivo del contacto
    with open(CARPETA + nombre_contactacto + EXTENSION, 'w') as archivo:
      #Rellenar los demás datos del contacto
      telefono_contacto = input('Teléfono: ')
      ocupacion_contacto = input('Ocupación: ')

      # Crear el objeto de contacto
      contacto = Contacto(nombre_contactacto, telefono_contacto, ocupacion_contacto)

      archivo.write('Nombre: ' + contacto.nombre + '\r\n')
      archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
      archivo.write('Ocupación: ' + contacto.ocupacion + '\r\n')
  else:
    print('\r\nEl contacto ya existe en la agenda\r\n') # Mensaje de error

def mostrar_menu():
  """Menu principal de la agenda"""
  print('\r\nSeleccione del menú lo que desea hacer:\r\n')
  print('1) Agregar contacto')
  print('2) Editar contacto')
  print('3) Ver contacto')
  print('4) Buscar contacto')
  print('5) Eliminar contacto')

def crear_directorio():
  """Crea el directorio donde se almacenarán los contactos"""
  if not os.path.exists(CARPETA):
    os.makedirs(CARPETA)



main()