# calculadora.py
# guarda ultimas diez operaciones en archivo
# usa open en modo r y w, guarda en archivo de texto

ARCHIVO_OPERACIONES = 'ejercicios/ejercicio3/operaciones.txt'

# pide operacion y numeros al usuario
def pedir_operacion():
    print('opciones disponibles: suma, resta, multiplicacion, division')
    tipo = input('operacion a realizar: ')
    primer_valor = float(input('primer numero: '))
    segundo_valor = float(input('segundo numero: '))
    if tipo == 'suma':
        resultado = primer_valor + segundo_valor
    elif tipo == 'resta':
        resultado = primer_valor - segundo_valor
    elif tipo == 'multiplicacion':
        resultado = primer_valor * segundo_valor
    elif tipo == 'division':
        if segundo_valor == 0:
            resultado = 0
        else:
            resultado = primer_valor / segundo_valor
    else:
        resultado = 0
    return primer_valor, segundo_valor, tipo, resultado

# carga registros previos del archivo
def cargar_registros():
    registros = []
    try:
        archivo_registro = open(ARCHIVO_OPERACIONES, 'r')
        for linea in archivo_registro:
            linea_limpia = linea.strip()
            if linea_limpia != '':
                registros.append(linea_limpia)
        archivo_registro.close()
    except:
        registros = []
    return registros

# guarda registro manteniendo maximo diez
def guardar_registro(primer, segundo, tipo, resultado):
    registros = cargar_registros()
    nuevo_registro = str(primer) + ',' + str(segundo) + ',' + tipo + ',' + str(resultado)
    registros.append(nuevo_registro)
    if len(registros) > 10:
        registros = registros[-10:]
    archivo_registro = open(ARCHIVO_OPERACIONES, 'w')
    for registro in registros:
        archivo_registro.write(registro + '\n')
    archivo_registro.close()

# ejecuta operacion y guarda registro
primer, segundo, tipo_op, resultado_op = pedir_operacion()
# guarda resultado en archivo
guardar_registro(primer, segundo, tipo_op, resultado_op)
print('resultado:', resultado_op)
