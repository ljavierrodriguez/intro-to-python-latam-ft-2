/* Loops */
/* 

for(iterator; condition; increment){
    codigo
}

for(index in collection){
    codigo
}

for(valor of collection){
    codigo
}

while(condition){
    codigo
}

do {
    codigo
} while (condition)


*/

let numeros = [1, 2, 3, 4, 5, 6]

for(let i = 1; i <= 10; i++){
    console.log(i)
}

for(let i = 0; i < numeros.length; i++ ){
    console.log(numeros[i])
}

for(let indice in numeros){
    console.log(numeros[indice])
}

for(let valor in numeros){
    console.log(valor)
}

let indice = 0;
while(indice < numeros.length){
    console.log(numeros[indice])
    indice++
}

indice = 0;
do {
    console.log(numeros[indice])
    indice++
} while (indice < numeros.length)
