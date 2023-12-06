##
# @file pieces.py
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:30:56 2023

@author: jradzied
"""
# pieces.py

##
# @class Piece
#
class Piece:
    ##
    # @param shape
    # @param color 
    def __init__(self, shape, color):
        print("Init Piece")

        self.shape = shape  # Liste représentant la forme de la pièce
        self.color = color  # Couleur de la pièce

       #see ref img/blockus.png
        if self.shape == 1:
           self.piece = [[1],[0]]  # Carré 1x1
        elif self.shape == 2:
           self.piece = [[1],[1]]  # rectangle 1x2
        elif self.shape == 3:
           self.piece = [[1],[1],[1]]
        elif self.shape == 4:
           self.piece = [[1,0],[1,1]]  
        elif self.shape == 5:
           self.piece = [[1],[1],[1],[1]] 
        elif self.shape == 6:
           self.piece = [[0,1],[0,1],[1,1]]  
        elif self.shape == 7:
           self.piece = [[1,0],[1,1],[1,0]] 
        elif self.shape == 8:
           self.piece = [[1,1],[1,1]]    

    ##
    #    
    def getPiece(self):
       return self.piece     
              
       

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

