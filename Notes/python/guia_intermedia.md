# Guia intermedia de Python

## El Zen de Python

Principios básicos para programar en el lenguaje.   
Para leerlo, abrir en la terminal el interprete de python, y escribir:
```python
>>> import this

# Output:
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
```

## Documentación

Documentación oficial: [Python 3.9.4 documentation](https://docs.python.org/3/).   
Secciones importantes:
* Tutorial -> Guía básica del lenguaje.
* Library Reference -> Explicación de implementación de métodos.
* Language Reference -> Explicación de elementos del lenguaje y sintaxis.
* PEP Index (Python Enhancement Proposals) -> Guías de buenas prácticas.

## Entorno Virtual

En vez de tener una versión de Python global en nuestro ordenador, que será la encargada de ejecutar cada uno de nuestros proyectos,
"creamos" un python aislado para cada proyecto, con la finalidad de poder decidir si actualizamos o no sus módulos para evitar
que el código rompa.

#### Crear entorno virtual
```bash
python3 -m venv <nombre_del_entorno>
```

#### Activar entorno virtual
```bash
source venv/bin/activate
```

#### Desactivar entorno virtual
```bash
deactivate
```

#### Crear alias en linux/mac para activar
Agregar al fichero ~/.bashrc:
```bash
# Activate python virtual environment
alias activatevenv='source venv/bin/activate'
```

## pip (Package Installer for Python)

Gestor de dependencias de python. (El npm de python)

#### Módulos populares
* Requests
* BeautifulSoup4
* Pandas
* Numpy
* Pytest

#### Instalar módulos
```bash
pip install pandas
```

#### Compartir dependencias
```bash
# Guardar dependencias
pip freeze > requirements.txt

# Instalar dependencias
pip install -r requirements.txt
```

#### Otros gestores de dependencias

* pyenv
* pipenv
* [anaconda](https://www.anaconda.com/products/individual): 
Especial para ciencia de datos. No es solo un gestor de dependencias.
También permite crear entornos virtuales. Además de python puede usar R.

## Comprehensions

Métodos concisos para crear estructura de datos.
#### List Comprehensions

```python
# [<element> for <element> in <iterable> if <condition>]
example = [ i**2 for i in range(1,101) if i % 3 != 0]

# Múltiplos de 4, 6 y 9, hasta 5 dígitos
my_list = [ i for i in range (1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
```

#### Dict Comprehensions

```python
# {<key>:<value> for <value> in <iterable> if <condition>}
example = {i: i**2 for i in range(1,101) if i % 3 != 0}

# Raiz cuadrada de múltiplos de 4, 6 y 9, hasta 5 dígitos
my_dict = {i: i**0.5 for i in range (1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 }
```

## Funciones Anónimas (lambda)

* Solo permiten una línea de código.
* Se retorna el valor de la expresión.
* Sintáxis:
```python
lambda argumentos: expresión

#Ejemplo palindrome
palindrome = lambda string: string == string[::-1]
```

## High order functions

Es una función que recibe como parámetro a otra función.   
Ejemplo:
```python
def saludo(func):
    func()

def hola():
    print("Hola!!")

def adios():
    print("Adios!!")

saludo(hola)    # Output: Hola!!
saludo(adios)   # Output: Adios!!
```

#### Filter

Aplicar un filtro a todos los elementos de un iterable.
Ejemplo:
```python
my_list = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda x: x%2 == 0, my_list))
print(even)
```
#### Map

Aplicar una operación a todos los elementos de un iterable.
Ejemplo:
```python
my_list = [1,2,3,4,5,6,7,8,9]

squares = list(map(lambda x: x**2, my_list))
print(squares)
```

#### Reduce

Aplicar una operación con todos los elementos de un iterable para obtener un resultado.
Ejemplo:
```python
from functools import reduce

my_list = [1,2,3]

factorial = reduce(lambda x, y: x * y, my_list)
print(factorial)
```

## Errores en Python

Dos tipos:
* SyntaxError
* Exception

#### SyntaxError

Errores en la sintaxis. En estos casos no se ejecuta ninguna línea del programa.

#### Exception

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

## Manejo de ficheros

#### Modos de apertura

* R -> Lectura
* W -> Escritura (sobreescribir)
* A -> Escritura (agregar al final)

#### Abrir ficheros

```python
# WITH: En python se denomina como un “manejador contextual”. Controla el flujo del archivo y se asegura que el archivo no se rompa.
with open("ruta/del/archivo.txt", "r") as f:
```

#### Leer ficheros

```python
with open("ruta/del/archivo.txt", "r") as f:
    for line in f:
        print(line)
```

#### Escribir ficheros

```python
with open("ruta/del/archivo.txt", "w", encoding="utf-8") as f:
    f.write("Hola!! \n")
    f.write("Adiós!! \n")
```