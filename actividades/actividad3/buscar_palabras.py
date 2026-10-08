# buscar_palabras.py
# busqueda de palabras con readlines y split
# usa open con modo r, readlines, split y bucles anidados

# busca palabra en archivo con split
# ejecuta busqueda de palabra
def buscar_palabra(nombre_archivo, palabra_buscar):
    archivo_lectura = open(nombre_archivo, 'r')
    lineas = archivo_lectura.readlines()
    archivo_lectura.close()
    indice_linea = 1
    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            if palabra == palabra_buscar:
                print('linea', indice_linea, 'palabra', palabra_buscar)
        indice_linea = indice_linea + 1

# genera lista ordenada de palabras unicas
# ejecuta generacion de lista
def generar_lista_ordenada(nombre_entrada, nombre_salida):
    archivo_entrada = open(nombre_entrada, 'r')
    texto = archivo_entrada.read()
    archivo_entrada.close()
    palabras = texto.split()
    palabras_unicas = []
    for palabra in palabras:
        if palabra not in palabras_unicas:
            palabras_unicas.append(palabra)
    palabras_ordenadas = sorted(palabras_unicas)
    archivo_salida = open(nombre_salida, 'w')
    for palabra in palabras_ordenadas:
        archivo_salida.write(palabra + '\n')
    archivo_salida.close()

# ejecuta busqueda de palabra
buscar_palabra('actividades/actividad1/archivoPrueba.txt', 'luz')
# ejecuta generacion de lista
generar_lista_ordenada('actividades/actividad1/archivoPrueba.txt', 'actividades/actividad3/palabras_unicas.txt')
