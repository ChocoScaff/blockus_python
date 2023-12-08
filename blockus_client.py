##
#@file blockus_client.py
#

# Imports
import time
from console import *
from blockus_shared import *
import asyncio
import json
from pieces import Piece
from gui import gui

##################################    
#client    
##################################
##
#
async def send_receive_matrix(reader, writer):
    
    #grille= [[' ' for i in range(21)] for j in range(21)] 	# grille qui pourra contenir
                    # 3 sortes de caractères : '*' ou 'O' ou le caractere espace ' '

    #initGrille (grille) 
    #matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    grille = [[' ' for i in range(21)] for _ in range(21)]
    initGrille(grille)
    

    screen = gui()
    screen.drawGrille()

    round=1
    while True:

        screen.wait_event()

        s=input("Appuyez sur la touche entrée ou 's' pour sortir... ")
        
        
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

        pieceChoisie = int(input("Selectionner une pièce 1-21 :"))
        pieceInstance = Piece(pieceChoisie,1)
        data = pieceInstance.getPiece()
        rotation = int(input("Selectionner la rotation (0-3) 1 = 90deg : "))
        pieceInstance.rotatePiece(rotation)         
        verifierPiece(x, y, grille, 1, data)
    
        grille_json = json.dumps(grille)
        writer.write(grille_json.encode())
        print("Matrice envoyée au serveur")

        screen.get_event()
        console_afficheGrille(grille)
        screen.drawPiece(grille)
        
        print("Attente du serveur")
            
        await writer.drain()
        
        data = await reader.read(4096)
        grille_json = data.decode()
        grille = json.loads(grille_json)
        print("Matrice reçue du serveur :")

        screen.get_event()
        console_afficheGrille(grille)
        screen.drawPiece(grille)

        #for row in grille:
        #    print(row)
        round=+1
        
##
#
async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    
    await send_receive_matrix(reader, writer)

    writer.close()
    await writer.wait_closed()
    
##################################
# programme principal :
##################################

#client 
asyncio.run(main())
