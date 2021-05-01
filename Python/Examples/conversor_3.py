def convertir_moneda(cantidad, equivalencia):
    valor_convertido = cantidad / equivalencia
    return round(valor_convertido, 2)


def solicitar_moneda(nombre_moneda):
    moneda = input("¿Cuántos " + nombre_moneda + " tienes?: ")
    return float(moneda)


def mostrar_moneda(cantidad, nombre_moneda):
    cantidad = str(cantidad)
    print("Tienes " + cantidad + " " + nombre_moneda)


menu = """
Bienvenido al conversor de monedas

1 - Euro a Dolar
2 - Dolar a Euro

Elige una opción: """

opcion = int(input(menu))
if opcion == 1:
    euros = solicitar_moneda("euros")
    dolares = convertir_moneda(euros, 0.8)
    mostrar_moneda(dolares, "dólares")
elif opcion == 2:
    dolares = solicitar_moneda("dólares")
    euros = convertir_moneda(dolares, 1.2)   
    mostrar_moneda(euros, "euros")