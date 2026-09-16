print("=== ADIVINA EL NÚMERO ===")

print("Piensa en un número del 1 al 100.")
print("Yo intentaré adivinarlo.")

inicio = 1
fin = 100
intentos = 0

while inicio <= fin:
    propuesta = (inicio + fin) // 2
    intentos += 1

    print(f"\n¿Tu número es {propuesta}?")
    respuesta = input("Escribe 'mayor', 'menor' o 'correcto': ")

    if respuesta == "correcto":
        print(f"\n¡Adiviné tu número!")
        print(f"Número de intentos: {intentos}")
        break

    elif respuesta == "mayor":
        inicio = propuesta + 1

    elif respuesta == "menor":
        fin = propuesta - 1

    else:
        print("Respuesta no válida. Escribe mayor, menor o correcto.")