# Errores en Python

Dos tipos:
* SyntaxError
* Exception

### SyntaxError

Errores en la sintaxis. En estos casos no se ejecuta ninguna línea del programa.

### Exception

Errores en tiempo de ejecución. El programa se ejecuta hasta que llega a la línea del error y se lanza la excepción.   
Alguna de ellas son:
* KeyboardInterrupt
* KeyError
* IndexError
* FileNotFoundError
* ZeroDivisionError
* ImportError

Palabras claves:
* try: Bloque de código a intentar a ejecutar.
* except: Acciones a ejecutar si se eleva una excepción.
* raise: Elevar una excepción.
* finally: Ejecutar una acción, ocurra un error o no.
Su uso común es para cerrar conexiones a BBDD o cerrar ficheros.

Ejemplo:
```python
# Caso donde salta una excepcion TypeError
def palindrome(string):
    return string == string[::-1]

try:
    print(palindrome(1))
except TypeError:
    print("Solo se pueden ingresar strings")

# Caso donde elevamos una excepcion nosotros mismos.
def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return string == string[::-1]
    except ValueError as error_message:
        print(error_message)
        return False

print(palindrome(""))
```

## Asserts Statements

Afirmaciones en python. Recomendadas para detectar errores del programador. Para errores del usuario, usar excepciones.

Sintaxis:
```python
assert expresion, error_message
# Ejemplo
assert natural_number in range(1,10), "natural_number no contiene un numero natural"
```