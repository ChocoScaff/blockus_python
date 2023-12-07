
import pygame 

##
# Colors
white = (255, 255, 255)
black = (0, 0, 0)

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
    
    def updateGrille(self,grille):
         # Draw the grid
        self.screen.fill("white")

        for row in range(grid_size):
            for col in range(grid_size):
                rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(self.screen, black, rect, 1)  # 1 is the border thickness

        # Update the display
        pygame.display.flip()
        
    
    def event(self):
        keys = pygame.key.get_pressed()
    
    def __del__(self):
        pygame.quit()
    