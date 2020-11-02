menu = """
Bienvenido al conversor de monedas 💵

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes? ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos = input("¿Cuántos pesos argentinos tienes? ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos = input("¿Cuántos pesos mexicanos tienes? ")
    pesos = float(pesos)
    valor_dolar = 21
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print("Ingresa una opción correcta")


# pesos = input("¿Cuántos pesos mexicanos tienes? ")
# pesos = float(pesos)
# valor_dolar = 20.94
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + " dólares")

# dolares2 = input("¿Cuántos dolares tienes? ")
# dolares2 = float(dolares2)
# valor_peso = 0.05
# pesos2 = dolares2 / valor_peso
# pesos2 = round(pesos2, 2)
# pesos2 = str(pesos2)
# print("Tienes $" + pesos2 + " pesos")
