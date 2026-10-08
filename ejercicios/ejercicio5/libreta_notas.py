# libreta_notas.py
# libreta que combina texto binario y modos
# usa archivo texto, binario con pickle, modos r w a, with, try except, split, seek, atributos

import pickle

ARCHIVO_TEXTO = 'ejercicios/ejercicio5/notas.txt'
ARCHIVO_BINARIO = 'ejercicios/ejercicio5/notas_binario.pkl'

# escribe nota en archivo texto con modo a
# ejecuta escritura de nota
def escribir_nota(texto):
    archivo = open(ARCHIVO_TEXTO, 'a')
    archivo.write(texto + '\n')
    archivo.close()

# lee contenido del archivo texto
def leer_notas():
    archivo = open(ARCHIVO_TEXTO, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

# guarda lista en archivo binario con pickle
# guarda lista en archivo binario
def guardar_binario(lista_notas):
    archivo_binario = open(ARCHIVO_BINARIO, 'wb')
    pickle.dump(lista_notas, archivo_binario)
    archivo_binario.close()

# carga datos del archivo binario con pickle
def cargar_binario():
    archivo_binario = open(ARCHIVO_BINARIO, 'rb')
    datos = pickle.load(archivo_binario)
    archivo_binario.close()
    return datos

# muestra atributos name mode closed
def mostrar_atributos():
    archivo = open(ARCHIVO_TEXTO, 'r')
    print('nombre del archivo:', archivo.name)
    print('modo de acceso:', archivo.mode)
    archivo.seek(0)
    archivo.close()
    print('archivo cerrado:', archivo.closed)

# lista palabras unicas ordenadas
def listar_palabras_unicas():
    archivo = open(ARCHIVO_TEXTO, 'r')
    texto = archivo.read()
    archivo.close()
    palabras = texto.split()
    unicas = sorted(set(palabras))
    archivo_salida = open('ejercicios/ejercicio5/palabras_unicas.txt', 'w')
    for palabra in unicas:
        archivo_salida.write(palabra + '\n')
    archivo_salida.close()

# ejecuta escritura de nota
escribir_nota('primera nota')
# ejecuta escritura de nota
escribir_nota('segunda nota')
# ejecuta lectura de archivo
notas_texto = leer_notas()
print('contenido del archivo texto:', notas_texto)
# guarda lista en archivo binario
guardar_binario(['nota 1', 'nota 2'])
# carga archivo binario
datos_binarios = cargar_binario()
print('contenido del archivo binario:', datos_binarios)
# muestra atributos del archivo
mostrar_atributos()
# genera archivo con palabras unicas
listar_palabras_unicas()
