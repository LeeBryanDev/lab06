# huerto_inteligente.py
# guarda y carga datos de huerto en archivo
# usa open en modo w para guardar y r para cargar datos

ARCHIVO_HUERTO = 'ejercicios/ejercicio4/huerto.txt'

# guarda datos del huerto en archivo
# guarda datos del huerto
def guardar_datos(planta, temperatura, humedad, luz):
    archivo_guardado = open(ARCHIVO_HUERTO, 'w')
    archivo_guardado.write(planta + '\n')
    archivo_guardado.write(str(temperatura) + '\n')
    archivo_guardado.write(str(humedad) + '\n')
    archivo_guardado.write(str(luz) + '\n')
    archivo_guardado.close()

# carga datos del archivo del huerto
def cargar_datos():
    datos = []
    try:
        archivo_cargado = open(ARCHIVO_HUERTO, 'r')
        for linea in archivo_cargado:
            datos.append(linea.strip())
        archivo_cargado.close()
    except:
        datos = []
    return datos

# guarda datos del huerto
guardar_datos('tomate', '22', '60', 'true')
# carga datos guardados
datos_huerto = cargar_datos()
# muestra planta cargada
if datos_huerto:
    print('planta:', datos_huerto[0])
else:
    print('planta:', 'ninguna')
