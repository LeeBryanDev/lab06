# info_archivo.py
# comprobacion de archivo con try y except
# usa modo r y muestra atributos
# usa modo r de lectura, muestra atributos del objeto archivo

# comprueba si archivo existe con open
# ejecuta comprobacion de existencia
def archivo_existe(nombre):
    try:
        archivo = open(nombre, 'r')
        contenido = archivo.read()
        print('nombre del archivo:', archivo.name)
        print('modo de acceso:', archivo.mode)
        archivo.close()
        print('archivo cerrado:', archivo.closed)
        if contenido == '':
            print('archivo vacio')
        else:
            cantidad = len(contenido)
            print('caracteres encontrados:', cantidad)
        return True
    except:
        print('archivo no existe')
        return False

# busca cantidad de caracteres con read
# ejecuta busqueda de info
def buscar_informacion(nombre):
    archivo_lectura = open(nombre, 'r')
    texto = archivo_lectura.read()
    archivo_lectura.close()
    cantidad_caracteres = len(texto)
    print('el archivo tiene', cantidad_caracteres, 'caracteres')

# ejecuta comprobacion de existencia
archivo_existe('actividades/actividad1/archivoPrueba.txt')
# ejecuta busqueda de info
buscar_informacion('actividades/actividad1/archivoPrueba.txt')
