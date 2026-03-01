# -*- coding: utf-8 -*-
"""
@author: Luis Tomás Pichucho Molina 
"""

import random

# Funciones

def mostrar_reglas():
    print("\n=== REGLAS ===")
    print("🪨 Piedra aplasta a Tijera")
    print("✂ Tijera corta a Papel")
    print("📄 Papel envuelve a Piedra")
    print("👉 Si ambos jugadores eligen lo mismo la ronda termina en empate.")
    print("👉 El ganador se decide comparando las elecciones del jugador y la computadora.\n")

def convertir_eleccion(numero):
    if numero == "1":
        return "piedra"
    elif numero == "2":
        return "papel"
    elif numero == "3":
        return "tijera"
    else:
        return None

def determinar_resultado(jugador, bot):
    if jugador == bot:
        return "empate"
    elif (jugador == "piedra" and bot == "tijera") or \
         (jugador == "tijera" and bot == "papel") or \
         (jugador == "papel" and bot == "piedra"):
        return "ganada"
    else:
        return "perdida"

#Programa principal

print("=== YAN-KEN-PO ===")
nombre = input("Ingrese su nombre: ")
print("Escriba 'Si' para jugar")
jugar = input("Jugar: ")

if jugar.lower() == "si":
    print("\n1. Jugar contra un bot")
    print("2. Salir del juego")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_reglas()
        opciones = ["piedra", "papel", "tijera"]
#Tupla de contadores: (ganadas, perdidas, empates)   
        contadores = (0, 0, 0)

        while True:
            print("\n1 = Piedra")
            print("2 = Papel")
            print("3 = Tijera")
            print("4 = Salir del juego")
            eleccion = input("Escoge una opción: ")

            if eleccion == "4":
                print("\n=== RESULTADOS FINALES ===")
                print("Ganadas:", contadores[0])
                print("Perdidas:", contadores[1])
                print("Empates:", contadores[2])
                print("Gracias por jugar,", nombre)
                break
            jugador = convertir_eleccion(eleccion)

            if jugador is None:
                print("Opción no válida")
                continue
            
            bot = random.choice(opciones)
            print(f"\n{nombre} eligió: {jugador}")
            print(f"El bot eligió: {bot}")
            resultado = determinar_resultado(jugador, bot)

# Convertimos la tupla en lista para modificar valores

            lista = list(contadores)

            if resultado == "empate":
                print("Resultado: Empate")
                lista[2] += 1
            elif resultado == "ganada":
                print("Resultado: ¡Ganaste!")
                lista[0] += 1
            else:
                print("Resultado: Perdiste")
                lista[1] += 1

            contadores = tuple(lista)

    elif opcion == "2":
        print("Gracias por jugar.")

    else:
        print("Opción no válida")

else:
    print("Empiece de nuevo.")