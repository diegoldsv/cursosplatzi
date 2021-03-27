euros = input("¿Cuántos euros tienes?: ")
euros = float(euros)
valor_euro_dolar = 1.18
dolares = euros / valor_euro_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")