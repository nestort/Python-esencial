# Tuplas
# Una tupla es una secuencia finita de objetos inmutable.

# Creación de tupla:
tupleA = (2, True, "Bossie", 23)

# Impresión del valor: 'Bossie'
print(tupleA[2])

# Recorrido de toda la tupla
indexValue = 0  # la tuplas inician desde el valor cero
while indexValue < len(tupleA):
    print("=>Inidice:", indexValue, "Valor:", tupleA[indexValue])
    indexValue = indexValue+1  # Incremento de indice

# Recorrido de la tupla usando For
for value in tupleA:
    print(value)

# Slicing(:) Porcion de la tupla
print("Porcion de la posición 1 a la 3:\n", tupleA[1:3])
print("Porcion de la posición 0 a la 2:\n", tupleA[:2])
print("Porcion de la posición 2 al final:\n", tupleA[2:])

# Slicing en cadenas
name = "Obi Wan Kenobi"
print("Porcion de la posición 4 a la 7:\n", name[4:7])
print("Porcion de la posición 0 a la 7:\n", name[:7])
print("Porcion de la posición 4 al final:\n", name[4:])

# Listas
# A diferencia de las tuplas, las listas pueden cambiar su longitud agregando o eliminando
# elementos.

# Creación de 2 listas
listA = [1, 3, 43, 4]
listB = ['Darth', 'Maul', 1.78]

# Concatenar o unir listA y listB
joinList = listA+listB
print(joinList)

# Busqueda de elemento en lista usando 'if'
if 'Darth' in joinList:
    print("Se encontro 'Darth' en la lista")
else:
    print("No se encontro a 'Darth'")

# Slicing en lista
print("Porcion de la posición 4 a la 7:\n", joinList[4:7])
print("Porcion de la posición 0 a la 7:\n", joinList[:7])
print("Porcion de la posición 4 al final:\n", joinList[4:])

# Indices negtaivos
# Nos sirven para recorrer una tupla, cadena, lista, entre otros 
# partiendo de la posicion inicial hacia la final 

# Ultimo elemento de tupla
print(tupleA[-1])

# Pen-Ultimo elemento de cadena
print(name[-2])

# Ultimo elemento de lista
print(listA[-1])

# Diccionarios
# A diferencia de las tuplas y listas los diccionarios permiten manipular los indices

#Creación de diccionario
dictA={"Obi":"2","darthMaul":"9"}

# Obtetener valor de 'darthMaul' del diccionario
print("El valor de Darth Maul es:",dictA['darthMaul'])


