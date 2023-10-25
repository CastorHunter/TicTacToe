#1. Écrire la fonction permettant d’afficher la grille de jeu.
#Elle prend un tableau en entrée, et affiche la grille grâce aux données du tableau.

liste_donnee = ["X","O","X","X","O"," ","O","X"," "]

def grille(liste):
    for i in range(3):
        for j in range(3):
            print(liste[i*3+j], end ="")
            if j<2:
                print("|", end="")
        print("")
    return liste

grille(liste_donnee)

#2. Écrire la fonction permettant de jouer un O ou un X.
#Elle prend un tableau en entrée, et le modifie afin d’ajouter un O ou un X à l’endroit souhaité
#par le joueur courant.

liste_donnee = [" "," "," "," "," "," "," "," "," "]

def placement(valeur, liste ,numero_case):
    if valeur=="X" or valeur=="O":
        if liste[numero_case-1]==" ":
            liste[numero_case-1]=valeur
            return True
        else :
            return False
    else :
        return False

#3. Écrire les fonctions vérifiant si oui ou non l’un des joueurs a réussi à aligner 3
#symboles sur une ligne verticale, horizontale, diagonale.

liste_donnee = ["X","O","X","X","O","X","O","X","X"]
#programme qui ne marche pas car non abouti, du au manque de temps
'''
def verification(liste, indice=0, echec=0, passage=1):
    if passage == 3:
        return True
    valeur = liste[indice]
    if valeur=="O" or valeur =="X":
        if echec == 3:
            return "test"
        if valeur==liste[passage+indice]:
            return verification(liste, indice, echec,  passage+1)
        else :
            return verification(liste, indice+3, echec+1, passage=0)
    return False
'''
#programme qui marche mais qui est "mal fait"
def verification(liste):
    if liste[0]=="X" or liste[0]=="O":
        if liste[0] == liste[1] and liste [1] == liste[2]:
            return True 
        if liste[0] == liste[4] and liste [4] == liste[8]:
            return True  
        if liste[0] == liste[3] and liste [3] == liste[6]:
            return True  
    if liste[6]=="X" or liste[6]=="O":
        if liste[6] == liste[7] and liste [7] == liste[8]:
            return True 
        if liste[7] == liste[4] and liste [4] == liste[2]:
            return True  
    if liste[2]=="X" or liste[2]=="O":
        if liste[2] == liste[5] and liste [5] == liste[8]:
            return True 
    if liste[1]=="X" or liste[1]=="O":
        if liste[1] == liste[4] and liste [4] == liste[7]:
            return True 
    return False

print(verification(liste_donnee))

#4. Écrire la fonction vérifiant si la grille est complète.
#Elle prend un tableau en entrée, et renvoie un booléen en sortie grâce à l’instruction return.

liste_donnee = ["X","X"," ","X","O","X","O","X","X"]

def complete(liste):
    for i in range(9):
        if liste[i] == " ":
            return False
    return True

print(complete(liste_donnee))

#5. Écrire un programme permettant de jouer à deux au Tic tac toe.
#Servez-vous des fonctions écrites dans les exercices 1 à 4 !


liste_donnee = [" "," "," "," "," "," "," "," "," "]
print("Voici le Tic tac toe!")
cases_dispo = [1,2,3,4,5,6,7,8,9]
tours = 0
reponse = ""
case = 0
grille(liste_donnee)
while verification(liste_donnee) == False and tours !=9 :
    print("c'est au tour du joueur", tours%2+1)
    while reponse != "X" and reponse !="O":
        reponse = input("Joueur, entres une valeur, X ou O : ")
    while case not in cases_dispo:
        case = input("Joueur, entres le numéro de la case. Les numéros de cases sont dans l'ordre de lecture, ainsi la case en haut à droite est la case 3 : ")
        if case in ["1","2","3","4","5","6","7","8","9"]:
            case = int(case)
    for i in range(len(cases_dispo)):
        if cases_dispo[i]==case:
            indice_case = i
    cases_dispo.pop(indice_case)
    print(cases_dispo)
    placement(reponse, liste_donnee ,case)
    grille(liste_donnee)
    tours +=1
    reponse = ""
    case = 0
print("Le Tic tac toe est terminé ! regardez qui as gagné!")

"""
6. Qu’aura-t-on besoin de faire, si on souhaite désormais programmer un jeu de
Puissance 4 ?

On devra s'arranger pour pouvoir placer uniquement de pions en bas ou sur d'autres pions, donc créer une fonction qui le vérifie.
Il faudrait également augmenter la taille de la grille, et le nombre de cases requis
"""