# Manejo de ficheros

### Modos de apertura

* R -> Lectura
* W -> Escritura (sobreescribir)
* A -> Escritura (agregar al final)

### Abrir ficheros

```python
# WITH: En python se denomina como un “manejador contextual”. Controla el flujo del archivo y se asegura que el archivo no se rompa.
with open("ruta/del/archivo.txt", "r") as f:
```

### Leer ficheros

```python
with open("ruta/del/archivo.txt", "r") as f:
    for line in f:
        print(line)
```

### Escribir ficheros

```python
with open("ruta/del/archivo.txt", "w", encoding="utf-8") as f:
    f.write("Hola!! \n")
    f.write("Adiós!! \n")
```