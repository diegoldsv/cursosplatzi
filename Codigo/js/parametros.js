//Parametros por referencia
function modificaObj(obj){
    obj.edad+=1;
}
function noModificaObj(obj){
    return {
        ...obj,
        edad: obj.edad + 1
    }
}