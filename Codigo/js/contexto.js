// Quién es This?
function Objeto(valor1, valor2){
    this.valor1 = valor1;
    this.valor2 = valor2;
    //This corresponde al objeto que se creara
}

//This: quien llame a la funcion
Objeto.prototype.accion = function () {
    return this.valor1;
}

//This: objeto global (ej: Window)
Objeto.prototype.accion2 = () => this.valor2;