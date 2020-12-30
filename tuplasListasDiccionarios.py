# Tuplas
# Una tupla es una secuencia finita de objetos inmutable.

# Creación de tupla:
values = (2, True, "Bossie", 23)

# Impresión del valor: 'Bossie'
print(values[2])

# Recorrido de toda la tupla
indexValue = 0  # la tuplas inician desde el valor cero
while indexValue < len(values):
    print("=>Inidice:", indexValue, "Valor:", values[indexValue])
    indexValue = indexValue+1  # Incremento de indice

# Recorrido de la tupla usando For
for value in values:
    print(value)

# Slicing(:) Porcion de la tupla
print("Porcion de la posición 1 a la 3:\n", values[1:3])
print("Porcion de la posición 0 a la 2:\n", values[:2])
print("Porcion de la posición 2 al final:\n", values[2:])

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
