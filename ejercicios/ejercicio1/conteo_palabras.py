# conteo_palabras.py
# cuenta palabras de tres archivos y ordena por repeticion

# cuenta palabras y ordena por repeticion
def contar_y_ordenar():
    archivos = ['ejercicios/ejercicio1/texto1.txt', 'ejercicios/ejercicio1/texto2.txt', 'ejercicios/ejercicio1/texto3.txt']
    todas_las_palabras = []
    for nombre in archivos:
        try:
            archivo = open(nombre, 'r')
            texto = archivo.read()
            archivo.close()
            palabras = texto.split()
            todas_las_palabras.extend(palabras)
        except:
            pass
    conteo_palabras = {}
    for palabra in todas_las_palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] = conteo_palabras[palabra] + 1
        else:
            conteo_palabras[palabra] = 1
    lista_ordenada = sorted(conteo_palabras.items(), key=lambda item: item[1], reverse=True)
    archivo_salida = open('ejercicios/ejercicio1/resultado_palabras.txt', 'w')
    for palabra, cantidad in lista_ordenada:
        archivo_salida.write(palabra + ' ' + str(cantidad) + '\n')
    archivo_salida.close()

# ejecuta conteo y orden
contar_y_ordenar()
