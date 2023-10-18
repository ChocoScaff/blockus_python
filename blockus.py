
import time
from console import *


# ANSI escape codes for text colors
GREEN = '\033[92m'
RED = '\033[91m'

def number_to_letter(number):
    if 1 <= number <= 26:
        return chr(ord('a') + number - 1)
    else:
        return "Invalid input: Number out of range"

def letter_to_number(letter):
    if len(letter) == 1 and 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    else:
        return "Invalid input: Not a lowercase letter"


# Initialise la grille de facon a ce qu'elle contienne ce qui se trouve 
# a la figure de droite 

def initGrille (grille) :
    # initialiser la grille à vide :
      
    i=0
    for i in range(1,20):
        if (i <  10):
            grille[0][i+1]= str(i) + " "
        elif (i >= 19):
            pass
        else:
            grille[0][i+1]= str(number_to_letter(i-9) + " ")
    
    for ligne in range (1,20) :
        for colonne in range (1,20) :
            grille[ligne][colonne]='  '
     
        
    for colonne in range (1,21) :
        grille[1][colonne]='* '    #'* '
        grille[20][colonne]='* '


    for ligne in range (1,21) :
        if (ligne <  10):
            grille [ligne+1][0]=ligne
        elif (ligne >= 19):
            pass
        else:    
            grille [ligne+1][0]=str(number_to_letter(ligne-9))
            
        grille [ligne][1]='* '
        grille [ligne][20]='* '

    #grille [pos_balle_x][pos_balle_y]='O'
    
    
def possitionnerPiece(grille, posX, posY,joueur=1):
    if joueur == 1:
        grille [posY][posX] = '0 '
    elif joueur == 2:
        grille [posY][posX] = '# '

def verifierAngle(grille, posX, posY, joueur=1):
    if joueur == 1:
        char = '0 '
    if joueur == 2:
        char = '# '
        
    if grille[posY-1][posX+1] == char: #Diag Haut Droite
        return True
    elif grille[posY-1][posX-1] == char: #Diag Haut Gauche
        return True
    elif grille[posY+1][posX+1] == char: #Diag Bas Droite
        return True
    elif grille[posY+1][posX-1] == char: #Diag Bas Gauche
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
   
def verifierCote(grille, posX, posY,joueur=1):
    
    if joueur == 1:
        char = '0 '
    if joueur == 2:
        char = '# '
    
    if grille[posY][posX+1] == char: #Droite
        return False
    elif grille[posY][posX-1] == char: #Gauche
        return False
    elif grille[posY-1][posX] == char: #Bas
        return False
    elif grille[posY+1][posX] == char: #haut
        return False
    
    return True

def selectionnerUnePiece():
    piece = input("1 0; 2 00, 3 000, 4 0000 :")
    if piece == "1":
        return 0
    elif piece == "2":
        return 1
    elif piece == "3":
        return 2
    elif piece == "4":
        return 3

def verifierPiece(x,y):
    #piece = selectionnerUnePiece()
    piece = 0
    #for i in range(0,piece):
    cote = verifierCote(grille, x, y)
    angle = verifierAngle(grille, x, y)
    
    if (cote == False) or (angle == False):
        print("invalide")
        return
    
    #for i in range(piece):
    possitionnerPiece(grille,x+piece,y)
    
    
    
##################################
# programme principal :
##################################
    
    
grille= [[' ' for i in range(21)] for j in range(21)] 	# grille qui pourra contenir
                # 3 sortes de caractères : '*' ou 'O' ou le caractere espace ' '


initGrille (grille) ;

console_afficheGrille(grille)

s='*'
while (s!='s') :
    #effaceEcran ()
    #afficheGrille(grille);
	
    x = input("Entree la ligne ")
    x = x.lower()
    if 'a' <= x <= 'z':
        x = ord(x) - 86
    else:
        x = int(x) + 1
        
    y = input("Entrer la colonne ")
    y = y.lower()
    if 'a' <= y <= 'z':
        y = ord(y) - 86
    else:
        y = int(y) + 1
           
    
    verifierPiece(x, y)
        
    console_afficheGrille(grille);
    s=input("Appuyez sur la touche entrée ou 's' pour sortir... ")
        