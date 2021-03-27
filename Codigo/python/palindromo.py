def run():
    palabra = input("Introduce una palabra: ")
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        print("Es una palabra palíndromo")
    else:
        print("No es una palabra palíndromo")

if __name__ == '__main__':
    run()