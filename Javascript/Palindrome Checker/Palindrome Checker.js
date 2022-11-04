function palindrome(str) {
  
   let newStr = str.toLowerCase().replace(/[^a-z\d]/g, '');/** aqui reemplaza todos los caracteres no alfanumericos de la "a" a la "z" y
    pone las letras en minusculas en una cadena vacia */ 
   return newStr.split('').reverse().join('') === newStr; /**  aqui lo divide en una matriz de caracteres luego lo invierte y
    une y lo compara para que tome todos los casos de pruebas*/
   }
  
   console.log(palindrome("eye___"));