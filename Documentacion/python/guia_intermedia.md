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