# Manejo de archivos
# Abre el archivo, si no existe lo crea
def createFile():
    fileTest = open('notes.txt','w')
    fileTest.close()
    print('creado cone éxito.')

def writeFile():
    fileTest = open('notes.txt','a') # Se usa 'a' para no sustituir datos
    fileTest.write('Nombre: Bossie2')
    fileTest.close
    print('Se escribio con éxito')

def readFile():
    fileTest = open('notes.txt','r')
    lineText=fileTest.readline()
    while lineText != "":
        print(lineText)
        lineText=fileTest.readline()
    fileTest.close()

#Crea el archivo
createFile()

# Escribir en archivo
writeFile()

# Leer archivo
readFile()