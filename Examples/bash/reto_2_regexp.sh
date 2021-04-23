# !/bin/bash
# Uso de expresiones regulares para validación de datos

# Datos del Usuario
userId=
userCountry=
userBirthDay=

# Validaciones
userIdRegexp='^[0-9]{10}$'
userCountryRegexp='VE|US|ES'
userBirthDayRegexp='^19|20[0-9]{2}[1-12][1-31]$'

echo "Ingrese los siguientes datos:"
read -p "Identificador: " userId
read -p "Pais de Origen (VE|US|ES): " userCountry
read -p "Fecha de Nacimiento (yyyyMMDD): " userBirthDay

# Validacion: ID
if [[ $userId =~ $userIdRegexp ]]; then
    echo "OK: Identificación válida"
else
    echo "KO: Identificación inválida"
fi

# Validacion: PAIS DE ORIGEN
if [[ $userCountry =~ $userCountryRegexp ]]; then
    echo "OK: Pais de Origen válido"
else
    echo "KO: Pais de Origen inválido"
fi

# Validacion: FECA DE NACIMIENTO
if [[ $userBirthDay =~ $userBirthdayRegexp ]]; then
    echo "OK: Fecha de Nacimiento válida"
else
    echo "KO: Fecha de Nacimiento inválida"
fi

echo "FIN DEL PROGRAMA"
