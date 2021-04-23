# !/bin/bash
# Sintaxis de setencia case

notaClase=0

read -n1 -p "Indique cual es su nota (1-9): " notaClase
echo ""


case $notaClase in
    1) echo "No sabias nada :)";;
    [2-4]) echo "Reprobaste";;
    [5-8]) echo "Aprobaste";;
    9) echo "Sabias todo :o";;
    *) echo "Este valor no corresponde a una nota";;
esac
