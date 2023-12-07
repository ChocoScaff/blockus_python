
import pygame 

class gui:

    def __init__(self):
        # pygame setup
        print("Init Pygame")
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
    
    def updateGrille(self,grille):
        return
    
    def __del__(self):
        pygame.quit()
    