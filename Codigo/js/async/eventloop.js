/*
Todas las tareas se colocan en la pila de ejecución

* Ejemplo sincrono

Pila de ejecucion:
- Tarea 1
- Tarea 2
- Tarea 3
    ....
- Tarea N

Cuando una tarea necesita esperar a alguien se delega y cuando termina se pone en
la cola de tareas

* Ejemplo asinc

Pila de Ejecucion:       Cola de Tareas:
- Tarea 1
- Tarea 2
- Tarea 3 (callback) //Se envia la solicitud
- Tarea 4
- Tarea 5
                        - Callback //Viene la respuesta
- Tarea N
- Callback


Basicamente se ejecuta TODAS las tareas sincronas y luego se ejecutan las respuestas
que han llegado de las sincronas

Para entender JS ejecutar este ejemplo

   console.log('a')
    setTimeout(() => console.log('b'), 0)
    console.log('c')


*/ 