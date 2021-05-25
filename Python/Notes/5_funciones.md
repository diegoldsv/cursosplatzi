# Funciones

Bloques de código para reutilizar.  
* Pueden tener valores de entrada -> Parámetros.
* Pueden tener valor de salida -> Valor a retornar.

```python
def nombre_de_la_funcion():
    paso1
    paso2
    ...
    pasoN

# Ejemplo
def suma_de_dos_numeros(numero1, numero2):
    return numero1 + numero2
```

## Funciones más utilizadas

## Funciones de Input / Output

* Función para obtener datos -> input()
* Función para mostrar datos -> print()

## Funciones de String

* upper(): Convierte todas las letras a mayúsculas.
* capitalize(): Convierte las primeras letras de cada palabra a mayúsculas.
* strip(): Eliminamos carácteres basura al inicio/final de un texto.
* lower(): Convierte todas las letras a minúsculas
* replace(texto_a_reemplazar, texto_nuevo): Reemplaza un texto por otro.

Para acceder a cada posición de un string usamos índices:
```python
nombre = "Diego"
print(nombre[2]) # Resultado: e
```

Para dividir un string (slice) usamos rangos:
```python
nombre = "Diego"
print(nombre[0:2]) # Resultado: Di
print(nombre[:3]) # Resultado: Die
print(nombre[3:]) # Resultado: go
# Conseguir slices de pasos de N en N
print(nombre[:4:2]) # Resultado: De (Pasos de 2 en 2)
print(nombre[::2]) # Resultado: Deo (Pasos de 2 en 2)
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