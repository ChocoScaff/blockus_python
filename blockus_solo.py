##
#@file blockus_solo.py
#

# Imports
import time
from console import *
from blockus_shared import *
from pieces import Piece


grille = [[' ' for i in range(21)] for _ in range(21)]
initGrille(grille)


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

    verifierPiece(x, y, grille, 1, [[1,1],[0]])

    console_afficheGrille(grille)

    round = +1
