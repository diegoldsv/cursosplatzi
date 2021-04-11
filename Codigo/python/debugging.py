def get_divisors(num):    
    divisors = []
    try:
        if(num < 0):
            raise ValueError("Debes ingresar un número entero positivo")
        for i in range(1, num + 1):
            # Para buscar errores en la lógica del programa, usar el debugger.
            # Situar el breakpoint en la siguiente línea:
            # if num % i == 1:
            # Error corregido:
            if num % i == 0:
                divisors.append(i)
    except ValueError as error_message:
        print(error_message)
        # Para que el assert falle:
        # divisors = False
    return divisors

def run():
    try:
        num = int(input("Ingresa un numero: "))
        divisors = get_divisors(num)
        # [Test] divisors debe ser una lista
        assert type(divisors) is list, "divisors no es una lista"
        print(divisors)
    except ValueError:
        print("Debes ingresar un número entero")


if __name__ == '__main__':
    run()