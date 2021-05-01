def es_primo(numero):
    for i in range(1,numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            return False
    return True

def run():
    numero = int(input("Escribe un número entero: "))
    if es_primo(numero):
        print(str(numero) + " es un número primo.")
    else:
        print(str(numero) + " no es un número primo.")

if __name__ == '__main__':
    run()