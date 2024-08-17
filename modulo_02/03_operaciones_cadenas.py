### OPERADORES ARITMETICOS

texto_1 = "Hola"
texto_2 = "mundo"
texto_3 = ""


## OPERADORES
print("OPERADORES")

# Concatenación (+): Une dos cadenas.
resultado = texto_1 + texto_2
print("resultado de la concatenación: " + resultado)
print("resultado de la concatenación:", resultado)

# Repetición (*): Repite n cantidad de veces la cadena.
resultado = texto_1 * 4
print("resultado de la repetición:", resultado)




## FUNCIONES
print("FUNCIONES")

# Longitud 'len()'
resultado = len(texto_1)
print("La variable texto_1 con la cedena '" +  texto_1 + "' tiene un total de " + str(resultado) +  " caracteres")
print("La variable texto_1 con la cedena '" +  texto_1 + "' tiene un total de", resultado, "caracteres")
print("La variable texto_2 con la cedena '" +  texto_2 + "' tiene un total de", len(texto_2), "caracteres")
print("La variable texto_3 con la cedena '" +  texto_3 + "' tiene un total de", len(texto_3), "caracteres")

# Convertir int|float a str 'str()'
valor_antes = 1
valor_despues = str(valor_antes)
print("El tipo de valor es:", type(valor_antes), " - El tipo de valor despues es: ", type(valor_despues))
print("El tipo de valor es:", type(2.0), " - El tipo de valor despues es: ", type(str(2.0)))

# Convertir str a int 'int()'
valor_antes = "1"
valor_despues = int(valor_antes)
print("El tipo de valor es:", type(valor_antes), " - El tipo de valor despues es: ", type(valor_despues))

# Convertir str a float 'float()'
print("El tipo de valor es:", type("2.0"), " - El tipo de valor despues es: ", type(float("2.0")))




## METODOS
print("METODOS")

# Convertir a mayusculas '.upper()':
print("El texto", texto_1, "en mayusculas", texto_1.upper())

# Convertir a minisculas '.lower()':
print("El texto", texto_1, "en minisculas", texto_1.lower())


texto_4 = "hola mundo," \
        "el mundo es muy grande"

# Remplazar una subcadena '.replace(<subcadena_en_cadena>,<subcadena_que_la_remplaza>)'
resultado = texto_4.replace("mundo","universo")
print(resultado)

# Numero de repeticiones de una subcadena '.count(<subcadena_a_contar>)'
resultado = texto_4.count(texto_2)
print("La palabra:", texto_2, "se repite ",resultado,"veces en",texto_4)





# EJERCICIO
# El siguiente texto remplazar la palabra "Juan", por tu nombre
# Y ayudale a corregir su tarea
"""
    Juan era un niño de 5 años aprendiendo a escribir su nombre.
    En la escuela le dejaron hacer una plana de su nombre
    Juan
    juan
    JuAn
    JUAN
    Juan
    jUan
"""
