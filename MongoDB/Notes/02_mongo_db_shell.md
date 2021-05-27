# Mongo DB Shell

Lista de comandos para conectarse y operar los clusters de Mongo desde una terminal

**Clusters**
```bash
#Conectarse a un Cluster
mongo <CLUSTER_URL> --username <USER_NAME>
```

**BBDDs**
```bash
#Mostrar BBDDs
show dbs
#Mostrar BBDD actual
db
#Cambiar a otra BBDD (Si no existe la crea)
use <nombre_bbdd>
#Mostrar Colecciones de la BBDD actual
show collections
```

**CRUD**
```bash
#CREATE

#   Un elemento -> db.<nombre_coleccion>.insertOne( <documento> )
db.prueba.insertOne( { name: "Documento de Prueba 1" } )

#   Varios elementos -> db.<nombre_coleccion>.insertMany( [<documento1>, <documento2>] )
db.prueba.insertMany( [ { name: "Documento de Prueba 2" },  { name: "Documento de Prueba 3" } ] )

#READ

#   Primer elemento -> db.<nombre_coleccion>.findOne()
db.prueba.findOne()

#   Elementos que cumplan condiciones -> db.<nombre_coleccion>.find(<documento_de_condiciones>)
db.prueba.find( {name: "Documento de Prueba 2" })

#   Funciones
#   - pretty(): Devuelve los documentos con un formato legible

#UPDATE

#   Un elemento -> db.<nombre_coleccion>.updateOne(<documento_de_condiciones>, <documento_de_modificaciones>)
db.prueba.updateOne({name: "Documento de Prueba 1"}, {$set: {number: 100}})
db.prueba.updateOne({name: "Documento de Prueba 2"}, {$set: {number: 200}})
db.prueba.updateOne({name: "Documento de Prueba 3"}, {$set: {number: 300}})

#   Varios elementos -> db.<nombre_coleccion>.update(<documento_de_condiciones>, <documento_de_modificaciones>)
db.prueba.updateMany({number: {$gte: 200}}, {$set: {number: 100}})

#DELETE

#   Un elemento -> db.<nombre_coleccion>.deleteOne(<documento_de_condiciones>)
db.prueba.deleteOne({name: "Documento de Prueba 3"})

#   Varios elementos -> db.<nombre_coleccion>.deleteMany(<documento_de_condiciones>)
db.prueba.deleteMany({number: 100})
```