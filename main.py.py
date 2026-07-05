"""
Game Catalog - Version 1

A simple command-line application written in Python.

Features:
- Add games to a personal catalog.
- Store each game's status.
- Track playtime.
- Rate completed games.
- Search for games and display stored information.

This project was built as a learning exercise while studying Python.
Its main goal is to practice dictionaries, functions, loops,
input validation, and code organization.

The interface is currently available in Spanish because it was
developed for Spanish-speaking users.
"""
# Stores all games and their associated information.
catalogo = {}

# Ask the user for a valid game status.
def pedir_estado():

    while True:
        print("[P] Pendiente, [J] Jugando, [D] Dejado, [T] Terminado")
        estado = input("Estado del juego: ")

        if estado.lower() in ["p","pendiente"]:
            return "Pendiente"
        
        elif estado.lower() in ["j","jugando","en proceso"]:
            return "Jugando"

        elif estado.lower() in ["d","dejado","apartado"]:
            return "Dejado"
        
        elif estado.lower() in ["t","terminado","completo"]:
            return "Terminado"

        else:
            print("Comando Invalido, ingresa una de las opciones")


# Ask for the game's playtime if it has already been started.
def pedir_tiempo_jugado(estado_juego):

    if estado_juego in ["Dejado","Terminado"]:
        while True: 
            try:
                tiempo_juego = int(input("¿Cuantas horas tenes en el juego? "))
                return tiempo_juego
            except ValueError:                                              
                print("Comando Invalido, ingresa un numero")


# Ask for the game's rating if it has been completed.
def pedir_puntaje(estado_juego):

    if estado_juego == "Terminado":
        while True:
            try:
                puntaje = int(input("¿Que puntaje del 1 al 10 le darías? "))
                    
                if 1 <= puntaje <= 10:
                    return puntaje
                    
                else:
                    print("Ingresa un numero del 1 al 10")
            except ValueError:
                print("Comando Invalido, ingresa un numero")


# Returns a specific piece of game data.
def mostrar_dato(dato_juego):

    while True:
        print("[E] Estado, [T] Tiempo Jugado, [P] Puntaje")
        dato = input("¿Que dato del juego quieres ver? ")
        
        if dato.lower() in ["e", "estado"]:
            return dato_juego["Estado"]

        elif dato.lower() in ["t", "tiempo", "tiempo_jugado"]:
            if "Tiempo" in dato_juego:
                return dato_juego["Tiempo"]
            print("Ese juego todavia no tiene registrado su tiempo jugado")

        elif dato.lower() in ["p", "puntaje"]:
            if "Puntaje" in dato_juego:
                return dato_juego["Puntaje"]
            print("Ese juego todavia no tiene registrado su puntaje")

        else: 
            print("Comando Invalido, Ingresa un dato que exista")


# Adds a game to the catalog.
def agregar_juego():

    datos_juego = {}

    # Ask for the game's name.
    juego = input("¿Que juego quieres agregar a tu catalogo? ")
    
    if juego == "":
        print("Operacion Cancelada")
        return None, None

    estado_juego = pedir_estado()
    datos_juego["Estado"] = estado_juego

    tiempo_juego = pedir_tiempo_jugado(estado_juego)
        
    if tiempo_juego is not None:
        datos_juego["Tiempo"] = tiempo_juego

    puntaje = pedir_puntaje(estado_juego)

    if puntaje is not None:    
        datos_juego["Puntaje"] = puntaje

    return datos_juego, juego


# Search for a game in the catalog.
def buscar_juego(catalogo):

    juego = input("¿Que juego deseas buscar? ")

    if juego in catalogo:
        return juego, catalogo[juego]
    
    print(f"{juego} no esta en tu catalogo")

    # Keep the return values consistent.
    return None, None


# Main menu
def buscar_agregar(catalogo):

    print("[B] Buscar, [A] Agregar, [V] Volver")
    while True:
        accion = input("¿Que quieres hacer: Buscar un juego o Agregar un juego? ")

        if accion.lower() in ["b","buscar"]:
            juego, datos_juego = buscar_juego(catalogo)
            
            if juego is not None:
                dato = mostrar_dato(datos_juego)
                print(dato)

        elif accion.lower() in ["a","agregar"]:
            datos_juego, juego = agregar_juego()
                
            if juego is not None:     
                catalogo[juego] = datos_juego
            
        elif accion.lower() in ["v","volver"]:
            break

        else:
            print("Comando Invalido, Ingresa una de las opciones pedidas")


buscar_agregar(catalogo)
print(catalogo)
