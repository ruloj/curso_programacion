# ALGORITMO DE ORDENAMIENTO DE LA BURBUJA

def bubble_sort(lista):
    longitud = len(lista)
    for i in range(longitud-1):
        for j in range(longitud-i-1):
            if lista[j] > lista[j+1]:
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar
    return lista


lista_desordenada = [5, 2, 8, 0, 3, 1, 5]

# print(lista_desordenada)
# lista_ordenada = bubble_sort(lista_desordenada)
# print(lista_desordenada)

def convertir_lista_a_str(lista):
    return [str(i) for i in lista]


## ESTA FUNCION IMPRIME PASO A PASO EL ALGORITMO
## Ejecutar dar ENTER para continuar entre cada paso
def bubble_sort_print(lista):
    longitud = len(lista)
    print("longitud lista: ", longitud)
    for i in range(longitud-1):
        print("valor i:", i)
        for j in range(longitud-i-1):
            lista_apuntadores = [' ' for _ in range(longitud)]
            lista_apuntadores[j] = "\u2191"
            lista_apuntadores[j+1] = "\u2191"
            print("\tvalor j:", j)
            print("\tEvaluando los valores de la lista")
            print("\t",convertir_lista_a_str(lista))
            print("\t",lista_apuntadores)
            print("\t",lista[j], ">", lista[j+1], "--->", lista[j] > lista[j+1])
            if lista[j] > lista[j+1]:
                print("\t\tse intercambian:")
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar
            else:
                print("\t\tse mantiene:")
            print("\t\tlista actualizada: ", lista)
            input()
    print("\n")
    return lista


print("lista original:", lista_desordenada)
lista_ordenada = bubble_sort_print(lista_desordenada)
print("lista ordenada:", lista_desordenada)

