# archivo_prueba.py
# manejo basico de archivos de texto con open y modos
# crea archivo con open en modo w, escribe con write, anexa con modo a, divide lineas con split

# crea archivo en modo escritura
def crear_archivo():
    archivo = open('actividades/actividad1/archivoPrueba.txt', 'w')
    archivo.close()

# escribe texto con write
def escribir_texto():
    archivo = open('actividades/actividad1/archivoPrueba.txt', 'w')
    archivo.write('Era el mejor de los tiempos y era el peor de los tiempos')
    archivo.write(' la edad de la sabiduria y tambien de la locura;')
    archivo.close()

# anexa texto con modo a
def anexar_texto():
    archivo = open('actividades/actividad1/archivoPrueba.txt', 'a')
    archivo.write(' la epoca de las creencias y de la incredulidad;')
    archivo.write(' la era de la luz y de las tinieblas')
    archivo.write(' la primavera de la esperanza y el invierno de la desesperacion.')
    archivo.close()

# divide lineas con split
def dividir_lineas():
    archivo_lectura = open('actividades/actividad1/archivoPrueba.txt', 'r')
    texto_completo = archivo_lectura.read()
    archivo_lectura.close()
    partes_separadas = texto_completo.split(';')
    archivo_escritura = open('actividades/actividad1/archivoPrueba.txt', 'w')
    for parte in partes_separadas:
        texto_limpio = parte.strip()
        archivo_escritura.write(texto_limpio + '\n')
    archivo_escritura.close()

# ejecuta paso de creacion
crear_archivo()
# ejecuta paso de escritura
escribir_texto()
# ejecuta paso de anexo
anexar_texto()
# ejecuta paso de division
dividir_lineas()
