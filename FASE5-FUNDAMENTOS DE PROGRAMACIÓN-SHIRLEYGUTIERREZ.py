# Estudiante: SHIRLEY
#FUNDAMENTOS DE PROGRAMACION
# Matriz de sesiones:
# [ID Cliente, Duración (segundos), Eventos Clics]

sesiones = [
    ["C001", 250, 12],
    ["C002", 45, 3],
    ["C003", 120, 7],
    ["C004", 300, 15],
    ["C005", 50, 2]
]

# Función para clasificar el nivel de compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 and clics < 8:
        return "Bajo"

    else:
        return "Medio"


# Generar informe
print(" INFORME DE COMPROMISO \n")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente)
    print("Clasificación:", clasificacion)
    print("-----------------------------")
