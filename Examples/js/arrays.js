//Arrays
var array = [1, 2, 3, 4, 5, 6 , 7, 8, 9 , 10]

//Filtrar 
//.filter() recibe una funcion que se le pasa cada elemento y retorna true o false. Retorna un nuevo array
//Ejemplo
const esPar = num => num%2 == 0;
console.log(array.filter(esPar));

//Map
//.map() recibe una funcion que se le pasa cada elemento y lo modifica. Retorna un nuevo array
//Ejemplo
const powerToTwo = num => num * num;
console.log(array.map(powerToTwo));

//Reduce
//.reduce() devuelve 1 valor a partir de un array
// Dos parametros:
// Funcion que recibe el acumulado y el elemento.
// Valor Incial
//Ejemplo
const sumaTotal = (acum, element) => acum += element;
console.log(array.reduce(sumaTotal, 0));

