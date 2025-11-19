import pygame
import sys

from funktions import *

pygame.init()
screen = pygame.display.set_mode((1, 1))  

# Immages 
background = pygame.image.load("pictures/roulette_simple_text.jpg").convert_alpha()
background = pygame.transform.scale(background, 
                                   (background.get_width()/6,
                                    background.get_height()/6))

# Backround
img_w = background.get_width()
img_h = background.get_height()
screen = pygame.display.set_mode((img_w,  img_h ))

# Colors
WHITE = (255, 255, 255)
GREEN_BACKROUND = (31, 146, 17)
DARK_GREEN = (42, 94, 36)
DARKGRAY = (120, 120, 120)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (199, 21, 8) 

# fonts
fonts_outside = pygame.font.SysFont(None, 40)

#Chip Fariablen 
blue_chip_coordinates = (200, 650)
red_chip_coordinates = (290, 650)
black_chip_coordinates = (290, 650)

chip_radius = 15          
# button_text = 'Click Me!'

def main():
    running = True

    manque = pygame.Rect(481, 500, 150, 50)
    passe = pygame.Rect(490, 170, 120, 50)
    impair = pygame.Rect(320, 500, 150, 50)
    pair =  pygame.Rect(320, 170, 120, 50)

    while running:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(background, (0,0))

        #Drawing the objekts
        draw_chips(red_chip_coordinates, chip_radius, RED)
        draw_chips(blue_chip_coordinates, chip_radius, BLUE)

        # draw_rect_with_text(manque, "Manque", mouse_pos)
        # draw_rect_with_text(passe, "Passe", mouse_pos)
        # draw_rect_with_text(impair, "Impair", mouse_pos)
        # draw_rect_with_text(pair, "Pair", mouse_pos)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if manque.collidepoint(mouse_pos):
                    print("Button 1 clicked!")

                mouse_x, mouse_y = event.pos
                distance = ((mouse_x - red_chip_coordinates[0]) ** 2 + 
                            (mouse_y - red_chip_coordinates[1]) ** 2) ** 0.5
                
                if distance <= chip_radius:
                    print('Button clicked!')

        #Displaying everthing at the end
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
