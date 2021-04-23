# !/bin/bash
# Programar para revisar tipos de operadores
# Autor: Diego L. Di Salvatore Veiga

numA=10
numB=12

echo "Numeros usados"
echo "numA=$numA"
echo "numB=$numB"

echo "Operadores Aritmeticos"
echo "A + B=" $((numA + numB))
echo "A - B=" $((numA - numB))
echo "A * B=" $((numA * numB))
echo "A / B=" $((numA / numB))
echo "A % B=" $((numA % numB))

echo "Operadores Relacionales"
echo "A > B=" $((numA > numB))
echo "A < B=" $((numA < numB))
echo "A >= B=" $((numA >= numB))
echo "A <= B=" $((numA <= numB))
echo "A == B=" $((numA == numB))
echo "A != B=" $((numA != numB))

echo "Operadores Asignacion"
echo "A += B=" $((numA += numB))
echo "A -= B=" $((numA -= numB))
echo "A *= B=" $((numA *= numB))
echo "A /= B=" $((numA /= numB))
echo "A %= B=" $((numA %= numB))
