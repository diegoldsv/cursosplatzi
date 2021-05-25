# Estructuras de Control

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