# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:30:56 2023

@author: jradzied
"""
# pieces.py

class Piece:
    def __init__(self, shape, color):
        self.shape = shape  # Liste représentant la forme de la pièce
        self.color = color  # Couleur de la pièce

# Liste des pièces possibles
pieces = [
    Piece([[1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]], 'rouge'),  # Carré 5x5

    Piece([[1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1]], 'rouge'),  # Rectangle 3x7

    Piece([[0, 1, 0],
           [1, 1, 1],
           [1, 1, 1]], 'rouge'),  # Triangle équilatéral 3x3

    Piece([[1, 1],
           [1, 1]], 'rouge'),  # Simple rectangle 2x2
]

