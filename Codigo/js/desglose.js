//Desglosar obj
function desglosarObj({ edad }){
    console.log(edad)
}
function desestructurarObj(persona){
    //var nombre = persona.nombre
    //var edad = persona.edad
    var { nombre, edad } = persona;
    console.log(nombre, edad);
}