##
#@file blockus_server.py
#

# Imports
import time
from console import *
from blockus_shared import *
import asyncio
import json
from pieces import Piece
from gui import gui


##
# @param number
#
def number_to_letter(number):
    if 1 <= number <= 26:
        return chr(ord('a') + number - 1)
    else:
        return "Invalid input: Number out of range"
##
# @param letter
#
def letter_to_number(letter):
    if len(letter) == 1 and 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    else:
        return "Invalid input: Not a lowercase letter"


    
##################################    
#server    
##################################
##
# @param reader
# @param writer
# 
#
async def handle_client(reader, writer):
    
    #grille= [[' ' for i in range(21)] for j in range(21)] 	# grille qui pourra contenir
                    # 3 sortes de caractères : '*' ou 'O' ou le caractere espace ' '

    #initGrille (grille) 

    screen = gui()
    screen.drawGrille()

    round=1
    while True:

        
        print("Attente du client :")
        data = await reader.read(4096)
        if not data:
            break
        grille_json = data.decode()
        grille = json.loads(grille_json)
        print("Matrice reçue du client :")

        screen.get_event()
        console_afficheGrille(grille)
        screen.drawPiece(grille)
        #screen.wait_event()

        #for row in grille:
        #    print(row)
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
        verifierPiece(x, y, grille, 2, data)
        
        grille_json = json.dumps(grille)
        writer.write(grille_json.encode())
        await writer.drain()
        print("Matrice modifiée renvoyée au client")

        screen.get_event()
        console_afficheGrille(grille)
        screen.drawPiece(grille)
        #screen.wait_event()

        round +=1
        
    writer.close()
    
##
# 
async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serveur en attente de connexions sur {addr}')

    async with server:
        await server.serve_forever()
    
##################################
# programme principal :
##################################

asyncio.run(main())
