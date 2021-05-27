# Modelo de Datos

La estructura de una bbbdd en Mongo se puede separar en esquemas y relaciones

## Esquemas

Estructura de los documentos que son parte de una colección.   
Mongo no impone un esquema, incluso se puede tener colecciones con documentos que no tengan ningún parecido en su estructura. (Mala práctica)

## Relaciones

En MongoDB hay dos formas de establecer relaciones:
* Documentos Embebidos
* Referencia a otros Documentos

Para plantear el modelo se recomienda pensar en lo siguiente:
* ¿Las entidades "Ns" de una relación 1 a N, necesitarán ser entidades separadas o siempre accederemos a ellas a través de la entidad "1"?
* ¿Cuál es la cardinalidad de la relación 1 a N, uno a pocos, uno a muchos o uno a millones?

En función de esto, seleccionar:
| Situación | Decisión |
| --------- | -------- |
| La cardinalidad es **uno a pocos** y **no hay necesidad de acceder directamente** a las entidades "Ns" | Entidad **1** tiene un Arreglo de **Ns** Documentos Embebidos |
| La cardinalidad es **uno a muchos** o **hay necesidad de acceder directamente** a las entidades "Ns" | Entidad **1** tiene un Arreglos de **Ns** Referencias a otros Documentos |
| La cardinaidad es **uno a millones** | Referencia de Entidades **Ns** a Entidad **1** |

## Lecturas Recomendadas

* [Data Modeling Introduction](https://docs.mongodb.com/manual/core/data-modeling-introduction/)
* [6 Rules of Thumb for MongoDB Schema Design: Part 1](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1)
* [6 Rules of Thumb for MongoDB Schema Design: Part 2](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-2)
* [6 Rules of Thumb for MongoDB Schema Design: Part 3](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-3)