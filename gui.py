
import pygame 

##
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

##
# size
WIDH_SCREEN = 800
HEIGHT_SCREEN = 800
ROW = 20
COLUMNS = 20
grid_size = 20
cell_size = 80

##
# @class gui
class gui:

    def __init__(self):
        # pygame setup
        print("Init Pygame")
        pygame.init()
        self.screen = pygame.display.set_mode((WIDH_SCREEN, HEIGHT_SCREEN))
        self.clock = pygame.time.Clock()
        self.event = pygame.event.wait()
    
    def drawGrille(self):
         # Draw the grid
        self.screen.fill("white")

        for row in range(grid_size):
            for col in range(grid_size):
                rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(self.screen, black, rect, 1)  # 1 is the border thickness

        # Update the display
        pygame.display.flip()
        self.event = pygame.event.wait()
    
    def drawPiece(self,grille):
        for ligne in range (1,21) :
            for colonne in range (1,21) :
                if grille[ligne][colonne] == '0 ':
                    rect = pygame.Rect((colonne-2) * cell_size, (ligne-2) * cell_size, cell_size, cell_size)
                    pygame.draw.rect(self.screen, red, rect, 0)  # 1 is the border thickness
                elif grille[ligne][colonne] == '# ':
                    rect = pygame.Rect((colonne-2) * cell_size, (ligne-2) * cell_size, cell_size, cell_size)
                    pygame.draw.rect(self.screen, green, rect, 0)  # 1 is the border thickness
        
        # Update the display
        pygame.display.flip()
        self.event = pygame.event.wait()

    
    def event(self):
        keys = pygame.key.get_pressed()
    
    def __del__(self):
        pygame.quit()
    