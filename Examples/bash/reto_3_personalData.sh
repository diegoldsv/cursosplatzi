# !/bin/bash
# Obtener informacion personal del usuario

nombre=
apellidos=
edad=
direccion=
tlf=

echo "Ingresar informacion personal:"
read -p "Nombre: " nombre
read -p "Apellido(s): " apellidos
read -n2 -p "Edad: " edad
echo -e "\n"
read -p "Direccion: " direccion
read -n9 -p "Tlf: " tlf
echo -e "\n"

echo "Nombre: $nombre"
echo "Apellido(s): $apellidos"
echo "Edad: $edad"
echo "Direccion: $direccion"
echo "Tlf: $tlf"

