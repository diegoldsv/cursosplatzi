# Conceptos

## Base de datos

* Contenedor físico de colecciones.
* Cada base de datos tiene su archivo propio en el sistema de archivos.
* Un cluster puede tener múltiples bases de datos.

## Colecciones

* Agrupación de documentos.
* Equivalente a una tabla en las bases de datos relacionales.
* No impone un esquema.

## Documentos

* Un registro dentro de una colección.
* Es análogo a un objeto JSON (BSON).   
*BSON: codificación binaria de documentos JSON. Permite más tipos de datos. Los drivers usados en cada lenguaje se encargan de estas transformaciones JSON / BSON*
* La unidad básica dentro de MongoDB.

## Analogía SQL / MongoDB

database <-> database
tables <-> collections
rows <-> documents
columns <-> fields