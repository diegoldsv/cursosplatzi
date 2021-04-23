//Sintaxis Objetos
var Objeto = {
    nombre: "Diego",
    edad: 21
}

//FUNCIONES: SINTAXIS Y TIPOS

//Para ejecutar: funcionNormal()
function funcionNormal(){
    console.log("Se ejecutó una función normal");
}

//Para ejecutar: funcionAsVariable()
const funcionAsVariable = function (){
    console.log("Se ejecutó una función como variable");
}

//Para ejecutar: arrowFunction() 
const arrowFunction = () => {
    console.log("Se ejecutó una arrow function");
}
// SI SOLO TIENE UN PARAMETRO: param => {}
const arrowUnParametro = param => {
    console.log(param);
}
// SI SOLO RETURNA ALGO: param => retorno
const arrow2 = () => console.log('Hello');
// SI SOLO RETORNA UN OBJETO
const arrow3 = persona => ({
    ...persona,
    edad: persona.edad + 22
})

//RETO 
const MAYORIA_DE_EDAD = 18;
const esMayorDeEdad = ({edad}) => edad >= MAYORIA_DE_EDAD;
const esMenorDeEdad = (persona) => !esMayorDeEdad(persona);

