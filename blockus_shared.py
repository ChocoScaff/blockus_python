
##
#Created on Wed Nov 22 14:03:09 2023
#
#@file blockus_shared.py
#


# Importation des bibliothèques nécessaires
import time
from console import *

import asyncio
import json

# bibliothèque pieces
from pieces import Piece, pieces




## Initialise la grille de facon a ce qu'elle contienne ce qui se trouve 
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

##
#
def number_to_letter(number):
    if 1 <= number <= 26:
        return chr(ord('a') + number - 1)
    else:
        return "Invalid input: Number out of range"
##
#
def letter_to_number(letter):
    if len(letter) == 1 and 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    else:
        return "Invalid input: Not a lowercase letter"

##
#
def possitionnerPiece(grille, posX, posY, joueur=1, piece = [[1,1,1],[1,0,0]] ):
    if joueur == 1:
        symbol = '0 '
    elif joueur == 2:
        symbol = '# '
    else:
        symbol = 'X '  # You can add more players and symbols if needed

    for i in range(len(piece)):
       for j in range(len(piece[i])):
           if piece[i][j] == 1:
               grille[posY + i][posX + j] = symbol

##
#
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

##
#
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

##
#
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
##
#
def verifierPiece(x,y,grille,joueur=1,piece = [[1,1,1],[1,0,0]] ):
    #piece = selectionnerUnePiece()
    #for i in range(0,piece):
    cote = verifierCote(grille, x, y, joueur)
    angle = verifierAngle(grille, x, y, joueur)
    
    if (cote == False) or (angle == False):
        print("invalide")
        return
    
    #for i in range(piece):
    possitionnerPiece(grille,x,y, joueur, piece)
    
