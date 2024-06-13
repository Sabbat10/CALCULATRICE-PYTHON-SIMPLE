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
    try:
        resultat = premier_nombre / deuxieme_nombre
        return int(resultat)
    except ZeroDivisionError:
        return("Impossible de diviser par 0")

