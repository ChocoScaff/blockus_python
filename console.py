##
#@file console.py
#

from colorama import Fore, Back, Style

##
#
def console_afficheGrille (grille) : 
    """Affiche le rectangle d'etoiles  (tout ceci en meme
    temps et non pas le rectangle puis la )  """
    for ligne in range (21) :
        for colonne in range (21) :
            if grille[ligne][colonne] == '0 ':
                print (Fore.RED + str(grille[ligne][colonne]),end="")
            elif: grille[ligne][colonne] == '# ':
                print (Fore.GREEN + str(grille[ligne][colonne]),end="")
            else:
                print (Fore.WHITE + str(grille[ligne][colonne]),end="")
        print(" ")

##
#
def console_effaceEcran ():
    for i in range (1,100) :
        print("\n")