
// Operadores de atribuição: usados para atribuir valores às variáveis

let A = 2; 
// Inicialmente, A vale 2
// Cada operação abaixo altera o valor de A de acordo com o operador usado

A = A + 2; // Soma o valor atual de A com 2. Resultado: A = 4
A += 12;   // Equivalente a A = A + 12. Resultado: A = 16
A -= 3;    // Subtrai 3 do valor atual de A. Resultado: A = 13
A *= 3;    // Multiplica o valor atual de A por 3. Resultado: A = 39
A /= 3;    // Divide o valor atual de A por 3. Resultado: A = 13
A %= 5;    // Calcula o resto da divisão de A por 5. Resultado: A = 3
A **= 2;   // Eleva o valor atual de A ao quadrado. Resultado: A = 9

// Operadores lógicos: usados para fazer verificações lógicas

// Operador AND (&&): Retorna verdadeiro somente se ambos os valores forem verdadeiros
// Operador OR (||): Retorna verdadeiro se pelo menos um dos valores for verdadeiro
// Operador NOT (!): Inverte o valor lógico (true para false e vice-versa)

// Exemplos de operações lógicas
const result1 = true && false; // false, pois ambos os valores não são verdadeiros
const result2 = false && false; // false, pois ambos os valores são falsos
const result3 = true && true; // true, pois ambos os valores são verdadeiros

const result4 = true || false; // true, pois pelo menos um dos valores é verdadeiro
const result5 = false || true; // true, pelo mesmo motivo
const result6 = false || false; // false, pois ambos os valores são falsos

const result7 = !true; // false, pois inverte o valor lógico de true para false
const result8 = !false; // true, pois inverte o valor lógico de false para true

// Note que a declaração abaixo contém um erro:
// const G = true; // Isso não corresponde a um operador lógico
