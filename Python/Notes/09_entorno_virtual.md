# Entorno Virtual

En vez de tener una versión de Python global en nuestro ordenador, que será la encargada de ejecutar cada uno de nuestros proyectos,
"creamos" un python aislado para cada proyecto, con la finalidad de poder decidir si actualizamos o no sus módulos para evitar
que el código rompa.

### Crear entorno virtual
```bash
python3 -m venv <nombre_del_entorno>
```

### Activar entorno virtual
```bash
source venv/bin/activate
```

### Desactivar entorno virtual
```bash
deactivate
```

### Crear alias en linux/mac para activar
Agregar al fichero ~/.bashrc:
```bash
# Activate python virtual environment
alias activatevenv='source venv/bin/activate'
```