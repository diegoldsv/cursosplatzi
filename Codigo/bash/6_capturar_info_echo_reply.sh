# !/bin/bash
# Capturar informacion del usuario

option=0
backupName=""

echo "Programa Utilidades Postgres"
echo -n "Ingresar una opción:"
read
option=$REPLY
echo -n "Ingresar el nombre del backup:"
read
backupName=$REPLY
echo "Opcion: $option, Backup Name: $backupName"
