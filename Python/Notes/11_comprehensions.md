# Comprehensions

Métodos concisos para crear estructura de datos.
### List Comprehensions

```python
# [<element> for <element> in <iterable> if <condition>]
example = [ i**2 for i in range(1,101) if i % 3 != 0]

# Múltiplos de 4, 6 y 9, hasta 5 dígitos
my_list = [ i for i in range (1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
```

### Dict Comprehensions

```python
# {<key>:<value> for <value> in <iterable> if <condition>}
example = {i: i**2 for i in range(1,101) if i % 3 != 0}

# Raiz cuadrada de múltiplos de 4, 6 y 9, hasta 5 dígitos
my_dict = {i: i**0.5 for i in range (1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 }
```