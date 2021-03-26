const API_URL = 'https://swapi.co/api/';
const PERSONA = API_URL + 'people/:id/';
const opts = {crossDomain:true};

//Se usará el mismo ejemplo del callback.js para ver las diferencias
//
//Promesas: Inician en Pending y luego se resuelven en fullfiled o rejected
//
//DEFINICION:
// Se usa: Resolve para indicar donde se ejecuta el .then() / Reject para indicar donde se ejecuta el .catch()
function obtenerPersonaje(id){
    return new Promise((resolve,reject)=>{
        $
        .get(PERSONA.replace(':id',id),opts, data => resolve(data))
        .fail(()=> reject(id));
    });
}
//EJECUCION:
//Se usa then() para llamar a la funcion que se ejecutara en caso de success
//Se usa catch() para llamar a la funcion en caso de fallo
const imprimir = data => data.forEach(e => console.log(e.name));
const error = id => console.log(`El id: ${id} no se encuentra`);

//obtenerPersonaje(1).then(imprimir).catch(error);
//obtenerPersonaje(502).then(imprimir).catch(error);

//Para hacerlas encadenadas
/*obtenerPersonaje(1)
    .then(personaje => {
     return obtenerPersonaje(2)
    })
    .then()
    ...
    ...
    ...
    .catch()
*/

//PROMESAS EN PARALELO
const ids = [1, 2, 3, 4, 5, 6];
let promesas = ids.map(id => obtenerPersonaje(id));
Promise
    .all(promesas)
    .then(imprimir)
    .catch(error);


//Async Await -- Hacemos lo mismo que arriba
async function prueba(){
    try{
      var data = await Promise.all(promesas);  
      imprimir(data);
    }catch(id){
       error(id); 
    }
}