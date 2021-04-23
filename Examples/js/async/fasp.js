//Funciones como parametros
function despedirse (){
    console.log('Logout');
}

function saludar(fn){
    console.log('Login');
    if(fn){
        fn();
    }
}
