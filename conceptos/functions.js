// Functions
/*
1. Funciones Declaradas

function nameFun(params?){
    codigo
}

2. Funciones Flecha (Arrow Functions)

const funcName = (params?) => return


3. Funciones Anonimas

const name = function(params?){
    codigo
}


*/

/* 1. */

function saludar(){
    console.log("Hola Mundo")
}

saludar() // Hola Mundo

/* 2. */

const sumar = (a, b) => a + b

console.log(sumar(10, 10)) // 20


/* 3. */

const multiplicar = function(a, b){
    return a * b
}

console.log(multiplicar(10, 10)) // 100


let numeros = [1, 2, 3, 4, 5]

let resultado = numeros.map((num) => num**2) // [1, 4, 9, 16, 25]

let resutado2 = numeros.map(function(num){ 
    return num**2
})

function cuadrado(num){ 
    return num**2
}

let resultado3 = numeros.map(cuadrado)


function nombreCompleto(nombre, apellido = "Doe", edad){
    console.log(`${nombre} ${apellido} tienes ${edad} años`) // John Doe
}

nombreCompleto("John", "Doe")

nombreCompleto("Maria", 34) // Maria 34 undefined


function totalizar(...rest){ // rest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return rest.reduce((total, num) => total + num, 0)
}

console.log(totalizar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))