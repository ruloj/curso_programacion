# VARIABLES
# Una variable es un espacio para guardar un valor
# nombre_variable = valor
nombre_variable = "snake case"
nombreVariable = "camel case"
NombreVariable = "pascal case"

####################################################################

### TIPOS DE DATOS
# Clasificación de los valores que se pueden guardar en una variable

## NUMEROS
# INT
entero = 10
print("La variable 'entero' tiene guardado el valor: " + str(entero) + " es de tipo: " + str(type(entero)))

# FLOAT
flotante = 10.0
print("La variable 'flotante' tiene guardado el valor: " + str(flotante) + " es de tipo: " + str(type(flotante)))


## TEXTO
# STRING
cadena = "Texto de ejemplo"
print("La variable 'cadena' tiene guardado el valor: " + str(cadena) + " es de tipo: " + str(type(cadena)))


## BOOLEANO
# BOOL
# explicito
booleano = False
print("La variable 'booleano' tiene guardado el valor: " + str(booleano) + " es de tipo: " + str(type(booleano)))
# implicito
booleano = 5 > 3
print("La variable 'booleano' tiene guardado el valor: " + str(booleano) + " es de tipo: " + str(type(booleano)))


## NONE
# representa vriable sin un valor definido
none = None
print("La variable 'none' tiene guardado el valor: " + str(none) + ". Es de tipo: " + str(type(none)))