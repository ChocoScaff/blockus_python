# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:26:36 2023

@author: PC
"""



def console_afficheGrille (grille) : 
    """Affiche le rectangle d'etoiles  (tout ceci en meme
    temps et non pas le rectangle puis la )  """
    for ligne in range (21) :
        for colonne in range (21) :
            print (grille[ligne][colonne],end="")
        print(" ")


def console_effaceEcran ():
    for i in range (1,100) :
        print("\n")