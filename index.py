## les variables
nombre_un = len(input("Entrez un nombre : "))
nombre_deux = len(input("Entrez un autre nombre : "))

## les fonctions
def addition(premier_nombre, deuxieme_nombre):
    return premier_nombre + deuxieme_nombre

def multiplication(premier_nombre, deuxieme_nombre):
    return premier_nombre * deuxieme_nombre

def soustraction(premier_nombre, deuxieme_nombre):
    return premier_nombre - deuxieme_nombre

def division(premier_nombre, deuxieme_nombre):
    if nombre_deux == 0:
        return "Impossible de diviser par 0"
    return premier_nombre / deuxieme_nombre

## les instructions
print(f"{nombre_un} + {nombre_deux} = {addition(nombre_un, nombre_deux)}")
print(f"{nombre_un} * {nombre_deux} = {multiplication(nombre_un, nombre_deux)}")
print(f"{nombre_un} - {nombre_deux} = {soustraction(nombre_un, nombre_deux)}")
print(f"{nombre_un} / {nombre_deux} = {division(nombre_un, nombre_deux)}")

