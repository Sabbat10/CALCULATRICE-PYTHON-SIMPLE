## choisez l'opération
# choice = int(input("Choisissez l'opération \n 1: addition \n 2: multiplication\n 3: soustraction \n 4: division \n \n choisissez une opération : "))
while True:
    choice = int(input("Choisissez l'opération \n 1: addition \n 2: multiplication\n 3: soustraction \n 4: division \n \n Choisissez une opération : "))
    if choice in [1, 2, 3, 4]:
        break
    else:
        print("Choix invalide. Veuillez choisir une opération valide.")

## les conditions
if choice == 1:
    print("Vous avez choisi l'addition")
elif choice == 2:
    print("Vous avez choisi la multiplication")
elif choice == 3:
    print("Vous avez choisi la soustraction")
elif choice == 4:
    print("Vous avez choisi la division")
else:
    print("Choix invalide")

## les variables

nombre_un = int((input("Entrez un nombre : ")))
nombre_deux = int(input("Entrez un autre nombre : "))

## les fonctions
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

## les resultats
if choice == 1:
    print(f"{nombre_un} + {nombre_deux} = {addition(nombre_un, nombre_deux)}")
elif choice == 2:
    print(f"{nombre_un} * {nombre_deux} = {multiplication(nombre_un, nombre_deux)}")
elif choice == 3:
    print(f"{nombre_un} - {nombre_deux} = {soustraction(nombre_un, nombre_deux)}")
elif choice == 4:
    print(f"{nombre_un} / {nombre_deux} = {division(nombre_un, nombre_deux)}")
