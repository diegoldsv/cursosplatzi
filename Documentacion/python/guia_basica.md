# Guia Basica de Python

## Variables

Caja o lugar donde puedo guardar objetos.

Ejemplo:
```python
caja = 10
print(caja) # Imprime: 10
```

Reglas:
* El identificador de la variable debe empezar con minúsculas.
* El identificador no puede empezar con números.
* Si el identificador contiene varias palabras, separarlas por guion bajo.

## Constantes 

Similar a las variables pero no cambian nunca su valor.   
Reglas:
* Identificador todo en mayúsculas.
* Nunca debe ser reasignado su valor.

## Tipo de Datos Primitivos

* Números enteros
* Números de punto flotante.
* Texto (cadenas de caracteres)
* Booleanos (verdadero y falso)

### Strings (Texto)

Para definirlas podemos usar comillas dobles o simples.   
Operadores:
* \+ -> Significa concatenación
```python
"a" + "b" # Resultado: "ab"
```
* \* -> Significa repetición
```python
"a" * 4 # Resultado: "aaaa"
```

Son **inmutables**. No pueden cambiar durante la ejecución.

### Booleanos

True o False

### Convertir datos de un tipo a otro

* String a Número: int("1")
* Número decimal a Número entero: int(4.5)
* Número a String: str(1)

## Operadores Aritméticos

- Suma: +
- Resta: -
- Multiplicación: *
- División: /
- Divison Entera: //
- Resto o Módulo: %
- Potencia: **
- Raiz: ** número decimal

## Operadores Lógicos

* Conjunción: and
* Disyunción: or
* Negación: not

## Operadores de Comparación

* Igualdad: ==
* No Igualdad: !=
* Mayor que: >
* Menos que: <
* Mayor o igual que: >=
* Menor o igual que: <=

## Condicionales

Sirven para modificar el flujo de la ejecución.

```python
if edad >= 18:
    print("Es mayor de edad")
elif edad == 17:
    print("El próximo año será mayor de edad")
else:
    print("Es menor de edad")
```

## Funciones

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

### Funciones de Input / Output

* Función para obtener datos -> input()
* Función para mostrar datos -> print()

### Funciones de String

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

## Bucles

Bloque de código que se repite siguiendo unas condiciones.

### While

El código se ejecuta **mientras** se cumple una condición:
```python
# Contar hasta 10
numero_actual = 0
while numero_actual <= 10:
    print(str(numero_actual))
    numero_actual = numero_actual + 1
```

### For

Para una variable, el código se ejecuta **mientras** el valor de la variable se encuentra en un grupo de valores.
```python
# Contar hasta 10
for numero_actual in range(11):
    print(str(numero_actual))

# Imprimir las letras de un nombre
for letra in "Diego":
    print(letra)
```

### Modificando el flujo de ejecución de los ciclos

Se puede modificar el flujo de ejecución con las siguientes palabras claves:
* break: Interrumpir un ciclo.
* continue: Ir a la siguiente iteración de un ciclo.

## Estructuras de Datos

### Listas

Grupo de valores almacenados en una variable.   

* Los datos pueden ser de diferentes tipos.
* Para trabajar sobre ellas, al igual que con los Strings, usamos índices y funciones propias de las listas.
* Son dinámicas, pueden variar durante la ejecución del programa.

```python
lista_de_numeros = [1, 2, 3, 4]
persona = ["Diego", 23, "Venezuela"]

# Acceder a un elemento de la lista
print(persona[0]) # Resultado: Diego

# Agregar/Eliminar elementos
lista_de_numeros.append(1) # Resultado: [1, 2, 3, 4, 1]
lista_de_numeros.pop(1) # Resultado: [1, 3, 4, 5]

# Suma de listas
lista_de_numeros + persona # Resultado: [1, 3, 4, 5, 'Diego', 23, 'Venezuela']
```

### Tuplas

Grupo de valores almacenados en una variable.

* Los datos pueden ser de diferentes tipos.
* Son inmutables, **no** pueden variar durante la ejecución del programa.

### Diccionarios

Grupo de llaves y valores almacenados en una variable.

* Las llaves son los identificadores de cada valor.
* Usamos las llaves para acceder a los valores.

```python
persona = {
    "Nombre": "Diego",
    "Edad": 23,
    "Pais": "Venezuela"
}

# Acceder a los valores del diccionario
print("Información de la persona:")
print("Nombre: " + persona["Nombre"])
print("Edad: " + str(persona["Edad"]))
print("Pais: " + persona["Pais"])

# Recorrer las llaves de un diccionario
for informacion in persona.keys():
    print(informacion)

# Recorrer los valores de un diccionario
for datos in persona.values():
    print(datos)

# Recorrer los items de un diccionario
for informacion, dato in persona.items():
    if type(dato) is int:
        dato = str(dato)
    print(informacion + ": " + dato)
```
## Importar Módulos

Existen librerías (grupos de funciones ya escritas) que podemos utilizar en nuestro código.   
Para ello, debemos importarlas al inicio del código:
```python
import random

print("Número aleatorio del 1 al 100: " + str(random.randint(1,100)))
```
## Buenas Prácticas

* Almacenar el código principal del programa en una función run() o main().
* Entre cada función dejar dos saltos de línea.
* Definir el punto de entrada de cada programa.

Ejemplo:
```python
def funcion1():
    pass


# Entre estas funciones hay dos saltos de línea
# El código principal se almacena en la función run().
def run():
    print("Código principal")


# Punto de Entrada
if __name__ == '__main__':
    run()
```