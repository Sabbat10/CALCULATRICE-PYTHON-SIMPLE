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
    if deuxieme_nombre == 0:
        return("Vous ne pouvez pas diviser par 0")
    resultat = premier_nombre / deuxieme_nombre
    return resultat

