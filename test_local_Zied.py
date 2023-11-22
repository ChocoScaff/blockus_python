"""
Created on Wed Nov 22 15:40:36 2023

@author: jradzied


@author: PC
"""

from pieces import Piece

# Initialise la grille de façon à ce qu'elle contienne ce qui se trouve à la figure de droite
def initGrille(grille):
    # initialiser la grille à vide :
    
    i = 0
    for i in range(1, 20):
        if i < 10:
            grille[0][i + 1] = str(i) + " "
        elif i >= 19:
            pass
        else:
            grille[0][i + 1] = str(number_to_letter(i - 9) + " ")
    
    for ligne in range(1, 20):
        for colonne in range(1, 20):
            grille[ligne][colonne] = '  '
     
    for colonne in range(1, 21):
        grille[1][colonne] = '* '    # Bord supérieur
        grille[20][colonne] = '* '   # Bord inférieur

    for ligne in range(1, 21):
        if ligne < 10:
            grille[ligne + 1][0] = ligne
        elif ligne >= 19:
            pass
        else:
            grille[ligne + 1][0] = str(number_to_letter(ligne - 9))
            
        grille[ligne][1] = '* '  # Bord gauche
        grille[ligne][20] = '* '  # Bord droit

def number_to_letter(number):
    if 1 <= number <= 26:
        return chr(ord('a') + number - 1)
    else:
        return "Invalid input: Number out of range"

def verifierAngle(grille, posX, posY, joueur=1):
    if joueur == 1:
        char = '0 '
    if joueur == 2:
        char = '# '
        
    if grille[posY - 1][posX + 1] == char:  # Diag Haut Droite
        return True
    elif grille[posY - 1][posX - 1] == char:  # Diag Haut Gauche
        return True
    elif grille[posY + 1][posX + 1] == char:  # Diag Bas Droite
        return True
    elif grille[posY + 1][posX - 1] == char:  # Diag Bas Gauche
        return True
    elif posX == 2 and posY == 2:
        return True
    elif posX == 19 and posY == 19:
        return True
    elif posX == 2 and posY == 19:
        return True
    elif posX == 19 and posY == 2:
        return True
    
    return False

def verifierCote(grille, posX, posY, joueur=1):
    if joueur == 1:
        char = '0 '
    if joueur == 2:
        char = '# '
    
    if grille[posY][posX + 1] == char:  # Droite
        return False
    elif grille[posY][posX - 1] == char:  # Gauche
        return False
    elif grille[posY - 1][posX] == char:  # Bas
        return False
    elif grille[posY + 1][posX] == char:  # Haut
        return False
    
    return True

def possitionnerPiece(grille, posX, posY, joueur=1):
    if joueur == 1:
        grille[posY][posX] = '0 '
    elif joueur == 2:
        grille[posY][posX] = '# '

def verifierPiece(x, y, grille, joueur=1):
    cote = verifierCote(grille, x, y, joueur)
    angle = verifierAngle(grille, x, y, joueur)
    
    if (cote == False) or (angle == False):
        print("invalide")
        return

def selectionnerUnePiece():
    pieces_index = int(input("1 Carré 5x5; 2 Rectangle 3x7, 3 Triangle équilatéral 3x3, 4 Simple rectangle 2x2 :"))
    
  #check index
    if 1 <= pieces_index <= 4:
        return pieces_index
    else:
        print("Choix invalide. Veuillez saisir un nombre entre 1 et 4.")
        return None


