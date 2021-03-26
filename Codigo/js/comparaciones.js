//Comparaciones VALORES PRIMITIVOS
console.log('Primitivos doble','4'==4); //True
console.log('Primitivos triple','4'===4); //False

//Comparaciones Objetos (REFERENCIAS)
var object = {
    nombre: "Diego"
};

var object2 = {
    nombre: "Diego"
};

console.log('Objetos distintos doble',object == object2); //False
console.log('Objetos distintos triple',object === object2); //False
object2 = object;
console.log('Objetos iguales doble',object == object2); //True
console.log('Objetos iguales triple',object === object2); //True

//RETO
function imprimirSiEsMayorDeEdad({nombre, edad}){
    if(edad >= 18) console.log(`${nombre} es mayor de edad`);
    else console.log(`${nombre} es menor de edad`);
}