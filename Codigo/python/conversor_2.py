menu = """
Bienvenido al conversor de monedas

1 - Euro a Dolar
2 - Dolar a Euro

Elige una opción: """

opcion = int(input(menu))
if opcion == 1:
    euros = input("¿Cuántos euros tienes?: ")
    euros = float(euros)
    valor_dolar = 0.8
    dolares = euros / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    dolares = input("¿Cuántos dolares tienes?: ")
    dolares = float(dolares)
    valor_euro = 1.2
    euros = dolares / valor_euro
    euros = round(euros, 2)
    euros = str(euros)
    print("Tienes " + euros + "€ euros")