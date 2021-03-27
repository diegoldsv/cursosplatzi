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
* Si el identificador contiene varias palabras, separarlos por guion bajo.

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
* + -> Significa concatenación
```python
"a" + "b" # Resultado: "ab"
```
* * -> Significa repetición
```python
"a" * 4 # Resultado: "aaaa"
```

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
- Raiz: ** número decimal o importando la libreria **math**

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

### Do While


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