# Estructuras de Datos

## Listas

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

## Tuplas

Grupo de valores almacenados en una variable.

* Los datos pueden ser de diferentes tipos.
* Son inmutables, **no** pueden variar durante la ejecución del programa.
* Es recomendable su uso para casos donde sabemos que no vamos a modificar el grupo de valores que queremos definir debido a la eficiencia de las tuplas.

```python
tupla_de_numeros = (1, 2, 3, 4)
```

## Diccionarios

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