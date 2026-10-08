# usuario_csv.py
# clase usuario a partir de csv y guarda por tipo
# usa open en modo r para leer lineas, split por comas y sorted por nivel

# define clase usuario con campos del csv
class Usuario:
    def __init__(self, codigo, tipo, dinero, nivel, puntaje):
        self.codigo = codigo
        self.tipo = tipo
        self.dinero = int(dinero)
        self.nivel = int(nivel)
        self.puntaje = int(puntaje)

# carga datos del csv con split
def cargar_usuarios():
    usuarios = []
    archivo_csv = open('ejercicios/ejercicio2/datosusuario.csv', 'r')
    for linea in archivo_csv:
        datos = linea.strip().split(',')
        if len(datos) == 5:
            usuario = Usuario(
                datos[0].strip(),
                datos[1].strip(),
                datos[2].strip(),
                datos[3].strip(),
                datos[4].strip()
            )
            usuarios.append(usuario)
    archivo_csv.close()
    return usuarios

# guarda ordenado por nivel en archivo por tipo
def guardar_por_tipo(usuarios):
    grupos = {}
    for usuario in usuarios:
        tipo_personaje = usuario.tipo
        if tipo_personaje not in grupos:
            grupos[tipo_personaje] = []
        grupos[tipo_personaje].append(usuario)
    for tipo in grupos:
        ordenados = sorted(grupos[tipo], key=lambda u: u.nivel)
        archivo_tipo = open('ejercicios/ejercicio2/' + tipo + '.txt', 'w')
        for usuario in ordenados:
            archivo_tipo.write(
                str(usuario.codigo) + ',' +
                usuario.tipo + ',' +
                str(usuario.dinero) + ',' +
                str(usuario.nivel) + ',' +
                str(usuario.puntaje) + '\n'
            )
        archivo_tipo.close()

# carga los datos del archivo
datos_usuarios = cargar_usuarios()
# guarda grupos ordenados por tipo
guardar_por_tipo(datos_usuarios)
