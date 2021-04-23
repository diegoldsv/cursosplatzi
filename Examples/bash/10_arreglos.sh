# ! /bin/bash
# Uso de Arreglos

arregloNumeros=(1 2 3 4 5 6)
arregloCadenas=(Marco, Antonio, Pedro, Susana)
arregloRangos=({A..Z} {10..20})

#Imprimir todos los valores
echo "Arreglo de Numeros (${#arregloNumeros[*]}): ${arregloNumeros[*]}"
echo "Arreglo de Cadenas (${#arregloCadenas[*]}): ${arregloCadenas[*]}"
echo "Arreglo de Rangos (${#arregloRangos[*]}): ${arregloRangos[*]}"
