const API_URL = 'https://swapi.co/api/';
const PERSONA = API_URL + 'people/:id/';

console.log("Hacemos la peticion");
const url = PERSONA.replace(':id',1);
const opts = {crossDomain:true};
const onResponse = function (data){
   console.log("Peticion Recibida");
   console.log(data);
}

$.get(url, opts, onResponse);