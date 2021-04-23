# !/bin/bash
# Capturar informacion del usuario

option=0
backupName=""
clave=""

echo "Programa Utilidades Postgres"
read -n1 -p "Ingresar una opción:" option
echo -e "\n"
read -n10 -p "Ingresar el nombre del backup:" backupName
echo -e "\n"
echo "Opcion: $option, Backup Name: $backupName"
echo -e "\n"
read -s -p "Ingresar clave:" clave
echo -e "\n"
echo "Clave: $clave"
