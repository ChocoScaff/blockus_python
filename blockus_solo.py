##
#@file blockus_solo.py
#

# Imports
import time
from console import *
from blockus_shared import *
from pieces import Piece
from gui import gui

grille = [[' ' for i in range(21)] for _ in range(21)]
initGrille(grille)

screen = gui()
screen.drawGrille()

round = 1
while True:
    s = input("Appuyez sur la touche entrée ou 's' pour sortir... ")

    x = input("Entree la colonne ")
    x = x.lower()
    if 'a' <= x <= 'z':
        x = ord(x) - 86
    else:
        x = int(x) + 1

    y = input("Entrer la ligne ")
    y = y.lower()
    if 'a' <= y <= 'z':
        y = ord(y) - 86
    else:
        y = int(y) + 1

    pieceChoisie = int(input("Selectionner une pièce : "))
    pieceInstance = Piece(pieceChoisie,1)
    rotation = int(input("Selectionner la rotation : "))
    pieceInstance.rotatePiece(rotation)
    data = pieceInstance.getPiece()
    verifierPiece(x, y, grille, 1, data )
    #verifierPiece(x, y, grille, 1, [[1],[1]] )

    console_afficheGrille(grille)
    screen.drawPiece(grille)

    round = +1
