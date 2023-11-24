##
#@file blockus_solo.py
#

import time
from console import *

from blockus_shared import *
from pieces import Piece


grille = [[' ' for i in range(21)] for _ in range(21)]
initGrille(grille)

Piece(1, 1)

round = 1
while True:
    s = input("Appuyez sur la touche entrée ou 's' pour sortir... ")

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

    verifierPiece(x, y, grille, 1)

    console_afficheGrille(grille)

    round = +1
