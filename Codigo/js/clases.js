//PROTOTYPE
//Constructor
function Tarea(nombre, descripcion, date){
    this.nombre = nombre;
    this.descripcion = descripcion;
    this.date = date;
}
//Funciones que se añaden al prototype
Tarea.prototype.setTerminada = () => console.log(`La tarea ${nombre} fue realizada`);

var estudiar = new Tarea('Estudiar', 'Curso Platzi JS', '07/07/2019')

//Clases
//Herencia: con extends y super en el contructor

class Tarea2 {
    constructor(nombre,descripcion,date){
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.date = date;
    }

    setTerminada() {
        console.log(`La tarea ${nombre} fue realizada`);
    }
}