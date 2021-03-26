# !/bin/bash
# Sintaxis de condicionales

notaClase=0
edad=0

read -n1 -p "Indique cual es su nota (1-9): " notaClase
echo ""

# Double Brackets expande el estandar de condicionales (No es portable a otros tipos de shell)
if [ $notaClase -gt 7 ]; then
    echo "Aprobaste!"
else
    echo "Reprobaste :("
fi


read -n2 -p "Indique cual es su edad: " edad
echo ""

# Single Brackets estandar de condicionales POSIX (Es portable a otros tipos de shell)
if (( $edad >= 18 )); then
    echo "Puedes Votar!"
else
    echo "No puedes Votar :("
fi
