# ! /bin/bash
# Uso de loops

#For: Imprimir ficheros del directorio actual
for file in $(ls)
do
    echo "${file}"
done

#Iterar con while
numero=0
while [ $numero -lt 10 ]
do
    echo $numero
    numero=$(( numero + 1 ))
    #Ejemplo Break
    if [ $numero -eq 3 ]; then
        echo "Abortamos"
        break;
    fi
done

