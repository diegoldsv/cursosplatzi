# Mongo DB

BBDD no relacional basada en documentos.

## Características

* Estructura de documentos tipo JSON (BSON).
* Es una BBDD distribuída (varios servidores).   
Esto implica que se pueda hacer un Escalado Horizontal (añadir servidores) y no solo Escalado Vertical (añadir RAM, procesador, disco duro)
* Schema less.   
Los documentos almacenados en la misma colección pueden tener distinta estructura.
* Lenguage de queries muy expresivo (similar a código Javascript).

## Ecosistema 

* MongoDB Server: Donde se alojan los datos.   
*Versiones: Community, Enterprise, Atlas(Cloud)*   
*Opciones de MongoDB como servicio: Atlas, mLab, MONGO CLUSTERS, ScaleGrid*
* MongoDB Shell: Terminal para interactuar con el servidor.
* MongoDB Compass: Interfaz gráfica para lanzar queries.
* Conectores: Librerías dentro del proyecto para comunicarnos con MongoDB.

### Otros

* MongoDB Mobile: Herramienta para lanzar queries desde el móvil.
* Stitch: Funciones para aplicar lógica serverless en la BBDD.
* MongoDB Charts: Conector para BI.

#### MongoDB Atlas

* Aprovisionamiento automático de clusters con MongoDB
* Alta disponibilidad y escalibilidad
* Seguro
* Disponible en AWS, GCP, Azure
* Fácil monitoreo y optimización