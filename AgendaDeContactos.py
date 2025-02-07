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
    opcion = input('\r\nSeleccione una de las opciones : ') # Str para validar respuestas y evitar el colapso del programa
    if opcion == '1':
      agregar_contacto()
      pregunta = False
    elif opcion == '2':
      editar_contacto()
      pregunta = False
    elif opcion == '3':
      mostrar_contactos()
      pregunta = False
    elif opcion == '4':
      buscar_contacto()
      pregunta = False
    elif opcion == '5':
      eliminar_contacto()
      pregunta = False
    elif opcion == '6':
      print('\r\n--Hasta luego--')
      pregunta = False
    else:
      print('\r\nOpción no válida, intente de nuevo')

def eliminar_contacto():
  """Elimina un contacto de la agenda"""
  print('\r\nIngresa el nombre del contacto que deseas eliminar...\r\n')
  # Solicitar el nombre del contacto
  nombre = input('Nombre del contacto: ')
  # Manejo de excepciones
  try:
    # Eliminar el contacto
    os.remove(CARPETA + nombre + EXTENSION)
    print(f'\r\n-- Contacto ({nombre}) eliminado correctamente --\r\n')
  except FileNotFoundError:
    print('\r\nEl contacto no existe en la agenda!!\r\n')
  # Volver a preguntar si se desea realizar otra acción
  main()

def buscar_contacto():
  """Busca un contacto en específico en el directorio"""
  print('\r\nIngresa el nombre del contacto que deseas buscar...\r\n')
  # Solicitar el nombre del contacto
  nombre = input('Nombre del contacto: ')
  # Manejo de excepciones
  try: 
    print('\r\n-------------------\r\n')
    print('Datos del contacto:')
    with open(CARPETA + nombre + EXTENSION) as contacto:
      for linea in contacto:
        print(linea.rstrip())
    print('\r\n-------------------\r\n')
  except FileNotFoundError:
    print('\r\nEl contacto no existe en la agenda!!\r\n')
  # Volver a preguntar si se desea realizar otra acción
  main()

def mostrar_contactos():
  """Muestra todos los contactos almacendados en el directorio"""
  archivos = os.listdir(CARPETA)
  archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
  for archivo in archivos_txt:
    # Separador de contactos
    print('\r\n-------------------\r\n')
    with open(CARPETA + archivo) as contacto:
      for linea in contacto:
        # Imprimir los datos del contacto
        print(linea.rstrip())
      # Separador de contactos
      print('\r\n-------------------\r\n')
  # Volver a preguntar si se desea realizar otra acción
  main()

def editar_contacto():
  """Edita un contacto de la agenda"""
  print('\r\nIngresa el nombre del contacto que deseas editar...\r\n')
  # Solicitar el nombre antiguo del contacto
  nombre_antiguo = input('Nombre del contacto: ')
  # Validar si el contacto existe
  existe = existe_contacto(nombre_antiguo)
  if existe:
    with open(CARPETA + nombre_antiguo + EXTENSION, 'w') as archivo:
      # Editar los datos del contacto
      nombre_contacto = input('Nuevo nombre: ')
      telefono_contacto = input('Nuevo teléfono: ')
      ocupacion_contacto = input('Nueva ocupación: ')
      # Instanciar el objeto de contacto
      contacto = Contacto(nombre_contacto, telefono_contacto, ocupacion_contacto)
      # Escribir los datos en el archivo
      archivo.write('Nombre: ' + contacto.nombre + '\r\n')
      archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
      archivo.write('Ocupación: ' + contacto.ocupacion + '\r\n')
      # Renombrar el archivo
      os.rename(CARPETA + nombre_antiguo + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
      # Mensaje de confirmación de contacto editado
      print('\r\n-- Contacto editado correctamente --\r\n')
  else:
    print('\r\nEl contacto no existe en la agenda!!\r\n')
  # Volver a preguntar si se desea realizar otra acción
  main()

def agregar_contacto():
  """Agrega un contacto a la agenda"""
  print('\r\nIngresa los datos del contacto para agregarlo a la agenda...\r\n')
  # Registrar el nombre del contacto
  nombre_contactacto = input('Nombre del contacto: ')
  # Validar si el contacto ya existe
  existe = existe_contacto(nombre_contactacto)
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
    # Mensaje de confirmación de contacto agregado
    print('\r\n-- Contacto agregado correctamente --\r\n')
  else:
    print('\r\nEl contacto ya existe en la agenda!!\r\n') # Mensaje de error
    # Volver a preguntar si se desea realizar otra acción
  main()

def existe_contacto(nombre):
  """Valida si el contacto existe en la agenda"""
  return os.path.isfile(CARPETA + nombre + EXTENSION)

def mostrar_menu():
  """Menu principal de la agenda"""
  print('\r\nSeleccione del menú lo que desea hacer:\r\n')
  print('1) Agregar contacto')
  print('2) Editar contacto')
  print('3) Ver contacto')
  print('4) Buscar contacto')
  print('5) Eliminar contacto')
  print('6) Salir')

def crear_directorio():
  """Crea el directorio donde se almacenarán los contactos"""
  if not os.path.exists(CARPETA):
    os.makedirs(CARPETA)



main()