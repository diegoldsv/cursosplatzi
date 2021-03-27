import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_ingresado = input("Elige un número del 1 al 100: ")
    numero_ingresado = int(numero_ingresado)
    while numero_ingresado != numero_aleatorio:
        if numero_ingresado < numero_aleatorio:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        numero_ingresado = input("Elige otro número: ")
        numero_ingresado = int(numero_ingresado)
    print("Ganaste!")

if __name__ == "__main__":
    run()