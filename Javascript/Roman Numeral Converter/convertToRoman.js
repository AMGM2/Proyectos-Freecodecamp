function convertToRoman(num) {
    let toRest = num ;
    let roman = {I:1, IV:4, V:5, IX:9,  X:10, XL: 40, L:50, XC:90,  C:100, CD:400, D:500, CM: 900, M:1000};
    let romanVal = (Object.values(roman));// toma los valores de los numeros
    let romanKey = (Object.keys(roman));// toma los valores de los numeros romanos
    let count = romanVal.length-1
    let romanNum =[]
    // se inicia un while con la condicion de count mayor igual a 0 
    while(count >= 0){
    if(romanVal[count] > toRest){ // si la cantidad de numeros es mayor a al numero dado 
    count--; // se le resta -1 a la cantidad
    } else { 
    romanNum.push(romanKey[count]) // añade la cantidad de numeros romanos a la variable vacia
    toRest -=romanVal[count] // a toRest se le resta la cantidad de 
    }
    }
     return romanNum.join(""); // se retorna 
    }
    
    convertToRoman(36);