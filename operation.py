nombre_deux = 0

def addition(premier_nombre, deuxieme_nombre):
    resultat = premier_nombre + deuxieme_nombre
    return resultat

def multiplication(premier_nombre, deuxieme_nombre):
    resultat = premier_nombre * deuxieme_nombre
    return resultat

def soustraction(premier_nombre, deuxieme_nombre):
    resultat = premier_nombre - deuxieme_nombre
    return resultat

def division(premier_nombre, deuxieme_nombre):
    if nombre_deux == 0:
        return "Impossible de diviser par 0"
    resultat = premier_nombre / deuxieme_nombre
    return resultat