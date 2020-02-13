'''
#* Archivo para ejecutar una tarea (main.py) especificando el nombre de la carpeta en la variable 'subdir'.

De esta manera, todos los paquetes con sus módulos del repositorio son accesibles entre sí, y dentro un paquete no se necesita especificar su nombre para acceder a sus módulos.

#! Ejecutar una tarea estando en el directorio de su carpeta puede arrojar la excepción ModuleNotFoundError.
'''

from sys import path
from os.path import dirname, join, abspath

# ruta del directorio actual, que debe ser la del repositorio local: /modelado-simulacion
current_dir = dirname(__file__)
# nombre de la carpeta de la tarea a ejecutar
subdir = 'pseudoaleatorios'
# ruta absoluta del directorio anterior
subdir_path = join(current_dir, subdir)
# agregar ruta anterior al PATH de Python para importar paquetes y módulos
path.append(abspath(subdir_path))

# nombre del archivo a ejecutar, para cada tarea debe ser main.py
file_name = 'main.py'
# ejecutar el archivo
with open(join(subdir_path, file_name), encoding='utf-8') as file:
    code = compile(file.read(), file_name, 'exec')
    exec(code)
